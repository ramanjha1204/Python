# Open the file in read mode
with open('file1.txt', 'r') as file:
    # Read a line from the file
    line = file.readline().strip()  # strip() removes leading and trailing whitespaces
    
    # Split the line into words using space as the delimiter
    words = line.split(' ')
    
    # Print the words
    for word in words:
        print(word)
