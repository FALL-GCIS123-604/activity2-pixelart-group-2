"""
This imports the Screen and Turtle classes from the turtle graphics module,
which is used for drawing shapes and graphics.
 """
from turtle import Screen, Turtle

'''Hello Professor,
Here is our assignment 2 done by four members:
Maaz Shaikh
Mohammed al salaam
Maham Mustafa 
Arina Baiazitova
Hope you like it!'''


"""
These constants define the size of each pixel.
And the rows and columns.
And the default colors for the pen and fill.
"""

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta): #Defines a function called initialization that takes a turta as an argument
    
    turta.speed(0) #Sets the turtle's speed
    turta.penup() #Lifts the pen up
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) #Moves the turtle to the position.
    turta.setheading(0) #Sets the turtle's heading to 0 degrees (facing right).
    turta.pendown() #Lowers the pen
    turta.pencolor(DEFAULT_PEN_COLOR) #Sets the pen color and fill color to their default values.
    turta.fillcolor(DEFAULT_PIXEL_COLOR)


"""
Defines a function to map a color code (as a string) to an actual color
"""

"""
Each color code (0-9, A) is mapped to a corresponding color. If the code isn't recognized, it returns None.
"""
def get_color(colour):
    
    if colour == '0':
        return 'black'
    elif colour == '1':
        return 'white'
    elif colour == '2':
        return 'red'
    elif colour == '3':
        return 'yellow'
    elif colour == '4':
        return 'orange'
    elif colour == '5':
        return 'green'
    elif colour == '6':
        return 'yellowgreen'
    elif colour == '7':
        return 'sienna'
    elif colour == '8':
        return 'tan'
    elif colour == '9':
        return 'gray'
    elif colour == 'A':
        return 'darkgray'
    else:
        return None  

"""
Defines a function to draw a filled square (pixel) of the specified color
"""
def draw_color_pixel(color_string, turta):
    
    turta.fillcolor(color_string)
    turta.begin_fill()

    """Draws a square by moving forward and turning right four times."""

    for _ in range(4):
        turta.forward(PIXEL_SIZE)  
        turta.right(90)  
    """Ends the fill, lifts the pen, moves forward one pixel size, and puts the pen down again."""
    turta.end_fill()
    turta.penup()
    turta.forward(PIXEL_SIZE)  
    turta.pendown()

"""Defines a function to draw a pixel based on the color code."""

def draw_pixel(colour, turta):

    color_string = get_color(colour)   
    """If the color is valid, it draws the pixel; otherwise, it prints an error message."""  
    if color_string:
        draw_color_pixel(color_string, turta)
    else:
        print("wrong color code.")

"""Defines a function to draw a line of pixels from a string of color codes."""
def draw_line_from_string(color_string, turta):
    
    for colour in color_string:
        color = get_color(colour)

        """If any color is invalid, it prints an error and stops drawing."""
        if color is None:
            print("invalid color in line.")
            return False  
        draw_pixel(colour, turta)
    """Returns True if the line was drawn successfully."""
    return True


"""Defines a function to read a shape definition from a file and draw it."""
def draw_shape_from_file(turta, filename):
    
    """Attempts to open the specified file for reading."""
    try:
        with open(filename, 'r') as file:
            y_start = turta.ycor()
            for line in file:
                """Reads each line from the file and removes whitespace."""
                line = line.strip()
                """Draws the line using the color codes from the file. If it encounters an error, it prints a message and stops."""
                if not draw_line_from_string(line, turta):
                    print("Stopped drawing")
                    break
                
                """Moves the turtle to the next row down after finishing a line."""
                turta.penup()
                turta.goto(turta.xcor() - len(line) * PIXEL_SIZE, y_start - PIXEL_SIZE)
                y_start -= PIXEL_SIZE  
                turta.pendown()
    
        """Catches and handles the case where the specified file does not exist."""
    except FileNotFoundError:
        print("incorrect file.")

"""Defines the main function."""
def main():
    # Create the turtle object
    turta = Turtle()
    initialization(turta)  # Set the initial position of the turtle

    # Ask the user for the path to the text file
    filename = input("Enter the path of the file (make sure the file is within the same folder): ")

    # Draw the shape from the file
    draw_shape_from_file(turta, filename)

    # Prevent the turtle graphics from closing immediately
    input("")


if __name__ == "__main__":
    main()
