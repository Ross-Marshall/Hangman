#!/usr/bin/python
import getpass
import sys
import Tkinter
#import tkMessageBox
#import Image
#sys.path.append('/me/code/python/hangman/Imaging-1.1.7/PIL')
#import ImageTk


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch] 

def letters_so_far(guess_list, hangman_word):
    print_index = []
    for item in guess_list:
        for index in item:
            print_index.append(index)

    print_index.sort()
    print 'Sorted index... ' + str( print_index )
    
    print_string = ''
    for i in range( len(hangman_word ) ):
        if i in print_index:
            print_string = print_string + hangman_word[i]
        else:
            print_string = print_string + '_'
    print print_string
    if print_string == hangman_word:
       print 'You WIN!!! The word was ' + hangman_word
       sys.exit(0)

#top = Tkinter.Tk()

#imageFile = "img1.png"
#f = Image.open(imageFile).show()
hangman = ['head','left_eye','right_eye','nose','mouth','body','left_arm','right_arm','left_leg','right_leg']

hangman_word = getpass.getpass('Enter your hangman word: ').upper()

#print hangman_word

right_guess = []
wrong_guess = []

body_index = 0

keep_guessing = True

while body_index < len( hangman ):
    print 'body_index = ' + str( body_index )
    a_letter = raw_input("Please enter a letter: ").upper()
    if len( a_letter ) != 1:
       print 'Please type one character at a time...\n'

    if a_letter in wrong_guess:
       print 'You already guessed ' + a_letter 
       continue

    if a_letter in hangman_word:
        print 'CORRECT : ' + a_letter + ' is in the word' 
        right_guess.append( find( hangman_word, a_letter ) ) 
        print 'find() returns==> ' + str( right_guess )
        letters_so_far( right_guess, hangman_word )

    if a_letter not in hangman_word:
        print 'WRONG : add ' + a_letter + ' to wrong list'
        wrong_guess.append( a_letter )
        print 'Draw ' + str( hangman[ body_index ] )
        if body_index > len( hangman ):
            print 'You lose...'
            keep_guessing = False
        body_index += 1
        print 'Wrong guesses ' + str( wrong_guess )

    print 'You typed ' + str( a_letter )

    if body_index >= len(hangman):
        print 'YOU LOSE!!! The word was ' + hangman_word
