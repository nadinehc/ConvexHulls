import numpy as np
import random as rd


def median(points: list):
    '''
    Finds the point with the mediane x-coodinate
    
    Args: 
        points(list): set of points in the 2D plane

    Returns: 
        (list): median point
    '''
    n = len(points)
    m = n//2 + 1 
    return(find(points,m,0,1))


def find(points: list, k: int, a: float, b: float):
    '''
    Finds the kth leftmost point from the list 'points', whose x-coordinate is in [a,b]

    Args: 
        points (list): set of points in the 2D plane
        k (int)
        a (float): lower limit of the x coodinate
        b (float): upper limit of the x coordinate

    Returns: 
        (list): kth leftmost point
    '''
    pivot = a+(b-a)*(k/len(points))   

    nb_point_left = 0           
    closest_left = [a-1,0]      
    closest_right = [b+1,0]     
    left_points = []            
    right_points = []           

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

    #cases where all points are on the same side of the pivot
    if closest_left == [a-1,0] :
        closest_left = min(points)
    if closest_right == [b+1,0] :
        closest_right = max(points)

    if nb_point_left == k :
        return (closest_left)
    elif nb_point_left>k :
        return (find(left_points, k, a, closest_left[0]))
    else :
        return(find(right_points,k-nb_point_left,closest_right[0],b))

    
def line (p1: list,p2: list,p: list):
    '''
    Returns the value of the ordinate of the line defined by points p1 and p2, calculated at the x-coordinate of point p.
    '''
    if p2[0] == p1[0]:
        return float('-inf')
    return p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(p[0]-p1[0])


def find_line(points: list, m: list):
    '''
    Find the line defined by two points of 'points' which is higher than each point of 'points' and that intersect x=xm as low as possible

    Args: 
        points(list): set of points in the 2D plane
        m(list):  point of 'points' with the mediane x-coodinate

    Returns: 
        p1(float), p2(float): points defining the line in the order of x-coordinate
    '''
    xm = m[0]       #median x-coordinate

    # random order
    rd.shuffle(points)
    
    # finding the first basis
    k = 0
    while points[k][0] >= xm :   
        k+=1
    p1 = points[k]

    k = 0
    while points[k][0] < xm :
        k+=1
    p2 = points[k]

    left_points = [p1]
    right_points = [p2]

    # update of the basis point by point
    for point in points :
        if point[0]<xm:
            left_points.append(point) 
            if point[1] > line(p1,p2,point):
                p1 = point
                for p in right_points :
                    if p[1]>line(p1,p2,p):
                         p2 = p
             
        else : 
            right_points.append(point)
            if point[1] > line(p1,p2,point):
                p2 = point
                for p in left_points :
                    if p[1]>line(p1,p2,p):
                       p1 = p
    
    return p1, p2



def upper_hull (points: list) :
    '''
    Finds the points that make up the upper part of the convex hull
    
    Args: 
        points(list): set of points in the 2D plane

    Returns: 
        (list): list of the points that make up the upper part of the convex hull, sorted from left to right 
    '''
    if len(points) < 2 :
        return points
    if len(points) == 2 :
        if points[0][0]<= points[1][0]:
            return points
        else :
            return [points[1],points[0]]
    
    m = median(points)
    p1,p2 = find_line (points, m)
    right_points = []
    left_points = []
    for point in points :
        if point[0] <= p1[0] : 
            left_points.append(point) 
        elif point[0] >= p2[0] :
            right_points.append(point)

    left_hull = upper_hull(left_points)
    right_hull = upper_hull(right_points)

    if len(left_hull) >=1 and left_hull[-1][0] == p1[0] :
        left_hull = left_hull[:-1]

    if len(right_hull) >=1 and right_hull[0][0] == p2[0] :
        right_hull = right_hull[1:]
    
    hull = left_hull + [p1,p2] + right_hull
    return hull


def inversion (points: list) :
    '''
    Applies a symetrie with respect to the axis y=0.5 to each point of 'points'
    
    Args: 
        points(list): set of points in the 2D plane

    Returns: 
        points(list): symetrical set of points in the 2D plane
    '''
    inverted_points = [p.copy() for p in points]
    for k in range (len(inverted_points)):
        inverted_points[k] = [inverted_points[k][0],1-inverted_points[k][1]]
    return inverted_points


def lower_hull (points: list) :
    '''
    Finds the points that make up the lower part of the convex hull
    
    Args: 
        points(list): set of points in the 2D plane

    Returns: 
        (list): list of the points that make up the lower part of the convex hull, sorted from left to right 
    '''
    inverted_points = inversion(points)
    hull = upper_hull(inverted_points)
    hull = inversion(hull)
    return hull
    

def output_sensitive_hull (points: np.ndarray):
    '''
    Finds the points that make up the convex hull using the output sensitive algorithme
    
    Args: 
        points(np.ndarray): set of points in the 2D plane

    Returns: 
        (np.ndarray): set of the points that make up the convex hull, in counter clockwise order
    '''
    P = [point.tolist() for point in points]

    upper = upper_hull(P)
    upper.reverse()

    lower = lower_hull(P)  
    lower = lower[1:]
    #lower = lower[1:-1]

    convex_hull = upper + lower
    convex_hull = np.array(convex_hull)

    return(convex_hull)