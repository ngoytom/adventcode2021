def pt1():
    count = 0 

    with open("day1_input.txt", "r") as f:
        data = [int(i) for i in f.read().strip().split("\n")] #parse input

    #checking if larger than previous
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1

    return count

def pt2():
    l, r = 0, 2
    count = 0 
    previous = 0

    with open("day1_input.txt", "r") as f:
        data = [int(i) for i in f.read().strip().split("\n")]
        previous = data[0] + data[1] + data[2]
        
        #check window value and compare
        while r != len(data) - 1: 
            update = previous - data[l] + data[r + 1]
            if update > previous:
                count += 1 
            previous = update
            l += 1
            r += 1

    return count

print(f'P1: {pt1()}')
print(f'P1: {pt2()}')

