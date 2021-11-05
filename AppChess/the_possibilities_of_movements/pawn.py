def PAWNpossibility (chessBoard, piece) :
    places= list()                                                                          
    #value of piece                                                                         
    pieceNumber= chessBoard[piece[0]][piece[1]] 
                                               
    # piece white
    if pieceNumber > 0 :
        if piece[0] == 6 :
            for i in range(1, 3) :
                j = piece[0] - i
                if j >= 0 :
                    if chessBoard[j][piece[1]] != 0 :
                        break
                    places.append((j, piece[1]))
        else :
            j = piece[0] - 1
            if j >= 0 :
                if chessBoard[j][piece[1]] == 0 :
                    places.append((j, piece[1]))
        
        i = piece[0] - 1                                        
        j=  piece[1] + 1
        if i >=0 and j < 8 : 
            #if the piece color is different
            if  (chessBoard[i][j] * pieceNumber ) < 0  :
                places.append((i, j))
                                                        
        j=  piece[1] - 1
        if i >=0 and j >= 0 : 
            if (chessBoard[i][j] * pieceNumber ) < 0  :
                places.append((i, j))   
    #if piece black             
    if pieceNumber < 0 :
        if piece[0] == 1 :
            for i in range(1, 3) :
                j = piece[0] + i
                if j < 8 :
                    if chessBoard[j][piece[1]] != 0 :
                        break
                    places.append((j, piece[1]))
        else :
            j = piece[0] + 1
            if j < 8 :
                if chessBoard[j][piece[1]] == 0 :
                    places.append((j, piece[1]))
        
        i = piece[0] + 1                                        
        j=  piece[1] + 1
        if i < 8 and j < 8 : 
            if  (chessBoard[i][j] * pieceNumber ) < 0  :
                places.append((i, j))
                                                        
        j=  piece[1] - 1
        if i < 8 and j >= 0 : 
            if (chessBoard[i][j] * pieceNumber ) < 0  :
                places.append((i, j))                     

    return places