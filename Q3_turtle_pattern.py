import turtle

def draw_koch_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_edge(t, length, depth - 1)
        t.left(60)
        draw_koch_edge(t, length, depth - 1)
        t.right(120)
        draw_koch_edge(t, length, depth - 1)
        t.left(60)
        draw_koch_edge(t, length, depth - 1)

def draw_polygon(t, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_koch_edge(t, length, depth)
        t.right(angle)

def main():
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    screen = turtle.Screen()
    screen.title("Recursive Geometric Pattern")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length / 2, length / 2)  # Center the drawing
    t.pendown()

    draw_polygon(t, sides, length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
