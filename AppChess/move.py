from the_possibilities_of_movements.possibiltyWithoutCheck import possibiltyWithoutCheck
from consultChessBoard import consultChessBoard
from from_Pawn_To_Queen import pawnTOqueen
from King_And_Tour import King_And_Tour

def move (chessBoard, Fpos=(100,100), Tpos=(100, 100)) :
    newPosPiece = (100, 100)
    ch = 1
    while ch != 0 :
        #input
        if  Fpos == (100,100) and  Tpos == (100, 100) :
            Fpos = int(input("\tmove from : \n\tline : ")), int(input("\tcolumn : "))
            if testInput(Fpos) :
                print(f"\t\tthe possibilty of {Fpos} ",possibiltyWithoutCheck(chessBoard, Fpos))    
            Tpos = int(input("\tto : \n\tline : ")), int(input("\tcolumn : "))

        if testInput(Fpos) and testInput(Tpos) :
            if Tpos in possibiltyWithoutCheck(chessBoard, Fpos) :
                King_And_Tour(chessBoard, Fpos, Tpos)
                if not pawnTOqueen(chessBoard, Fpos, Tpos) :
                    chessBoard[Tpos[0]][Tpos[1]], chessBoard[Fpos[0]][Fpos[1]] = chessBoard[Fpos[0]][Fpos[1]], 0
                newPosPiece = Tpos
                ch = 0
            else :
                print("impossible\n\t\t")
                consultChessBoard(chessBoard)
                print(f"\t\tthe possibilties of {Fpos} are   ",possibiltyWithoutCheck(chessBoard, Fpos))
                Fpos = (100,100)
                Tpos = (100,100)
        else : 
            print("erreur")
            Fpos = (100,100)
            Tpos = (100,100)        
    return newPosPiece

testInput = lambda tup :  tup[0]<8 and tup[0] >= 0  and tup[1]<8 and tup[1] >= 0   