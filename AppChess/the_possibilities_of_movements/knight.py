def KNIGHTpossibility (chessBoard, piece) :

    places= list() 
    #value of piece                                                                         
    pieceNumber= chessBoard[piece[0]][piece[1]] 
    #inialisation
    listPlaceOfKnight = [
        (piece[0] + 2, piece[1] + 1),
        (piece[0] + 2, piece[1] - 1),
        (piece[0] - 2, piece[1] + 1),
        (piece[0] - 2, piece[1] - 1),
        (piece[0] + 1, piece[1] + 2),
        (piece[0] - 1, piece[1] + 2),
        (piece[0] + 1, piece[1] - 2),
        (piece[0] - 1, piece[1] - 2)
    ]

    for i, j in listPlaceOfKnight :
        if i < 8 and i >= 0 and j < 8 and j >= 0 :
            
            if chessBoard[i][j] != 0 :
                #if the piece color is different
                if (chessBoard[i][j] * pieceNumber ) < 0 :
                    places.append((i, j))
                continue    
            places.append((i, j))        

    return places