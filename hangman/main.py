from utils.game import Hangman

def main ():
    """
    Function to create an object of a class Hangman
    """
    print("game is starting:")
    player1 = Hangman()
    player1.start_game()
    
  
if __name__ == '__main__':
    main()