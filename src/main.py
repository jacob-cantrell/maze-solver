from graphics import Window, Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(450, 450, 600, 600)
    cell2.draw(150, 150, 250, 250)
    cell1.draw_move(cell2, False)
    win.wait_for_close()

main()