slogan = input()

# read the starting position and the step size (integers)

position = int(input())

step = int(input())

# find and output the hidden message
nest = [slogan[(position + i * step) % len(slogan)] for i in range(len(slogan))]


print(nest)





