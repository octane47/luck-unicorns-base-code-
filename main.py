from main import *
import random

# Funtions go here...
def yes_no(question):
    vaild = False
    while not vaild:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        if response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


def instructions():
    print("**** HOW TO PLAY ****")
    print()
    print("choose a starting amount (minimum $1, maximum $10).")
    print()
    print("then press <enter> to play. you will get either a horse, a zebra, a donkey or a unicorn")
    print()
    print("it costs a $1 per round. depending on your prize you might win some money back. here the payout amounts..." )
    print()
    print("unicorn : $5.00 balance increases by $4")
    print("horse: $0.50 balance decreases by $0.50")
    print("zebra: $0.50 balance decreases by 0.50")
    print("donkey: $0.00 balance decreases by $1")
    print()
    print("can you avoid the donkeys, get the unicorns and walk with cash in hand?")
    return ""


def num_check(question, low, high):
    error = "please enter a whole number between 1 and  10\n"

    vaild = False
    while not vaild:
        try:
            #ask the question
            response = int(input(question))
            
            # if the amount is too low / to high give
            if low  < response <= high:
                return response


            # output an error
            else:
              print(error)
        except ValueError:
          print(error)     

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} } {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""
# Main Routine goes here...
played_before = yes_no("have you played the game before? ")
     
if played_before == "no":
    instructions()
print ("lets pay i mean play")
# ask user how much they want to play with...
how_much =num_check("how much would you like to pay with? ", 0, 10)
print ("you will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input(" press enter to play...").lower()

while play_again == "":

  #increase # of rounds played
  rounds_played += 1

  #print round number
  print()
  print("*** Round #{} ***".format(rounds_played))

  chosen_num = random.randint(1, 100)

  #Adjust balance
  #if the random # is between 1 and 5,
  # user gets a unicorn (add $4 to balance)
  if 1 <= chosen_num <=5:
    chosen = "unicorn"
    prize_decoration = "!"
    balance += 4
  
  #if the random # is between 6 and 36
  # user gets a donkeu (subract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    prize_decoration = "D"
    balance -=1
  
  #the token is either a hose or zebra...
  #in both cases, ubtract $0.50 from the balance
  else:
    #if the number is even,set the chosen
    #item to horse
    if chosen_num % 2 == 0:
      chosen= "horse"
      prize_decoration = "~-"

      #otherwise set it to a zebra
    else:
      chosen = "zebra"
      prize_decoration =">>"
    balance -= 0.5
  
  outcome = "you got a {}. Your balance is" \ "${:.2f}".format(chosen, balance)

  statment_generator(outcome, prize_decoration)
    
  if balance <1:
    play_again = "xxx"
    print("sorry you have run out of money")
  else:
    play_again = input("press enter to play again" "or 'xxx' to quit")
  
  
print()
print("final_balance", balance)
     