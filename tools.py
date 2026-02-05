import numpy as np
import random as rd

def median(points):
    #print("correct = ", np.median(points.T[0]))
    n = len(points)
    m = n//2 + 1   #middle index (la médiane est le m ième element)
    return(find(points,m,-1,1))



def find(points, k, a, b):
    '''
    finds the kth leftmost point from the list points where x is in [a,b] """
    '''
    pivot = a+(b-a)*(k/len(points))

    nb_point_left = 0     #nombre de points à gaughe du pivot
    closest_left = [a-1,0]    #point à gauche du pivot le plus près 
    closest_right = [b+1,0]     #points à droite le plus près du pivot
    left_points = []            #listes des points à gauche du pivot
    right_points = []           #liste des points à droite du pivot

    for point in points :
        if point[0]<pivot :
            nb_point_left += 1
            left_points.append(point)
            if point[0] > closest_left[0] :
                closest_left = point
        
        else :
            right_points.append(point)
            if point[0] < closest_right[0] :
                closest_right = point

    print(nb_point_left)

    if nb_point_left == k :
        return (closest_left)
    elif nb_point_left>k :
        return (find(left_points, k, a, closest_left[0]))
    else :
        return(find(right_points,k-nb_point_left,closest_right[0],b))

    
def line (p1,p2,p):
    '''
    return the value of the y value of the line defined by p1 and p2, calculated in the abscice of point p
    '''
    return p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*p[0]

def find_line(points,xm):
    ## random order
    rd.shuffle(points)
    
    ## finding the first basis
    k = 0
    while points[k][0] > xm :   ## rajouter des fail au cas où
        k+=1
    p1 = points[k]
    points.remove(p1)
    
    k = 0
    while points[k][0] < xm :
        k+=1
    p2 = points[k]
    points.remove(p2)

    left_points = [p1]
    right_points = [p2]
    
    ## update of the basis point by point
    for point in points :
    
        if point[0]<xm:
            if point[1] > line(p1,p2,point):
                p1 = point
                for p in right_points :
                    if p[1]>line(p1,p2,p):
                        p2 = p
            else : 
                left_points.append(point) 
        
        else : 
            if point[1] > line(p1,p2,point):
                p2 = point
                for p in left_points :
                    if p[1]>line(p1,p2,p):
                        p1 = p
            else : 
                right_points.append(point)
    
    return p1, p2















