#written by akshay Patil
while True:
    board=["  " for i in range(9)]
    def print_board():
        print(" ")
        print("| {} | {} | {} |".format( board[0],board[1],board[2] ))
        print("| {} | {} | {} |".format( board[3],board[4],board[5] ))
        print("| {} | {} | {} |".format( board[6],board[7],board[8] ))
        print(" ")
    print(" ")
    print("Welcome to Tic Tac Toe !!! ")

    p1=input("Enter name of player 1 :- ")
    p2=input("Enter name of player 2 :- ")

    print("okk then, lets begin the game")
    print("Here is your game board")
    print_board()

    print("Player 1 will start the game")
    print("Rules:- When prompted enter the box number(1-9) in which you want to place your move and press enter")

    def is_victory(icon):
        if(board[0]==icon and board[1]==icon and board[2]==icon) or \
           (board[3]==icon and board[4]==icon and board[5]==icon) or \
           (board[6]==icon and board[7]==icon and board[8]==icon) or \
           (board[0]==icon and board[3]==icon and board[6]==icon) or \
           (board[1]==icon and board[4]==icon and board[7]==icon) or \
           (board[2]==icon and board[5]==icon and board[8]==icon) or \
           (board[0]==icon and board[4]==icon and board[8]==icon) or \
           (board[2]==icon and board[4]==icon and board[6]==icon):
            return True
        else:   return False
        
    def if_draw():
        if "  " not in board:
            return True
        else:
            return False
    
       
       
   
    for i in range(1,10):
        while True:
            if i%2!=0:
                move=int(input("{} 's move :- ".format(p1)).strip())
                if board[move-1]=="  ":
                    board[move-1]="X"
                    print_board()             
                    break
                else:
                    print("That space is taken ")
            elif i%2 ==0:
                move=int(input("{} 's move :- ".format(p2)).strip())
                if board[move-1]=="  ":
                    board[move-1]="O"
                    print_board()
                    is_victory("O")
                    break
                else:   print("That space is taken ")
        if is_victory("X"):
            print("Congratulations {} , you have won the game !!!".format(p1))
            break
        elif if_draw():
            print("Its a draw !!!")
            print(" ")
            break
        if is_victory("O"):
            print("Congratulations {} , you have won the game !!!".format(p2))
            break
        elif if_draw():
            print("Its a draw !!!")
            print(" ")
            break
    
    
    
                    

            
        
            
    


        
    
        
        
            
        
            
            
            
        
        
    
     


    
