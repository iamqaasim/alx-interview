#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys

# Create a dictionary to keep track of HTTP status codes and their occurrence count
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize total size and counter
total_size = 0
counter = 0

try:
    # Read input from standard input (stdin) line by line
    for line in sys.stdin:
        # Split the line into a list of strings separated by a space character
        line_list = line.split(" ")
        
        # Check if the list has more than 4 elements (minimum required to extract code and size)
        if len(line_list) > 4:
            # Extract the HTTP status code (second last element) and convert it to a string
            code = line_list[-2]
            # Extract the size of the response (last element) and convert it to an integer
            size = int(line_list[-1])
            
            # Check if the status code is in the cache dictionary
            if code in cache.keys():
                # If yes, increment its count by 1
                cache[code] += 1
            
            # Add the response size to the total size
            total_size += size
            
            # Increment the counter by 1
            counter += 1
            
        # If the counter reaches 10
        if counter == 10:
            # Reset the counter to 0
            counter = 0
            
            # Print the total file size
            print('File size: {}'.format(total_size))
            
            # Sort the cache dictionary by key and iterate over it
            for key, value in sorted(cache.items()):
                # If the count for the current status code is not zero
                if value != 0:
                    # Print the status code and its count
                    print('{}: {}'.format(key, value))

# If any exception occurs during execution, catch it and ignore it
except Exception as err:
    pass

# Finally, when the program execution is complete, print the total file size and the cache
finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

