

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
    print("give me your money")
    print()
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


# Main Routine goes here...
played_before = yes_no("have you played the game before? ")

if played_before == "no":
    instructions()
print ("Program continues")
# ask user how much they want to play with...
how_much =num_check("how much would you like to pay with? ", 0, 10)
print ("you will be spending ${}".format(how_much))
