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
    n = len(maze)
    m = len(maze[0])
    def find_E(maze):
        for i in range(n):
            for j in range(m) :
                if maze[i][j] == 'E':
                  return (i,j)
        return -1       
              
    coordE = find_E(maze)
    if(coordE == -1):
        return -1
            
    visited = [-1]*n*m
    nodesToVisit = Q.Queue()
    nodesToVisit.put(coordE)
    visited[coordE[0]*m +coordE[1]] = 0

    while (not nodesToVisit.empty()):

      current = nodesToVisit.get()
      x = current[0]
      y = current[1]
      
      for i in [-1, 1]:
        
        if((maze[x+i][y]=='S')or (maze[x][y+i] == 'S')):
          return visited[x*m+y] +1
      
        if((maze[x+i][y] != '#') and (visited[(x+i)*m+y] == -1)) : 
            visited[(x+i)*m+y] = visited[x*m+y] +1 

            nodesToVisit.put((x+i,y))
          
        if((maze[x][y+i] != '#') and (visited[x*m+(y+i)] == -1)) : 
            visited[x*m+(y+i)] = visited[x*m+y] +1 

            nodesToVisit.put((x,y+i)) 

        



        

            

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
        
        Minh-Phuong Tran and Gildas Mulders, with the help of Gilles Peiffer
    """
    
    def Minh(Vector, start, length):
        index=-1
        valeur=999999
        for i in range(start, start + length):
            if(Vector[i]>-1):
                if(valeur>Vector[i]):
                    valeur=Vector[i]
                    index=i%length
        return index
    
    n = len(tasks)
    tab = [-1]* n*n
    modTab = [0]* n*n
    MeilleurChemin = [0] *n
    for E in paths:
        tab[(E[0]-1)*n+E[1]-1] = E[2] + tasks[E[1]-1]
        tab[(E[1]-1)*n+E[0]-1] = E[2] + tasks[E[0]-1]
    for i in range(n):
        modTab[i] = tab[i]  
    modTab[0] = -2
    
    current=Minh(modTab, 0, n)
    Time=modTab[current]
    MeilleurChemin[0]=0
    MeilleurChemin[current]=Time
    modTab[current]=-2
    
    for m in range(1,n):
        
        for o in range(n):
            
            if(modTab[(m-1) * n + o]==-2):
                modTab[m * n + o]=-2
            elif(modTab[(m-1) * n + o]==-1):
                if(tab[current * n + o]!=-1):
                    modTab[m * n + o]=Time + tab[current * n + o]
                else:
                    modTab[m * n + o]=-1
            else:
                if(tab[current * n + o]!=-1):
                    modTab[m * n + o]= min(Time + tab[current * n + o],modTab[(m-1) * n + o])
                else:
                    modTab[m * n + o]=modTab[(m-1) * n + o]
                    
        current=Minh(modTab, m*n, n)
        if(current==-1):
            break
        Time=modTab[m * n + current]
        MeilleurChemin[current ]=Time
        modTab[m * n + current]=-2
        if(current==n-1):
            break
        
    return MeilleurChemin[n-1]+tasks[0]
  


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
                 
            

        
