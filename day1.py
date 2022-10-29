def pt1():
    count = 0 
    with open("day1_input.txt", "r") as f:
        data = [int(i) for i in f.read().strip().split("\n")] #parse input
 
    #checking if larger than previous
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1

    return count

print(f'P1: {pt1()}')

