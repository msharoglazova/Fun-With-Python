#!/usr/local/bin/python3
# FILE: CommandLineTExtDisplay.py
# DATE: 2-17-2019
# DESC: This program rewraps the text from a filename passed so that
#       it fits into an 80 column window without breaking any words.

""" Algorithm:
	The main purpose of this program is to open the file passed
	as a command line argument. However, in case user forgets
	to include an argument an option to enter the file name is provided.
	Generator will open the file and yield from it recursively.
	Formatting happens in the function call using textwrap fill()
	function.
	Several exception handlers (usin nested blocks) are provided:
	1. In case command line argument is missing
	2. Users enters the worng path
	3. Command line arugment path is wrong
    Note: if the filepath is given as a command line argument,
        command line syntax can be used. That is filename can
	include * or . or ~. If it is given through user input,
        it MUST be a full absolute path. In the future, regex
        may be used to handle that more flexibly. Also, a loop might be added
        to accomodate user keeping typing the wrong file path. At the moment
        the program will exit with no print, if the user types a wrong path twice.
        But for now, this suffices for the purposes of the assignment.
"""

import sys
import textwrap

def make_line():
    try:					# try open command line argument
        filename = str(sys.argv[1])
        file = open(filename)
    except IndexError:				# argument is missing
        filename = input("Enter file path: ")	# user input option
        try:
            file = open(filename)
        except (FileNotFoundError, IOError):	# wrong input
            print("Could not open file. Check that the path is correct!")
            filename = input("Try again: ")
            file = open(filename)
    except (FileNotFoundError, IOError):	# argument is wrong
        print("Could not open the file. Check that the path is correct!")
        file = input("Try again: ")
        file = open(filename)
    finally:					
        yield from file


line = make_line()
try:
    while True:
        print(textwrap.fill(next(line), width=80,
           break_long_words=False), end = '\n')
except StopIteration:
    pass
finally:
    exit()

print()




