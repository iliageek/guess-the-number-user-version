import random

# Start Game
def start():

    # Get Numbers
    pc_num = random.randint(1, 100)
    user_num = int(input("\nEnter Your Guess:\n"))

    # Guess The Number
    while pc_num != user_num:
        
        if pc_num > user_num:
            print("\nYour Number is Smaller Than PC Number!\nTry Again...")
            user_num = int(input("\nEnter Your Guess Again:\n"))
            
        elif pc_num < user_num:
            print("\nYour Number is Larger Than PC Number! \n Try Again...")
            user_num = int(input("\nEnter Your Guess Again:\n"))
            
        else:
            break
        
    print("\n It's True!\nGoodjob\nYou Win!\n")
    
    def play_again():
        
        # Play Again
        play_again = input("Do You Want To Play Again [Y/N]:").capitalize().strip()
        
        if play_again == "Y":
            print("Good! You Can :D")
            start()
        
        elif play_again == "N":
            print("\nOK... Goodbye!\n")
            exit()
        
        else:
            print("\nI Didn't Undrestand Waht You Said!\n")
            exit()
            
            
    play_again()

start()
