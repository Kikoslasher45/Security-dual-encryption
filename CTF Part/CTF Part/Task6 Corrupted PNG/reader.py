# read hello.hello file and display its content
import os
import sys
import time

def main():
    # get the current working directory
    cwd = os.getcwd()
    print("Current working directory: ", cwd)
    # get the path of the hello.hello file
    hello_path = os.path.join(cwd, "", "danger.png")
    print("hello.hello path: ", hello_path)
    # read the hello.hello file
    with open(hello_path, "r") as hello_file:
        print("hello.hello content: ", hello_file.read())
   
if __name__ == "__main__":
    main()