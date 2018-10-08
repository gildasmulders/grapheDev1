"""
    Students template for the first homework of LINMA1691 "Théorie des graphes".

    Authors : Philippe Matthew, Devillez Henri
"""

import itertools
import csv

def check_mapping(A, B, h):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        - h an array describing an isomorphism mapping node i from A to node h[i] from B  
    Return True if h(A) = B, False otherwise
    """
    for E1 in range(len(A)):
            for I1 in range(len(A)):
                    if A[E1][I1] != B[h[E1]][h[I1]]:
                        return False
                        
    return True

def are_iso(A,B):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        
    Return (Ans, h) with :
        - Ans = True if A and B are isomorphs, False otherwise
        - h an array describing an isomorphim such that h(A) = B
    """

    n = len(A)    
    h = list(range(n))
    for E1 in list(itertools.permutations(h,n)):
        flag = check_mapping(A, B, list(E1))
        if flag:
            return flag, list(E1)          
    return flag, []


def color_ones(A):
    """
    Input :
        - A an adjacency matrix (array of arrays)
        
    Return an array of same dimension as A containing only ones
    """
    
    n = len(A)
    T = [1]*n        
    
    return T

def color_degree(A):
    """
    Input :
        - A an adjacency matrix (array of arrays)
    
    Return an array containing the degrees of the nodes of A
    """
    n = len(A)
    D = [0]*n
    for i in range(n):
        sum = 0
        for j in A[i]:
            sum += j            
        D[i] = sum       
   
    return D

def color_k_neigh(A, k):
    """
    Input :
        - A an adjacency matrix (array of arrays)
        - k the size of the neighbourhood of the coloring scheme 
    
    Return an array containing the colors as defined in Q4 of the project statement
    The colors have to be structured as a sorted tuple of pairs (k, deg(v)) 
    """
    
    def matr_product(A, B):
    
        n = len(A)
        
        C = [0]*n
        for l in range(n):
            C[l] = [0] * n
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k]*B[k][j]        
        return C
    n = len(A)
    toRet = [0]*n
    NodeSeenAlready = [0] * n
    D = color_degree(A)
    for o in range(n):
        NodeSeenAlready[o] = [o]
        toRet[o] = [(0, D[o])]        
        
    for i in range(k): 
        if i == 0:
            for j in range(n):
                for m in range(n):
                    if A[j][m] > 0:
                        if m not in NodeSeenAlready[j]:
                            NodeSeenAlready[j].append(m)
                        toRet[j].append((i+1, D[m]))
                    elif m in NodeSeenAlready[j]:
                        toRet[j].append((i+1, D[m]))
        else:
            C = matr_product(A, A)
            for j in range(n):
                for m in range(n):
                    if C[j][m] > 0:
                        if m not in NodeSeenAlready[j]:
                            NodeSeenAlready[j].append(m)
                        toRet[j].append((i+1, D[m]))
                    elif m in NodeSeenAlready[j]:
                        toRet[j].append((i+1, D[m]))
            A = C
    for l in range(n):
        toRet[l] = tuple(sorted(toRet[l]))
     
    return toRet

def are_iso_with_colors(A, B, color = color_ones):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        - color a coloring function
    Return (Ans, h) using the coloring heuristic with :
        - Ans = True if A and B are isomorphic, False otherwise
        - h describe an isomorphim such that h(A) = B if Ans = True, h = [] otherwise
    
    """
    n = len(A)
    colorsA = color(A)
    colorsB = color(B)
    h = [-1]*n
    
    sameColor = []
        
    for E2 in range(n):
        for E3 in range(n):
            if(colorsA[E2] == colorsB[E3]) :
                sameColor.append(tuple([E2, E3]))
    
    
    def iso_with_colors( h):
        
        n = len(A)
        
        if -1 not in h :
            
            if check_mapping(A, B, h) == True :
                return True, h

        
        for E4 in sameColor:
            if (h[E4[0]] == -1) and (E4[1] not in h):
                h[E4[0]] = E4[1]
                result, temp = iso_with_colors(h)
                if result == True:
                    
                    return True, temp
                else:
                    h[E4[0]] = -1
                    
        return False, []

    iso, hfinal = iso_with_colors(h)
        
    return iso, hfinal

if __name__ == "__main__":

    # Read Input
    
    with open('in1.csv', 'r') as fd:
        lines = list(csv.reader(fd, delimiter=','))
        n = int(len(lines)/2)

        A = []
        B = []

        for i in range(n):
            A.append([int(x) for x in lines[i]])
        
        for j in range(n, 2*n):
            B.append([int(x) for x in lines[j]])  
            
    # Compute answer
    #are_iso, h = are_iso(A, B)
    are_iso, h = are_iso_with_colors(A, B, color_ones)
    #are_iso, h = are_iso_with_colors(A, B, color_degree)
    #are_iso, h = are_iso_with_colors(A, B, lambda x : color_k_neigh(x, 2))
     
    # Check results

    with open('out1.csv', 'r') as fd:
        lines = csv.reader(fd, delimiter=',')
        true_answer = int(next(lines)[0])
        
        if are_iso != true_answer:
            if true_answer:
                print("Wrong answer: A and B are isomorphic")
            else:
                print("Wrong answer: A and B are not isomorphic")
        else:
            if are_iso:
                if check_mapping(A, B, h):
                    print("Correct answer")
                else:
                    print("Wrong answer: incorrect mapping")
                
            

        


