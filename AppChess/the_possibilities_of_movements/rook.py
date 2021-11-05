from the_possibilities_of_movements.searchPiece import searchPiece
def ROOKpossibility (chessBoard, piece) :
    places= list()                                                                          
    #value of piece                                                                         
    pieceNumber= chessBoard[piece[0]][piece[1]] 
    #search king position by value(500 if white , -500 if black)
    king = searchPiece(chessBoard, 500 if pieceNumber > 0 else -500)                                             
    #test2 next to the piece                                         
    j=  piece[1] + 1 
    while j < 8 :
        if chessBoard[piece[0]][j] != 0  :
            #if the piece color is different
            if (chessBoard[piece[0]][j] * pieceNumber ) < 0 :
                places.append((piece[0], j))
            break
        places.append((piece[0], j))
        j +=1
    #test1 next to the piece       
    j= piece[1] - 1
    while j >= 0 :
        if chessBoard[piece[0]][j] != 0  :
            if (chessBoard[piece[0]][j] * pieceNumber ) < 0  :
                places.append((piece[0], j))
            break
        places.append((piece[0], j))
        j -=1
    
    #test below the piece                                         
    i=  piece[0] + 1 
    while i < 8 :
        if chessBoard[i][piece[1]] != 0  :
            if (chessBoard[i][piece[1]] * pieceNumber ) < 0 :
                places.append((i, piece[1]))
            break
        places.append((i, piece[1]))
        i +=1
        
    #test above the piece       
    i= piece[0] - 1
    while i >= 0 :
        if chessBoard[i][piece[1]] != 0 :
            if (chessBoard[i][piece[1]] * pieceNumber ) < 0  :
                places.append((i, piece[1]))
            break
        places.append((i, piece[1]))
        i -=1
    return places



