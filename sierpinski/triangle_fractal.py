""" 
Uses turtle module to draw Sierpinski triangle.
"""
import turtle #import turtle module

""" draw_triangle
Takes three arguments to draw a triangle
1.turtle object
2.triangles vertices
3.boolean value for filling the shape
"""
def draw_triangle(some_turtle,coordinates,isFill):

	some_turtle.up()
	some_turtle.goto(coordinates[1][0],coordinates[1][1])
	some_turtle.down()
	some_turtle.fill(isFill)
	some_turtle.goto(coordinates[2][0],coordinates[2][1])
	some_turtle.goto(coordinates[0][0],coordinates[0][1])
	some_turtle.goto(coordinates[1][0],coordinates[1][1])
	some_turtle.end_fill()
    
""" get_points
Takes length of the triangles edge as argument and returns vertices
"""	
def get_points(edge_length):
	return  [[-edge_length,-edge_length/2],[0,edge_length],[edge_length,-edge_length/2]]
		

""" get_middle
Takes two points as argument and returns their midpoint
"""			
def get_middle(point1,point2):
	return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
		

""" triangle_fractal
Takes three arguments to draw a Sierpinski triangle using recursion
1.turtle object
2.triangles vertices
3.degree of fractal
"""				
def triangle_fractal(some_turtle,coordinates, degree):
	if degree < 1:
		isFill = 1
	else:
		isFill = 0
	draw_triangle(some_turtle,coordinates,isFill)
	if degree > 0:
		triangle_fractal(some_turtle,[coordinates[1],
						get_middle(coordinates[1],coordinates[0]),
						get_middle(coordinates[1],coordinates[2])], degree-1)
		triangle_fractal(some_turtle,[coordinates[2],
						get_middle(coordinates[2],coordinates[1]),
						get_middle(coordinates[2],coordinates[0])], degree-1)
	
		triangle_fractal(some_turtle,[coordinates[0],
						get_middle(coordinates[0],coordinates[1]),
						get_middle(coordinates[0],coordinates[2])], degree-1)
		
def main():
	window = turtle.Screen()
	window.bgcolor("white")	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue", "green")
	brad.fillcolor("green")
	brad.speed(10)
	#coordinates = [[-100,-50],[0,100],[100,-50]]
	coordinates2 = get_points(200)
	
	triangle_fractal(brad,coordinates2, 3)
	
	
	window.exitonclick()

main()