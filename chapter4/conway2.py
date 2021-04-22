
#conway's game of life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of lists for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #add a living cell
        else:
            column.append(' ') #add a dead cell
    nextCells.append(column) #nextCells is a list of column lists.
    
while True: #Main program loop
    print('\n\n\n\n\n') #Seperate each step with newlines
    currentCells = copy.deepcopy(nextCells)
        
    #Print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '')#print the # or space
        print() #print a newline at the end of the current row
        
    #calculate the next steps cells based on current steps cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get in neighboring coordinates
            # % WIDTH ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT
            
            #Count number of living neightbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1# Top left is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 #top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # left Neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors+= 1 #Bottom left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 #Bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1#bottom right neighbor is alive
                
            #set cell based on conways game of life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #Living cells with 2 or 3 neighbors to stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #Dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                #everything else stays or dies
                nextCells[x][y] = ' '
    time.sleep(1) #Add a 1-second pause to reduce flickering