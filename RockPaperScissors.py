def get_ans (): 
  while True : 
   try:
    ans = int(input("Choose one of the following : "))
   except  ValueError:
    print("Enter the numbers you stupid! Try again!")
   else :
    break
  
  if ans == 1 :
   move = "Rock"
  elif ans == 2 :
   move = "Paper"
  else : move = "Scissors"
  return move
 

class bot :
 
 def __init__(self):
  bmove = ""
  count = range(3)
  
  if count == 1 :
   bmove = "Rock"
  elif count == 2 :
   bmove = "Paper"
  else : bmove = "Scissors"
  return bmove
 
print("1.Rock")
print("2.Paper")
print("3.Scissors")

# Game

player_ans = get_ans()
bot_ans = bot

if player_ans and bot_ans ==  "Rock" :
 
 print("So the match is equal")

elif player_ans and bot_ans ==  "Paper" :
 
 print("So the match is equal")

elif player_ans and bot_ans ==  "Scissors" :
 
 print("So the match is equal")

# 6

