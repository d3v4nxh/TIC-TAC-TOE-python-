import random

#for double player 
def double_player():
      def sum(a,b,c):
            return a+b+c
#printing the board            
      def printBoard(xState,zState):
#these function stands for the live interchanging of values of 'X' or 'O'
            zero='X'if xState[0] else('O'if zState[0] else 0)
            one='X'if xState[1] else('O'if zState[1] else 1)
            two='X'if xState[2] else('O'if zState[2] else 2)
            three='X'if xState[3] else('O'if zState[3] else 3)
            four='X'if xState[4] else('O'if zState[4] else 4)
            five='X'if xState[5] else('O'if zState[5] else 5)
            six='X'if xState[6] else('O'if zState[6] else 6)
            seven='X'if xState[7] else('O'if zState[7] else 7)
            eight='X'if xState[8] else('O'if zState[8] else 8)

            print(f" {zero} | {one} | {two} ")
            print(f"---|---|---")
            print(f" {three} | {four} | {five} ")
            print(f"---|---|---")
            print(f" {six} | {seven} | {eight} ")
# for checking the win      
      def checkwin(xState,Zstate):
            Wins =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
            for win in Wins:
                  if (sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
                        print("X won the match ;) ")
                        return 1
                  if (sum(zState[win[0]],zState[win[1]],zState[win[2]]) == 3):
                        print("O won the match :) ")
                        return 0
            return -1
#main function            
      if __name__ == "__main__":
            xState = [0,0,0,0,0,0,0,0,0]
            zState = [0,0,0,0,0,0,0,0,0]
            turn = 1
# Be cautious on using while true and its condition            
            while(True): 
                  printBoard(xState,zState)
                  if(turn == 1): 
                        print("X's Chance")
                        value = int(input("Please enter your CHOICE: "))
                        xState [value]=1
                  else:
                        print("O's chance")
                        value = int(input("Please enter your CHOICE: "))
                        zState[value]=1
                  cwin=checkwin(xState,zState)
                  if(cwin!=-1):
                        print("match over")
                        break    
                  turn = 1- turn
#For single player OR player vs machine 
def single_player():
      board = [[' ' for _ in range(3)] for _ in range(3)]
      def display_board(board):
          print(" 0 | 1 | 2 ")
          print("-----------")
          print(" 3 | 4 | 5 ")
          print("-----------")
          print(" 6 | 7 | 8 ")
          for i in range(3):
              for j in range(3):
                  if j < 2:
                      print(f"{board[i][j]} |", end=" ")
                  else:
                      print(board[i][j])

      def is_winner(board, player):
          # Check rows, columns, and diagonals for a win
          for i in range(3):
              if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                  return True
          if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
              return True
          return False

      def is_draw(board):
          return all(board[i][j] != ' ' for i in range(3) for j in range(3))

      def is_game_over(board):
          return is_winner(board, 'X') or is_winner(board, 'O') or is_draw(board)
      def minimax(board, depth, is_maximizing):
          if is_winner(board, 'X'):
              return -1
          if is_winner(board, 'O'):
              return 1
          if is_draw(board):
              return 0

          if is_maximizing:
              max_eval = -float('inf')
              for i in range(3):
                  for j in range(3):
                      if board[i][j] == ' ':
                          board[i][j] = 'O'
                          eval = minimax(board, depth + 1, False)
                          board[i][j] = ' '
                          max_eval = max(max_eval, eval)
              return max_eval
          else:
              min_eval = float('inf')
              for i in range(3):
                  for j in range(3):
                      if board[i][j] == ' ':
                          board[i][j] = 'X'
                          eval = minimax(board, depth + 1, True)
                          board[i][j] = ' '
                          min_eval = min(min_eval, eval)
              return min_eval
      def ai_move(board):
          best_move = None
          best_eval = -float('inf')
          for i in range(3):
              for j in range(3):
                  if board[i][j] == ' ':
                      board[i][j] = 'O'
                      eval = minimax(board, 0, False)
                      board[i][j] = ' '
                      if eval > best_eval:
                          best_eval = eval
                          best_move = (i, j)
          return best_move
      def make_player_move(board, move, player):
          mapping = {
              0: (0, 0), 1: (0, 1), 2: (0, 2),
              3: (1, 0), 4: (1, 1), 5: (1, 2),
              6: (2, 0), 7: (2, 1), 8: (2, 2)
          }
          row, col = mapping.get(move)
          if row is not None and col is not None and board[row][col] == ' ':
              board[row][col] = player
              return True
          else:
              return False

      while not is_game_over(board):
          display_board(board)

          if len([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']) % 2 == 0:
              i, j = ai_move(board)
              board[i][j] = 'O'
          else:
              try:
                  move = int(input("Enter your move (0-8): "))
                  if make_player_move(board, move, 'X'):
                      continue
                  else:
                      print("Invalid move. That position is already taken or out of range. Try again.")
                      continue
              except ValueError:
                  print("Invalid input. Please enter a valid number from 0 to 8.")

      display_board(board)
      if is_winner(board, 'X'):
          print("You win!")
      elif is_winner(board, 'O'):
          print("AI wins!")
      else:
          print("It's a draw!")



print("welcome to tic tac toe ")
while (True):
      print("ENTER 1 FOR MULTIPLAYER GAME ")
      print("ENTER 2 FOR SINGLE PLAYER GAME")
      print("ENTER 3 FOR EXIT THE GAME ")
      x = int(input("ENTER YOUR CHOICE :  "))
      match x: 
            case 1:
                  double_player()                  
            case 2:
                  single_player()                  
            case 3:
                  print("THANK YOU FOR PLAYING GAME ") 
                  break                        
            case _:
                  print("INCORRECT CHOICE")
                  