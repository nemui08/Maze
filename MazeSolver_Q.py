from Queue import Queue
import time  

# ฟังก์ชัน BFS โดยใช้ Queue
def bfs(maze_obj):
    from Maze import pos
    queue = Queue()  # ใช้ Queue แทน deque
    queue.enqueue(maze_obj.ply)  # ใช้ enqueue() แทน append
    visited = set()
    visited.add((maze_obj.ply.y, maze_obj.ply.x))
    parent = {}

    while not queue.isEmpty():  # ใช้ isEmpty() แทนการเช็คว่า queue ว่างไหม
        current_pos = queue.dequeue()  # ใช้ dequeue() แทน popleft
        if (current_pos.y, current_pos.x) == (maze_obj.end.y, maze_obj.end.x):
            while current_pos != maze_obj.ply:
                maze_obj.maze[current_pos.y][current_pos.x] = "."
                current_pos = parent[(current_pos.y, current_pos.x)]
            maze_obj.maze[maze_obj.ply.y][maze_obj.ply.x] = "P"
            maze_obj.printEND()
            return True

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_y = current_pos.y + move[0]
            new_x = current_pos.x + move[1]

            if maze_obj.isInBound(new_y, new_x) and (new_y, new_x) not in visited:
                if maze_obj.maze[new_y][new_x] != "X":
                    queue.enqueue(pos(new_y, new_x))  # ใช้ enqueue() แทน append
                    visited.add((new_y, new_x))
                    parent[(new_y, new_x)] = current_pos
                    maze_obj.maze[current_pos.y][current_pos.x] = "."
                    maze_obj.maze[new_y][new_x] = "P"
                    maze_obj.print()
                    time.sleep(0.1)
                    break
    return False