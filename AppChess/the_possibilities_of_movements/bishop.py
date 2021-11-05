def BISHOPpossibility (chessBoard, piece) :
    places= list()                                                                          
    #value of piece                                                                         
    pieceNumber= chessBoard[piece[0]][piece[1]] 
                                 
    #test1 below right the piece 
    i = piece[0] + 1                                        
    j=  piece[1] + 1 
    while i < 8 and j < 8 :
        if chessBoard[i][j] != 0  :
            
            if (chessBoard[i][j] * pieceNumber ) < 0 :
                places.append((i, j))
            break
        places.append((i, j))
        i += 1
        j += 1
    #test2 below left the piece 
    i = piece[0] + 1       
    j= piece[1] - 1 
    while i < 8 and j >= 0 :
        if chessBoard[i][j] != 0  :
            if (chessBoard[i][j] * pieceNumber ) < 0  :
                places.append((i, j))
            break
        places.append((i, j))
        i += 1
        j -= 1

    #test3 above right the piece
    i = piece[0] - 1                                        
    j=  piece[1] + 1 
    while i >=0 and j < 8 :
        if chessBoard[i][j] != 0  :
            if (chessBoard[i][j] * pieceNumber ) < 0 :
                places.append((i, j))
            break
        places.append((i, j))
        i -= 1
        j += 1
    #test4 above left the piece  
    i = piece[0] - 1       
    j= piece[1] - 1 
    while i >= 0 and j >= 0 :
        
        if chessBoard[i][j] != 0  :
            if (chessBoard[i][j] * pieceNumber ) < 0  :
                places.append((i, j))
            break
        places.append((i, j))
        i -= 1
        j -= 1
    return places