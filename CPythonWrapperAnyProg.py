#!/usr/local/bin/python3

"""FILE: CPythonWrapperAnyProg.py
    DATE: 04-22-2019
    DESC: Write a universal wrapper program that expects its command line arguments
        to contain the absolute path to any program, followed by its arguments. 
        The wrapper should run that program and report its exit value.
   NOTE: This wraper program will take valiable amount of command line arguments which MUST be
        full paths to files and execute depending on the commands.
        Wrapped in the try and catch block to prevent error when no command line arguments are passed.
        If-else block attampts to address various types of programs such as simple c++ and java
        to exemplify how it would work with differnent types of programs. Because these types of
        program include a compilation step, special cases had to be created.
        Sample runs with c++ were done on hills and worked with single file programs.
        Sample runs with java were done locally because hills doesn't have JVM, and also work with
        single file programs. 
        In the future I might work more on this to compile multiple file programs.
"""
 
import sys
import subprocess

try:
    argument = [str(a) for a in sys.argv]	# create a list of command line arguments
    del argument[0]		#delete this program's name from list of arguments aka execution

    if argument[0] == "g++" or argument[0] == "gcc":		# in case it is c++ code
        subprocess.call(["g++", argument[1]]) 			# compile using g++ compiler
        process = subprocess.call("./a.out")			# run as c++ 

    elif argument[0] == "javac":				# in case of java code
        subprocess.call(["javac", argument[1]])			# compile using javac compiler
        temp = argument[1].rsplit('/', 1)			#slice the argument to retrieve filename
        classpath = temp[0]					# tell JVM where executable class is
        process = subprocess.call(["java", "-cp", classpath, temp[1].strip('.java')])	  # run as java

    else:
        process = subprocess.call(argument)			# runs as is

    print("Exit status: ", process)				# print the exit value

except IndexError:
    print("Some arguments might be missing")			# handle the exception if thrown



