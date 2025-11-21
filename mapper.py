#!/usr/bin/env python
"""mapper.py"""

import sys

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # tab-delimited; the trivial word count is 1
        for word in words:
            # 1. Treat upper and lower case words the same (case-insensitive)
            # The .lower() method converts the word to all lowercase.
            processed_word = word.lower() # 
            
            # 2. Strip trailing commas and dots at the end of the words
            # The .rstrip() method removes specified trailing characters.
            processed_word = processed_word.rstrip(',.') # 
            
            # Ensure the word is not empty after stripping (e.g., if input was just ".,")
            if processed_word:
                print ('%s%s%d' % (processed_word, separator, 1))

if __name__ == "__main__":
    main()
