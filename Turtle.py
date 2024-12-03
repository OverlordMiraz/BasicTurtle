import turtle

def setup_turtle():
    t = turtle.Turtle()
    t.speed(3)  # Set moderate speed for smooth animation
    t.pensize(5)  # Set pen thickness
    t.penup()
    t.goto(-200, 0)  # Starting position
    t.pendown()
    return t

def draw_M(t):
    t.setheading(90)  # Point upward
    t.forward(100)    # Left vertical line
    t.setheading(-45) # Diagonal down-right
    t.forward(70)
    t.setheading(45)  # Diagonal up-right
    t.forward(70)
    t.setheading(-90) # Right vertical line
    t.forward(100)

def draw_I(t):
    t.setheading(90)  # Point upward
    t.forward(100)    # Vertical line
    t.setheading(-90) # Go back down
    t.forward(100)

def draw_R(t):
    t.setheading(90)  # Point upward
    t.forward(100)    # Vertical line
    t.setheading(0)   # Point right
    t.forward(50)     # Top horizontal
    t.setheading(-90) # Point down
    t.forward(40)     # Right side of loop
    t.setheading(180) # Point left
    t.forward(50)     # Bottom of loop
    t.setheading(-45) # Diagonal for leg
    t.forward(85)

def draw_A(t):
    t.setheading(75)  # Angle for left side
    t.forward(104)    # Left diagonal
    t.setheading(-75) # Angle for right side
    t.forward(104)    # Right diagonal
    t.penup()
    t.backward(52)    # Go back halfway
    t.setheading(180) # Point left
    t.pendown()
    t.forward(27)     # Cross line

def draw_Z(t):
    t.setheading(0)   # Point right
    t.forward(70)     # Top horizontal
    t.setheading(-135) # Diagonal angle
    t.forward(100)    # Diagonal line
    t.setheading(0)   # Point right
    t.forward(70)     # Bottom horizontal

def main():
    screen = turtle.Screen()
    screen.title("Writing MIRAZ")
    screen.bgcolor("white")
    
    t = setup_turtle()
    
    # Draw each letter with spacing
    draw_M(t)
    t.penup()
    t.forward(80)
    t.pendown()
    
    draw_I(t)
    t.penup()
    t.forward(80)
    t.pendown()
    
    draw_R(t)
    t.penup()
    t.forward(80)
    t.pendown()
    
    draw_A(t)
    t.penup()
    t.forward(80)
    t.pendown()
    
    draw_Z(t)
    
    t.hideturtle()  # Hide the turtle cursor
    screen.mainloop()

if __name__ == "__main__":
    main() 