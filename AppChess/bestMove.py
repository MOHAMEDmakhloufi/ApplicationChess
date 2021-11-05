
from the_possibilities_of_movements.possibility import possibility
from the_possibilities_of_movements.possibiltyWithoutCheck import possibiltyWithoutCheck
from the_possibilities_of_movements.inCheck import inCheck
from gameOver import gameOver
import math
from the_possibilities_of_movements.searchPiece import searchPiece
from King_And_Tour import King_And_Tour
# calculate score  
# each piece has a score = value * 10 + number of possibilities 
def calculateScore (chessBoard) :
    score = 0
    for i, line in enumerate(chessBoard) :
        for j, column in enumerate(line) :
            if column > 0 :
                 score += (column * 10) + len( possibiltyWithoutCheck(chessBoard, (i,j)) )
            elif column < 0 :
                score += (column * 10) - len( possibiltyWithoutCheck(chessBoard, (i,j)) )
    
    return score            

#end function calculateScore 

def move (ChessBoard : list, Fpos, Tpos) :
    
    newChessBoard  = [ line.copy() for line in ChessBoard]
    
    King_And_Tour(newChessBoard, Fpos, Tpos)
    newChessBoard [Tpos[0]][Tpos[1]], newChessBoard [Fpos[0]][Fpos[1]] = newChessBoard [Fpos[0]][Fpos[1]], 0

    return newChessBoard 

#start minmax
def minmax( chessBoard, listPossibilities, piece, depth, colorPlayer) : # white : True, Black : False
    
    if depth == 0 :
        return {piece : calculateScore(chessBoard)}
    # WHITE      
    if colorPlayer :
        #initialisation -oo
        maxEvaluation = { (100, 100) :-math.inf} 

        for child in listPossibilities :
            
            # test of game over or check
            kingWhite = searchPiece(chessBoard, 500)
            kingBlack = searchPiece(chessBoard, -500)
            if gameOver(move(chessBoard, piece, child), -10) :
                
                return {child : math.inf}
            if gameOver(move(chessBoard, piece, child), 10) :
                return {child : -math.inf} 
            #test inCheck    
            if inCheck(move(chessBoard, piece, child), kingBlack) :
                if not  piece_at_risk(move(chessBoard, piece, child), child) :
                    # print(child)
                    return {child : math.inf}
                else :
                    continue
            if inCheck(move(chessBoard, piece, child), kingWhite) :
                if  piece_at_risk(move(chessBoard, piece, child), child) :
                    return {child : math.inf}
                else :
                    continue
            if dangerousMove(move(chessBoard, piece, child), child, chessBoard[child[0]][child[1]]) :
                continue 
            if chessBoard[piece[0]][piece[1]] == 1 and child[0] == 0:
                return {child : math.inf}

            #end test    
            evaluation = minmax( move(chessBoard, piece, child), possibiltyWithoutCheck(move(chessBoard, piece, child), child), child, depth - 1, False)

            maxEvaluation.update(evaluation)
            maxEvaluation = max(maxEvaluation.items(), key=lambda x : x[1])
            
            #cast to dict
            if maxEvaluation[0] in evaluation :
                maxEvaluation = {child : maxEvaluation [1]}
            else :
                maxEvaluation = {maxEvaluation[0] : maxEvaluation [1]} 
        else : 
            return maxEvaluation    
    # BLACK
    if not colorPlayer :
        bad= { (100, 100) : math.inf}
        for i, line in enumerate(chessBoard) :
            for j, column in enumerate(line) :
                                            #if the piece color is different
                if chessBoard[i][j] != 0 and (chessBoard[i][j] * -1) < 0 :  
                    if possibiltyWithoutCheck(chessBoard, (i, j)) != [] :
                        evaluation = minmax(chessBoard, possibiltyWithoutCheck(chessBoard, (i, j)), (i, j), depth - 1, True)
                        bad.update(evaluation)
                        bad = min(bad.items(), key=lambda x : x[1])
                        #cast to dict
                        if bad[0] in evaluation :
                            bad = {(i, j) : bad [1]}
                        else :
                            bad = {bad[0] : bad [1]}

        return bad  
#end minmax    
   
#start function piece at risk
def piece_at_risk(ChessBoard, piece) :
    #value of piece                                                                         
    pieceNumber= ChessBoard[piece[0]][piece[1]] 
    for i, line in enumerate(ChessBoard) :
        for j, column in enumerate(line) :
                                                #if the piece color is different
            if ChessBoard[i][j] != 0 and (ChessBoard[i][j] * pieceNumber ) < 0 :
                if piece in possibility(ChessBoard, (i, j)) :

                    king = searchPiece(move(ChessBoard, (i, j), piece), 500 if pieceNumber < 0 else -500)
                    if inCheck(move(ChessBoard, (i, j), piece), king) :
                        return False 

    return True
#end function piece at risk

#start function dangerous move  
def dangerousMove(ChessBoard, piece, pieceNumberChild= (100, 100)) :
    #value of piece                                                                         
    pieceNumber= ChessBoard[piece[0]][piece[1]] 
    for i, line in enumerate(ChessBoard) :
        for j, column in enumerate(line) :
                                                #if the piece color is different
            if ChessBoard[i][j] != 0 and (ChessBoard[i][j] * pieceNumber ) < 0 :
                if piece in possibiltyWithoutCheck(ChessBoard, (i, j)) :
                    if pieceNumberChild == (100, 100) :
                        if abs(pieceNumber) > abs(ChessBoard[i][j]) :
                            return True
                    else :        
                        if pieceNumberChild != 0 and  abs(pieceNumber) >= abs(pieceNumberChild) :
                            return True
                        if abs(pieceNumber) >= abs(ChessBoard[i][j]) :
                            return True 
    return False
# end  function dangerous move              
def bestMove(chessBoard) :
    best= { (100, 100) : -math.inf}
    move2 = ""
    for i, line in enumerate(chessBoard) :
        for j, column in enumerate(line) :
                                            #if the piece color is white and different to zero
            if chessBoard[i][j] != 0 and chessBoard[i][j]  > 0 :  
                if possibiltyWithoutCheck(chessBoard, (i, j)) != [] :

                    evaluation = minmax(chessBoard, possibiltyWithoutCheck(chessBoard, (i, j)), (i, j), 3, True)
                    
                    key = list(evaluation.keys())
                    if dangerousMove(chessBoard, (i, j)) :
                        evaluation[key[0]] += 10
                    
                    l1 = list(best.values())
                    l2 = list(evaluation.values()) 
                    l3 = list(evaluation.keys())
                    if l1[0] == l2[0] :
                        move2 = {(i, j): l3[0]}
                    best.update(evaluation)

                    m = max(best.items(), key=lambda x : x[1])


                    if m[0] in evaluation :   
                        move = {(i, j): m[0]}
                        move2 = ""   
                    #cast to dict    
                    best = {m[0] : m[1]}
    return move , move2
