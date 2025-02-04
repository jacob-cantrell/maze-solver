from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    line1 = Line(Point(0, 0), Point(50, 50)) 
    line2 = Line(Point(0, 100), Point(100, 0))
    win.draw_line(line1, "black")
    win.draw_line(line2, "black")
    win.wait_for_close()

main()