from Position import pos
from Queue import Queue

def bfs(maze_obj):
    queue = Queue()
    queue.enqueue(maze_obj.ply)
    visited = set()
    visited.add((maze_obj.ply.y, maze_obj.ply.x))
    parent = {}

    while not queue.is_empty():
        current_pos = queue.dequeue()
        if (current_pos.y, current_pos.x) == (maze_obj.end.y, maze_obj.end.x):
            while current_pos != maze_obj.ply:
                maze_obj.maze[current_pos.y][current_pos.x] = "*"
                current_pos = parent[(current_pos.y, current_pos.x)]
            maze_obj.maze[maze_obj.ply.y][maze_obj.ply.x] = "P"
            maze_obj.draw_maze()
            maze_obj.draw_player()
            maze_obj.print_end()
            return True

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_y = current_pos.y + move[0]
            new_x = current_pos.x + move[1]

            if maze_obj.is_in_bound(new_y, new_x) and (new_y, new_x) not in visited:
                if maze_obj.maze[new_y][new_x] == " " or maze_obj.maze[new_y][new_x] == "E":
                    queue.enqueue(pos(new_y, new_x))
                    visited.add((new_y, new_x))
                    parent[(new_y, new_x)] = current_pos
                    maze_obj.maze[current_pos.y][current_pos.x] = "."
                    maze_obj.maze[new_y][new_x] = "P"
                    maze_obj.screen.update()   
                    break
    return False