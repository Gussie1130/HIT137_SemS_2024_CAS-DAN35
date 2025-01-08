import turtle

def draw_tree(t, branch_length, angle_left, angle_right, depth, reduction_factor, total_depth):
    """
    t               
    branch_length   
    angle_left      
    angle_right     
    depth           
    reduction_factor
    total_depth     
    """
    
    if depth == 0:
        return
    
    if depth == total_depth:
        t.color("brown")
        t.pensize(10) 
    else:
        t.color("green")
        t.pensize(max(1, depth)) 
    
    t.forward(branch_length)
    
    t.left(angle_left)
    draw_tree(t, branch_length * reduction_factor,  
              angle_left, angle_right, depth - 1,
              reduction_factor, total_depth)
    t.right(angle_left)
    
    t.right(angle_right)
    draw_tree(t, branch_length * reduction_factor, 
              angle_left, angle_right, depth - 1,
              reduction_factor, total_depth)
    t.left(angle_right)
    
    t.backward(branch_length)


def draw_trunk(t, length):
    t.color("brown")
    t.pensize(10)  
    t.penup()
    t.goto(0, -200) 
    t.pendown()
    t.setheading(90) 
    t.forward(length) 


def main():
    angle_left = int(input("Enter the left branch angle (degrees): "))     
    angle_right = int(input("Enter the right branch angle (degrees): "))    
    branch_length = int(input("Enter the starting branch length (pixels): ")) 
    depth = int(input("Enter the recursion depth: "))                        
    
    while True:
        reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): ").strip())
        if 0 < reduction_factor < 1:
            break
        print("Reduction factor must be between 0 and 1. Try again.")
    
    screen = turtle.Screen()
    screen.title("Recursive Tree")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(5)      
    t.penup()
    t.goto(0, -200) 
    t.left(90)      
    t.pendown()
    
    draw_tree(t, branch_length, angle_left, angle_right,
              depth, reduction_factor, depth)
    
    draw_trunk(t, branch_length)
    
    screen.mainloop()

if __name__ == "__main__":
    main()
