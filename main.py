import random

def loadstats():
    global wins
    global losses
    with open("wins.txt") as f:
        wins = int(f.read())
    with open("losses.txt") as f:
        losses = int(f.read())

def viewstats():
    global wins
    global losses
    with open("wins.txt") as f:
        wins = int(f.read())
    with open("losses.txt") as f:
        losses = int(f.read())
    print("=============")
    print(f"Your stats:\nWins   = {wins}\nLosses = {losses}")
    print("=============")
    return

def main():
    while True:
        print("==============================")
        print("=- Rock, Paper and Scissors -=")
        print("==============================")
        print("1. Play\n2. View Stats\n3. Exit")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Please enter a number.")
            return
        match choice:
            case 1:
                print("=- Let's Play Rock, Paper and Scissors -=")
                play()
            case 2:
                viewstats()
            case 3:
                print("Quitting game...")
                exit()
            case _:
                print("Invalid input. Please try again.")
                continue

def play():
    global wins
    global losses
    while True:
        l = ["Rock", "Paper", "Scissors"]
        computer = random.choice(l)
        print("Choose your hand from the following: ")
        print("===========\n1. Rock\n2. Paper\n3. Scissors\n===========\n4. Back\n===========")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Please enter a number.")
            continue
        match choice:
            case 1:
                user = "Rock"
            case 2:
                user = "Paper"
            case 3:
                user = "Scissors"
            case 4:
                return
            case _:
                print("Invalid input.")
                continue
        #draw
        if user == computer:
            print("==============")
            print("Its a draw!")
            print("==============")
            print("1. Play Again.\n2. Back to main menu.")
            try:
                choice = int(input("Enter: "))
            except ValueError:
                print("Please enter a number.")
            match choice:
                case 1:
                    continue
                case 2:
                    return
                case _:
                    print("Invalid input. Please try again.")
                    
        #win
        elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
            wins += 1
            with open("wins.txt", "w") as f:
                f.write(str(wins))
            loadstats()
            print("==========================================")
            print(f"=- You Win! with total wins now {wins} -=")
            print("==========================================")
            print("1. Play Again.\n2. Back to main menu.")
            try:
                choice = int(input("Enter: "))
            except ValueError:
                print("Please enter a number.")
            match choice:
                case 1:
                    continue
                case 2:
                    return
                case _:
                    print("Invalid input. Please try again.")
        #loss
        else:
            losses += 1
            with open("losses.txt", "w") as f:
                f.write(str(losses))
            loadstats()
            print("==========================================")
            print(f"=- You lost, with total losses now {losses} -=")
            print("==========================================")
            print("1. Play Again.\n2. Back to main menu.")
            try:
                choice = int(input("Enter: "))
            except ValueError:
                print("Please enter a number.")
            match choice:
                case 1:
                    continue
                case 2:
                    return
                case _:
                    print("Invalid input. Please try again.")

loadstats()
main()