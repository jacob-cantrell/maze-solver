from graphics import Window, Maze

def main():
    win = Window(800, 600)
    num_rows = 12
    num_cols = 16
    margin = 50
    cell_size_x = (800 - 2 * margin) / num_cols
    cell_size_y = (600 - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()

main()