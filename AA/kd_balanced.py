def bkdtree(point,axis=0):

    if not point:
        return None
    
    point.sort(key=lambda x:x[axis])
    median=len(point)//2

    return {
        "point":point[median],
        "axis":axis,
        "left":bkdtree(point[:median],(axis+1)%len(point[0])),
        "right":bkdtree(point[median+1:],(axis+1)%len(point[0]))
    }

def ptree(root,level=0,side=None):

    if root is None:
        return
    
    prefix=""
    if side is not None:
        prefix=side+"----"
    
    print("  "*level+prefix+str(root["point"]))
    ptree(root["left"],level+1,"L")
    ptree(root["right"],level+1,"R")

    

points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
root=bkdtree(points,0)
ptree(root)