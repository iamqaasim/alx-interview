import sys
import signal

# Define a signal handler for CTRL + C
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Initialize variables to store statistics
total_file_size = 0
status_code_count = {}

# Function to print the statistics
def print_statistics():
    print("File size:", total_file_size)
    for status_code in sorted(status_code_count):
        print(status_code, ":", status_code_count[status_code])

# Loop through stdin line by line
line_count = 0
for line in sys.stdin:
    line_count += 1
    # Split the line into fields using whitespace as delimiter
    fields = line.split()
    if len(fields) != 7:
        # Skip lines that do not have the expected format
        continue
    ip_address, _, _, request, status_code, file_size, _ = fields
    if request != "GET /projects/260 HTTP/1.1":
        # Skip lines that do not have the expected request
        continue
    try:
        # Parse the status code and file size as integers
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        # Skip lines with non-integer status code or file size
        continue
    # Update the total file size
    total_file_size += file_size
    # Update the status code count
    status_code_count[status_code] = status_code_count.get(status_code, 0) + 1
    # Print the statistics after every 10 lines
    if line_count % 10 == 0:
        print_statistics()
# Print the final statistics
print_statistics()
