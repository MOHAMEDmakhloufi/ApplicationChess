# from the_possibilities_of_movements.inCheck import *


def KINGpossibility (chessBoard, piece) :
    places= list()                                                                          
    #value of piece                                                                         
    pieceNumber= chessBoard[piece[0]][piece[1]] 

    #inialisation
    listPlaceOfKing = [
        (piece[0] + 1, piece[1]),
        (piece[0] + 1, piece[1] + 1),
        (piece[0] + 1, piece[1] - 1),
        (piece[0]    , piece[1] + 1),
        (piece[0]    , piece[1] - 1),
        (piece[0] - 1, piece[1]),
        (piece[0] - 1, piece[1] + 1),
        (piece[0] - 1, piece[1] - 1)
    ]
    for i, j in listPlaceOfKing :
        if i < 8 and i >= 0 and j < 8 and j >= 0 :
            # if  inCheck(chessBoard, piece, (i, j)) :
            #     continue
            if chessBoard[i][j] != 0 :
                #if the piece color is different
                if (chessBoard[i][j] * pieceNumber ) < 0 :
                    places.append((i, j))
                continue    
            places.append((i, j))        
    #for white
    if pieceNumber > 0 and piece == (7, 4) :
        if chessBoard[7][0] == 5 and chessBoard[7][1] == 0 and chessBoard[7][2] == 0 and chessBoard[7][3] == 0 :
            places.append((7, 2))
        if chessBoard[7][7] == 5 and chessBoard[7][5] == 0 and chessBoard[7][6] == 0 :
            places.append((7, 6))   
    #for black
    elif pieceNumber < 0 and piece == (0, 4)  :
        if chessBoard[0][0] == 5 and chessBoard[0][1] == 0 and chessBoard[0][2] == 0 and chessBoard[0][3] == 0 :
            places.append((0, 2))
        if chessBoard[0][7] == 5 and chessBoard[0][5] == 0 and chessBoard[0][6] == 0 :
            places.append((0, 6))          
    return places
