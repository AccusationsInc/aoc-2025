#Set file path
filename = "input.txt"


#Read input into an array
with open(filename) as file:
    lines = [line.rstrip() for line in file]

#set count to 0
password = 0

#Set current dial position
currentPos = 50

#Iterate through each line
for rotation in lines :

    print(f"Starting Position :: {currentPos}")
    print("Rotation :: " + rotation)
    #Direction to turn dial
    direction = rotation[0]

    #Clicks to turn dial
    clicks = int(rotation[1:])
    
    if(direction == "L") :
        clicks *= -1
    
    currentPos += clicks


    currentPos = (100 + currentPos) % 100

    if(currentPos == 0) :
        print("Ping!")
        password += 1
    
    print(f"Ending Position :: {currentPos}\n\n")

print(f"Password :: {password}")