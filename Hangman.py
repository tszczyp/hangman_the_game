import random
from passwordList import passwords

# Player states during the gameplay.
player_states = ['''
    +---+
    |
    |
    |
    |
    ===''', '''
    +---+
    |   O
    |
    |
    |
    ===''', '''
    +---+
    |   O
    |   |
    |
    |
    ===''', '''
    +---+
    |   O
    |  /|
    |
    |
    ===''', '''
    +---+
    |   O
    |  /|\\
    |
    |
    ===''', '''
    +---+
    |   O
    |  /|\\
    |  /
    |
    ===''', '''
    +---+
    |   O
    |  /|\\
    |  / \\
    |
    ===''']


class Hangman:

    def show_player_state(self, mistakes):
        """ Displays a state of the player depending on the number of mistakes.
            @mistakes - Amount of incorrect responses player made during the gameplay.
        """
        print(player_states[mistakes])

    def welcome_message(self):
        """ Prints the welcome message."""

        print("Welcome to the Hangman game, easily one of the best games in the world. ;) To continue, please select your difficulty level. \n")
        h.choose_difficulty()

    def choose_difficulty(self):
        """ Allows to choose the difficulty level. """

        difficulty_choice = input("Type 1 to select easy, 2 to select normal and 3 to select hard: \n")

        if difficulty_choice == "1":
            self.game_mode = "easy"
            print(f"You have chosen an {self.game_mode} mode.")
            h.get_password_based_on_difficulty()
        elif difficulty_choice == "2":
            self.game_mode = "normal"
            print(f"You have chosen a {self.game_mode} mode.")
            h.get_password_based_on_difficulty()
        elif difficulty_choice == "3":
            self.game_mode = "hard"
            print(f"You have chosen a {self.game_mode} mode.")
            h.get_password_based_on_difficulty()
        else:
            print("Wrong input, try again.")
            h.choose_difficulty()

    def get_password_based_on_difficulty(self):
        """ Gets a random password depending on the chosen difficulty level."""

        if self.game_mode == "easy":
            easy_list = [x for x in passwords if 3 <= len(x) <= 5]
            self.password = random.choice(easy_list)
        elif self.game_mode == "normal":
            normal_list = [x for x in passwords if 6 <= len(x) <= 9]
            self.password = random.choice(normal_list)
        else:
            hard_list = [x for x in passwords if len(x) > 9]
            self.password = random.choice(hard_list)

    def show_board(self, mistakes_number, missed_letters, correct_letters):
        """ Shows the game board with the necessary information for the player.
            @mistakes_number - Amount of incorrect responses player made during the gameplay.
            @missed_letters - incorrect letters passed by the player.
            @correct_letters - correct letters passed by the player.
        """

        h.show_player_state(mistakes_number)

        print("Missed letters:", end=' ')
        for letter in missed_letters:
            print(letter, end=' ')
        print("\n")

        blanks = '_' * len(self.password)

        for i in range(len(self.password)):
            if self.password[i] in correct_letters:
                blanks = blanks[:i] + self.password[i] + blanks[i+1:]

        for letter in blanks:
            print(letter, end=' ')
        print("\n")

    def choose_player_action(self):
        """ Allows the player to make a choice in which way they want to answer."""

        choice = input(
            "Please choose your answering method:\n Press 1 to guess a single letter.\n Press 2 to guess an entire password. ")

        if choice == '1':
            h.make_a_guess()
        elif choice == '2':
            h.guess_entire_password()
        else:
            print("Incorrect choice, please type again")
            h.choose_player_action()

    def make_a_guess(self):
        """ Allows the player to guess a letter."""

        self.guess = input("Make a guess, remember, that capital letter do matter: ")

        if len(self.guess) != 1:
            print("Please enter a single letter.")
            h.make_a_guess()
        elif self.guess.isnumeric():
            print("Please enter a letter not a number.")
            h.make_a_guess()
        elif not self.guess.isalpha():
            print("Please enter an alphabetical letter.")
            h.make_a_guess()
        else:
            return self.guess

    def guess_entire_password(self):
        """ Allows the player to guess an entire password."""

        self.guess = input("Guess the password, remember, that capital letter do matter: ")

        if self.guess.isnumeric():
            print("Please enter the password not a number.")
            h.guess_entire_password()
        elif not self.guess.isalpha():
            print("Please enter the password by using alphabetical letters")
            h.guess_entire_password()
        else:
            return self.guess

    def play_again(self):
        """ Asks if the player wants to play again."""

        print("Do you want to start over? y/n")
        return input().lower().startswith('y')

    def lets_play(self):
        """ Controls the flow of the game."""

        correct_guesses = ""
        incorrect_guesses = ""
        misses = 0
        game_over = False

        h.welcome_message()

        while True:
            h.show_board(misses, incorrect_guesses, correct_guesses)

            h.choose_player_action()

            guess = self.guess

            if guess in self.password:
                correct_guesses = correct_guesses + guess
                all_letters_guessed = True
                for i in range(len(self.password)):
                    if self.password[i] not in correct_guesses:
                        all_letters_guessed = False
                        break
                if all_letters_guessed:
                    h.show_board(misses, incorrect_guesses, correct_guesses)
                    print("You have won :)")
                    game_over = True
            else:
                incorrect_guesses = incorrect_guesses + guess
                misses = misses + 1
                if misses == len(player_states) -1:
                    h.show_board(misses, incorrect_guesses, correct_guesses)
                    print("You have lost")
                    game_over = True

            if game_over:
                if h.play_again():
                    game_over = False
                    h.lets_play()
                else:
                    break


if __name__ == "__main__":
    h = Hangman()

    h.lets_play()