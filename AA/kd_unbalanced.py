
def insert(root,point,axis=0):

    if root is None:
        return {"point":point,"axis":axis,"left":None,"right":None}
    
    if point[axis]<root["point"][axis]:
        root["left"]=insert(root["left"],point,(axis+1)%len(point))
    else:
        root["right"]=insert(root["right"],point,(axis+1)%len(point))
    
    return root

def print_tree(node,level=0,side=None):
    
    if node is not None:
        prefix=""
        if side is not None:
            prefix=side+"---"
        
        print("  "*level+ prefix+ str(node["point"]))
        print_tree(node["left"],level+1,"L")
        print_tree(node["right"],level+1,"R")


points = [(17,12),(1,1),(16,8),(5,4),(18,11),(19,2)]
root=None
for point in points:
    root=insert(root,point,0)
print_tree(root)