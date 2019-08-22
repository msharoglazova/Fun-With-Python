#!/usr/local/bin/python3

"""FILE: EncodingChecker.py
    DATE: 05-17-2019
    DESC: Write a program that creates a pool of workers to all at once
check whether or not the files whose pathnames are passed in are encoded in UTF-8.
NOTE: If any file is not in the current directory, a FULL PATH to the file MUST be passed.
"""

import concurrent.futures
import sys, codecs

argument = [str(a) for a in sys.argv]	# create a list of command line arguments
del argument[0]             #delete this program's name from list of arguments aka execution

def check_encoding(file):
    #print("checking file", file)
    try:
        f = codecs.open(file, encoding='utf-8', errors='strict')
        for line in f:		
            pass
        print("File", file, "- valid utf-8")
        return True
    except UnicodeDecodeError:			# if file is not valid utf-8, and error will be raised
        print("File", file, "- invalid utf-8")
        return False

"""ThreadPoolExecutor will create a pool of workers with the number of workers equal to the number
of files on the list. Each file will be processed in its own thread.
Since there are no variables that can be changed by the function, there's no concern
of any possible data race conditions.
"""

with concurrent.futures.ThreadPoolExecutor(max_workers=len(argument)) as executor:
    for a in argument:
        executor.submit(check_encoding, a)
