def pt1():
    depth, horizontal = 0, 0 #y, x

    with open("day2_input.txt", "r") as f:
        data = [i for i in f.read().strip().split("\n")] #parse input
        
        for line in data:
            if "forward" in line:
                horizontal += int(line.split(" ")[1]) #get value by splitting
            elif "up" in line:
                depth += int(line.split(" ")[1])
            elif "down" in line:
                depth -= int(line.split(" ")[1]) 
    
    return (abs(depth * horizontal))

def pt2():
    depth, horizontal = 0, 0 #y, x
    aim = 0

    with open("day2_input.txt", "r") as f:
        data = [i for i in f.read().strip().split("\n")] #parse input
        
        for line in data:
            if "forward" in line:
                forward = int(line.split(" ")[1])
                horizontal += forward
                depth += aim * forward
            elif "up" in line:
                aim -= int(line.split(" ")[1])
            elif "down" in line:
                aim += int(line.split(" ")[1]) 
    
    return (abs(depth * horizontal))


print(f'P1: {pt1()}')  
print(f'P2: {pt2()}')  
    
