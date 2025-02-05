from graphics import Window, Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(50, 50, 100, 100)
    cell2.draw(150, 150, 250, 250)
    win.wait_for_close()

main()