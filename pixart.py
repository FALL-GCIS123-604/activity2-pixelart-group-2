import turtle as t  

def draw_filled_square(color, size):
    """Draws a filled square of a given color and size."""
    t.fillcolor(color)  # Set the fill color for the square
    t.begin_fill()  # Start filling the square with color
    for angle in [0, 90, 180, 270]:  # Loop through the four right angles to draw the square
        t.forward(size)  # Move the turtle forward by the specified size
        t.right(90)  # Turn the turtle 90 degrees to the right
    t.end_fill()  # End the filling of the square

def draw_line_from_color_codes(color_codes, size):
    """Draws a line of squares based on a string of color codes (e.g., '0202')."""
    for code in color_codes:  # Loop through each character (color code) in the string
        # Set the color based on the color code ('0' for black, '2' for red)
        color = 'black' if code == '0' else 'red' if code == '2' else None
        if color:
            draw_filled_square(color, size)  # Draw a filled square of the corresponding color
        t.penup()  # Lift the pen to move to the next position without drawing
        t.forward(size)  # Move the turtle forward by the size of the square
        t.pendown()  # Lower the pen to resume drawing

def draw_grid():
    """Draws a 20x20 checkerboard grid."""
    size = 20  # Define the size of each square
    num_squares = 20  # Define the number of squares in each row/column
    
    # Define color patterns for even and odd rows 
    even_row_codes = "02" * (num_squares // 2)  # Even rows start with black
    odd_row_codes = "20" * (num_squares // 2)   # Odd rows start with red

    # Move the turtle to the top-left corner to start drawing the grid
    t.penup()
    t.goto(-num_squares * size // 2, num_squares * size // 2)
    t.pendown()

    for row in range(num_squares):  # Loop through each row
        if row % 2 == 0:
            draw_line_from_color_codes(even_row_codes, size)  # Draw even row (starting with black)
        else:
            draw_line_from_color_codes(odd_row_codes, size)   # Draw odd row (starting with red)
        
        # Move the turtle to the start of the next row, one step down
        t.penup()
        t.goto(-num_squares * size // 2, t.ycor() - size)
        t.pendown()

# Setup and draw the grid
t.speed(0)  
draw_grid() 

# Hide the turtle when done and display the drawing window
t.hideturtle()
t.mainloop()  
