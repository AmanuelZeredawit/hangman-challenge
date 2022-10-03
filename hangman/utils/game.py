class Hangman:
    import random
    import re
    from sys import exit
   
    
    
    
    possible_word = ['becode', 'learning', 'mathematics', 'sessions']
    word_to_find = list(random.choice(possible_word))
    well_guessed_letter = list('_')*len(word_to_find)
    
    def __init__(self):
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0
        self.word_to_find = Hangman.word_to_find
        self.well_guessed_letter = Hangman.well_guessed_letter
        self.bad_guessed_letter = ""
        print(self.word_to_find)


    

    def play(self):

        letter = input("enter an alphabetic letter: ")
        
        if len(letter) == 1 and letter.isalpha():
            letter = letter.lower()
            self.turn_count += 1
            print(self.turn_count)
            for iter in range(len(self.word_to_find)):
                if self.word_to_find[iter] == letter:
                    self.well_guessed_letter[iter] = letter
                    print(self.well_guessed_letter)
                    
                else:
                    self.bad_guessed_letter = self.bad_guessed_letter + letter
                    self.error_count += 1
                    self.lives = self.lives - 1

       


            
        else:
            print("please enter correct letter")
            return self.lives - 1
        
        return self.lives


    def game_over(self):
        print("game over")
        self.sys.exit()
        
        

    def well_played(self):
        return f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count_here} errors!"
        
    
    def start_game(self):
        
        print(self.lives)
        while(self.lives > 0):
            self.lives = self.play()
            if self.well_guessed_letter == self.word_to_find:
                print(self.well_played())
                self.game_over()
        if self.lives == 0:
            self.game_over()

        print("well_guessed_letters: ",str(self.well_guessed_letter)+
        "bad_guessed_letter: ",self.bad_guessed_letter +
        "error_count:", str(self.error_count) +
        "turn_count:", str(self.turn_count))
        
    
    



              
