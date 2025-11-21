#!/usr/bin/env python
"""reducer.py"""
 
from itertools import groupby
from operator import itemgetter
import sys

# Define a list to store all results from the single reducer
all_results = []
 
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)
 
def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    
    # First, perform the standard word count aggregation
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            # Store the aggregated result
            all_results.append((total_count, current_word))
        except ValueError:
            pass
            
    # After all aggregation, sort the results by count (the first item in the tuple) 
    # The key=lambda x: x[0] sorts by the count. The reverse=True ensures descending order.
    # Note: Since -numReduceTasks 1 is used, all results are in this list.
    all_results.sort(key=lambda x: x[0], reverse=True)
    
    # Print only the first 3 results
    for i in range(min(3, len(all_results))):
        count, word = all_results[i]
        print ("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
