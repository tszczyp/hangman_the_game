# The Hangman

## Overview
Guess letters to fill in the blanks before your little man gets hung out to dry.

## Number of players
One player required.

## Game play
The system chooses one phrase from its database; the player must try to guess what it is one letter at a time or guess an entire phrase at once.
If a player suggests a letter that occurs in the word, the system fills in the blanks with that letter in the right places.
If the word does not contain the suggested letter, the system draws one element of a hangman's gallows.
As the game progresses, a segment of the gallows and of a victim is added for every suggested letter not in the word.
The game ends when either the phrase is guessed correctly or the player runs out of incorrect guesses.
The player can choose if they want to play again.

## Objective
Guess the word/phrase before your man gets hung!

## The system and difficulty
There are 3 difficulty levels which can be chosen by the player:
- Easy - up to 5 letters in a single phrase, minimum 3
- Normal - from 6 to 9 letters in phrase
- Hard - 10 letters and above

Ironically the Hard difficulty may be the easiest one considering more letters in each word to guess.

The player may choose to guess an entire phrase at once, if incorrect, it will be treated as a single mistake.
Note, that incorrectly guessed phrase will be shown as a single letter in list of mistakes, although its singular letters may or may not be a part of password themselves.
This means, that even though player guessed the phrase incorrectly, they may use its letters again and they might work.

## The size matters
Some words require a capital letters to use, such as "American", it was left on purpose to make the game a little harder.
Only the first letters may be capital.

