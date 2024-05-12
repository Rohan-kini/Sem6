import math

def orientation(p,q,r):
    val=(q[1]-p[1])*(r[0]-q[0])-(q[0]-p[0])*(r[1]-q[1])
    if val==0:
        return 0
    return 1 if val>0 else -1


def graham_scan(points):

    n=len(points)

    if n<3:
        return []
    
    min_points=min(points,key=lambda x:(x[1],x[0]))

    sorted_points=sorted(points,key=lambda x:(math.atan2(x[1]-min_points[1],x[0]-min_points[0])))

    stack=[sorted_points[0],sorted_points[1],sorted_points[2]]

    for i in range(3,n):
        while len(stack)>1 and orientation(stack[-2],stack[-1],sorted_points[i])==1:
            stack.pop()
        stack.append(sorted_points[i])
    
    return stack


points=[(0, 0), (3, 0), (1, 4), (3, 3), (5, 2), (5, 5), (9, 6), (7, 0), (10, 0)]
convex_hull=graham_scan(points)
print(f"Convex Hull:{convex_hull}")