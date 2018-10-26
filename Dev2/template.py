"""
    Students template for the second homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""


import queue as Q
from collections import deque

# You cannot import other modules
# You do not have to use all imported modules


def shortest_path_1(maze):
    """ 
    INPUT : 
        - maze, a 2D array representing the maze    
    OUTPUT :
        - return the minimal number of steps required to go to the exit of the maze.
        
        See project statement for more details
    """
    for i in range(len(maze)):
        for j in range(len(maze[0])) :
            if maze[i][j] == 'E':
              coordE = (i,j, 0)
                
    visited = []
    nodesToVisit = Q.Queue()
    nodesToVisit.put(coordE)

    foundS = 0
    while (not nodesToVisit.empty() and not foundS):

      current = nodesToVisit.get()
      x = current[0]
      y = current[1]
      d = current[2] + 1
      
      for i in range(-1, 2,2):
        
        if((maze[x+i][y] != '#') and ((x+i, y) not in visited)) : 
          nodesToVisit.put((x+i,y,d))
          
        if((maze[x][y+i] != '#') and ((x, y+i) not in visited)) : 
          nodesToVisit.put((x,y+i,d)) 

        if((maze[x+i][y]=='S')or (maze[x][y+i] == 'S')):
          return d

      visited.append((x,y))


        

            

    return -1

def shortest_path_2(tasks, paths):
    """ 
    INPUT : 
        - tasks, the time to achieve each task (in minutes)
        - paths, list of tuples (a, b, t) giving a trail between tasks a and b.
          You need t minutes to walk this trail.
    OUTPUT :
        - return the time you need to finish the game
          
        See project statement for more details
    """

    return -1


if __name__ == "__main__":

    # Read Input for the first exercice
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.split(' ')
        
        n = int(l[0])
        m = int(l[1])
        
        maze = []
        for row in range(n):
            l = fd.readline().rstrip()
            maze.append(list(l))

    
            
    # Compute answer for the first exercice
     
    ans1 = shortest_path_1(maze)
     
    # Check results for the first exercice

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %" % (ans1, expected_output)) 
        
    # Read Input for the second exercice
    
    with open('in2.txt', 'r') as fd:
        l = fd.readline().split(' ')
        
        n = int(l[0])
        m = int(l[1])
        
        tasks = [int(x) for x in fd.readline().rstrip().split(' ')]
        
        paths = []
        for p in range(n):
            l = fd.readline().rstrip().split(' ')
            paths.append(tuple([int(x) for x in l]))
            
    # Compute answer for the second exercice
     
    ans2 = shortest_path_2(tasks, paths)
     
    # Check results for the second exercice

    with open('out2.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans2:
            print("Exercice 2 : Correct")
        else:
            print("Exercice 2 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans2, expected_output)) 
                 
            

        
