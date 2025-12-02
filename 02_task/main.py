import turtle
import sys


def koch_curve(t, order, size):  # copied from the LMS
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    # AB side
    koch_curve(t, order, size)
    # BC side
    t.right(120)
    koch_curve(t, order, size)
    # AC side
    t.right(120)
    koch_curve(t, order, size)

    window.mainloop()


def parse_args() -> int:
    if len(sys.argv) < 2:
        return 3  # default order

    try:
        order = int(sys.argv[1])
    except ValueError:
        raise ValueError("First argument must be an integer")

    if order <= 0:
        raise ValueError("First argument must be more than zero")

    return order


def main():
    order = parse_args()
    draw_koch_curve(order)


if __name__ == "__main__":
    main()
