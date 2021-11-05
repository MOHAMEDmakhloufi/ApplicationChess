from bestMove import bestMove
from the_possibilities_of_movements.inCheck import inCheck
from the_possibilities_of_movements.possibility import possibility
from the_possibilities_of_movements.possibiltyWithoutCheck import possibiltyWithoutCheck
from gameOver import gameOver
from move import move
from consultChessBoard import consultChessBoard
from the_possibilities_of_movements.searchPiece import searchPiece
from bestMove import minmax
#inialisation
chessBoard = [
    [-5, -2, -3, -9,  -500, -3, -2, -5],
    [-1, -1, -1,    -1, -1, 0, -1, -1],
    [ 0,  0,  0,  0 ,  0,  0,  0,  0],
    [ 0,  0,  0,   0,  0,  0,  0,  0],

    [0,  0, 3,    0,  0,  0,  0,  0],
    [ 0,  0,  0,   0,  0,  9,  0,  0],
    [ 1,  1,  1,   0,  0,  1,  1, 1],
    [ 5,  2,  3,  0,  500,  0,  2, 5]        
]
    # [-5, -2, -3, -9,  -500, -3, -2, -5],
    # [-1, -1, -1,    -1, -1, -1, -1, -1],
    # [ 0,  0,  0,  0 ,  0,  0,  0,  0],
    # [ 0,  0,  0,   0,  0,  0,  0,  0],

    # [0,  0,  0,    0,  0,  0,  0,  0],
    # [ 0,  0,  0,   0,  0,  0,  0,  0],
    # [ 1,  1,  1,    1,  1,  1,  1, 1],
    # [ 5,  2,  3,  9,  500,  3,  2, 5] 
consultChessBoard(chessBoard)
game = int(input("Do you want to play in white or black : \n    1.White\n   -1.Black \n-->"))  

while not gameOver(chessBoard, game) :
    print("You") if game == 1 else print("COMPETITOR")
    #best move
    test = 0
    if game == 1 :
        dic = bestMove(chessBoard)
        bMove = dic[0]
        SecondBMove = dic[1]
        print("\t the best move", bMove)
        if len(SecondBMove) != 0 :
            print("\t second best move", SecondBMove)
        print("\t1.Selected This Move",
             "\n\t2.Selected This Second Best Move" if len(SecondBMove) != 0 else "" ,
             "\n\t0.No \n\t", end="--> ")    
        test = int(input())
        
    game *= -1
    if test == 1 :
        for t1,t2 in bMove.items() :
            newPosPiece = move(chessBoard, t1, t2)
    elif test == 2 and len(SecondBMove) != 0 :
        for t1,t2 in SecondBMove.items() :
            newPosPiece = move(chessBoard, t1, t2)        
    else :
        newPosPiece = move(chessBoard)
    if newPosPiece != (100, 100) :
        #search king position by value(500 if white , -500 if black)
        king = searchPiece(chessBoard, 500 if game > 0 else -500) 
        if inCheck(chessBoard, king, newPosPiece) :
            print("\t\t\t***inCHECK***")
    consultChessBoard(chessBoard)
print( "Gamme Over ", "YOU ARE WINNER" if game < 0 else "HE ARE WINNER" )
consultChessBoard(chessBoard)