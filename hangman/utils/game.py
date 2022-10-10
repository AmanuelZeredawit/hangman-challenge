class Hangman:
    import random
    from sys import exit
    """
    Hangman class reperesent a game.
    """
    possible_word = ['becode', 'learning', 'mathematics', 'sessions']
    word_to_find = list(random.choice(possible_word))
    well_guessed_letter = list('_')*len(word_to_find)
    
    def __init__(self):
        """
        Constructs all the necessary attributes for the Hangman object.
        """
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0
        self.word_to_find = Hangman.word_to_find
        self.well_guessed_letter = Hangman.well_guessed_letter
        self.bad_guessed_letter = ""
        print(self.well_guessed_letter)


    def play(self):
        """
        Function to play the game.
        :return: lives number of wrong trails left.
        """
 
        letter = input("enter an alphabetic letter: ")
        # check if it is single letter alphabet
        if len(letter) == 1 and letter.isalpha():
            letter = letter.lower()
            self.turn_count += 1
            
            # check if letter is in word_to_find and not already guessed
            if (letter in self.word_to_find) and (letter not in self.well_guessed_letter):

                # loop over the word_to_find to get the index of the letter and update well_guessed_letter
                for iter in range(len(self.word_to_find)):
                    if self.word_to_find[iter] == letter:
                        self.well_guessed_letter[iter] = letter
                
                    
            else:
                # if letter not in word_to_find decreament self lives, increament error_count and update bad_guessed_word
                self.bad_guessed_letter = self.bad_guessed_letter + letter
                self.error_count += 1
                self.lives = self.lives - 1
                

        else:
            # warn player, increament error_count, update bad_guessd_letter and decrement and return lives 
            print("warning: please enter alphabets")
            self.error_count += 1
            self.bad_guessed_letter = self.bad_guessed_letter + letter
            return self.lives - 1
            
        
        return self.lives


    def game_over(self):
        """
        :print: game over.
        """
        print("game over")
        exit()
        
        

    def well_played(self):
        """
        :return: a string that states wining of the game.
        """
        return f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!"
        
    
    def start_game(self):
        """
        starts the game.
        """
        while True:
            # check if number of lives is not finished            
            if self.lives == 0:
                self.game_over()
            self.lives = self.play()

            #check if guess is succes
            if self.well_guessed_letter == self.word_to_find:
                print(self.well_played())
                self.game_over()

            # display the states of the variables of the game  
            print("well_guessed_letters: ",str(self.well_guessed_letter)+
              " bad_guessed_letters: ",self.bad_guessed_letter +
              " error_count: ", str(self.error_count)+
              " turn_count:", str(self.turn_count))
        
    
    



              
