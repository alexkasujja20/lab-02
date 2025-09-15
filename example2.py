with open('sample.txt', 'r') as f:
    for line in f:
        print(line.strip())

#modifying this code
with open('sample.txt', 'r') as f:
    for i, line in enumerate(f, start=1): #to start numbering from 1
        print(f"{i}: {line.strip()}")