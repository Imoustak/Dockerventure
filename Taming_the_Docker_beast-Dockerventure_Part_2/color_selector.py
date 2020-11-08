#!/usr/bin/python

import os

"""Script that prints out the selected color."""

# The color to be used read from the environtment variable color
#color = os.environ['color']
color = "blue"

def main():
 
    print("The color picked is: {}!".format(color))

if __name__ == '__main__':
    main()