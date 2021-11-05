from the_possibilities_of_movements.rook import *
from the_possibilities_of_movements.bishop import *
from the_possibilities_of_movements.queen import *
from the_possibilities_of_movements.knight import *
from the_possibilities_of_movements.pawn import *
from the_possibilities_of_movements.king import *
from the_possibilities_of_movements.inCheck import *
from the_possibilities_of_movements.searchPiece import *

def move (ChessBoard : list, Fpos, Tpos) :
    
    newChessBoard  = [ line.copy() for line in ChessBoard]
    
    newChessBoard [Tpos[0]][Tpos[1]], newChessBoard [Fpos[0]][Fpos[1]] = newChessBoard [Fpos[0]][Fpos[1]], 0

    return newChessBoard 

def possibiltyWithoutCheck (chessBoard, piece) :
    places= list() 
    #value of piece    
    pieceNumber= chessBoard[piece[0]][piece[1]]

    #search king position by value(500 if white , -500 if black)
    king = searchPiece(chessBoard, 500 if pieceNumber > 0 else -500) 

    # black or white
    pieceNumber= abs(pieceNumber)

    if pieceNumber == 5 :
        places= ROOKpossibility(chessBoard, piece)
    elif pieceNumber == 2 :
        places= KNIGHTpossibility(chessBoard, piece)   
    elif pieceNumber == 3 :
        places= BISHOPpossibility(chessBoard, piece)
    elif pieceNumber == 9 :
        places= QUEENpossibility(chessBoard, piece) 
          
    elif pieceNumber == 1 :
        places= PAWNpossibility(chessBoard, piece)
    elif pieceNumber == 500 :
        places= KINGpossibility(chessBoard, piece)  
    else :
        return []
    newPlaces = list()
    #test inCheck
    for i, j in places : 
        if pieceNumber == 500 :
            king = (i, j)
           
        if inCheck(move(chessBoard, piece, (i, j)), king) :
            continue
        newPlaces.append((i, j))
   
    return newPlaces