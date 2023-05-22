from canvas import *
from square import *
from rectangle import *

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

colors = {"white": (255,255,255), "black": (0,0,0)}
canvas_color = input("Enter canvas color (black or white): ")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw (rectangle or square)? Enter 'q' to quit ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red do you want? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    elif shape_type.lower() == "square":
        square_x = int(input("Enter x of the square: "))
        square_y = int(input("Enter y of the square: "))
        square_width = int(input("Enter width of the square: "))
        square_height = int(input("Enter height of the square: "))
        red = int(input("How much red do you want? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        s1 = Rectangle(x=square_x, y=square_y, height=square_height, width=square_width, color=(red, green, blue))
        s1.draw(canvas)
    
    elif shape_type.lower() == "q":
        break


canvas.make("C:\\Users\\mhmts\\PycharmProjects\\math painting app\\canvas.png")

