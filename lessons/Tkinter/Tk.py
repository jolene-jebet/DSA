import tkinter as tk

# Linked list for displaying users
# Queue for displaying highest in the scores
# Binary tree
# Graph for di

# Maze layout: 0 = wall, 1 = path, 2 = player, 3 = goal
maze = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 3],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [2, 1, 1, 1, 0],
]

player_pos = [4, 0]  # Start at bottom left

CELL_SIZE = 50


def draw_maze(canvas):
    canvas.delete("all")
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if maze[row][col] == 0:
                color = "black"
            elif maze[row][col] == 1:
                color = "white"
            elif maze[row][col] == 2:
                color = "blue"
            elif maze[row][col] == 3:
                color = "green"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


def move_player(direction, canvas, message_label):
    row, col = player_pos
    new_row, new_col = row, col

    if direction == "up":
        new_row -= 1
    elif direction == "down":
        new_row += 1
    elif direction == "left":
        new_col -= 1
    elif direction == "right":
        new_col += 1
    else:
        message_label.config(text="Invalid direction. Use: up, down, left, right")
        return

    if (0 <= new_row < len(maze)) and (0 <= new_col < len(maze[0])):
        if maze[new_row][new_col] in (1, 3):
            # Update player position
            maze[row][col] = 1
            player_pos[0], player_pos[1] = new_row, new_col
            if maze[new_row][new_col] == 3:
                maze[new_row][new_col] = 2
                draw_maze(canvas)
                message_label.config(text="🎉 You reached the goal!")
                return
            maze[new_row][new_col] = 2
            message_label.config(text="")
        else:
            message_label.config(text="Blocked by a wall!")
    else:
        message_label.config(text="Can't move outside the maze!")

    draw_maze(canvas)


def handle_input(entry, canvas, label):
    direction = entry.get().lower().strip()
    entry.delete(0, tk.END)
    move_player(direction, canvas, label)


def main():
    root = tk.Tk()
    root.title("Maze Runner")

    canvas = tk.Canvas(root, width=5 * CELL_SIZE, height=5 * CELL_SIZE)
    canvas.pack()

    entry = tk.Entry(root)
    entry.pack()
    entry.focus()

    message_label = tk.Label(root, text="", fg="red")
    message_label.pack()

    entry.bind("<Return>", lambda event: handle_input(entry, canvas, message_label))

    draw_maze(canvas)
    root.mainloop()


if __name__ == "__main__":
    main()