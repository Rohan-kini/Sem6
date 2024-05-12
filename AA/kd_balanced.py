def build_kd_tree(points, axis=0):
    
    if not points:
        return None
    
    # Sort points based on the current axis
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    
    # Recursively build left and right subtrees
    return {
        'point': points[median],
        'axis': axis,
        'left': build_kd_tree(points[:median], (axis + 1) % len(points[0])),
        'right': build_kd_tree(points[median + 1:], (axis + 1) % len(points[0]))
    }

def print_tree(root, level=0, side=None):
    
    if root is None:
        return
    
    prefix = ""
    if side is not None:
        prefix = side + "---"
    
    # Print current node
    print('  ' * level + prefix + str(root['point']))
    
    # Recursively print left and right subtrees
    print_tree(root['left'], level + 1, 'L')
    print_tree(root['right'], level + 1, 'R')

# Example usage
points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
root = build_kd_tree(points)
print_tree(root)
