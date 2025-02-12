import os
import keyboard
import turtle
from MazeSolver_S_LT import dfs 
from MazeSolver_Q_LT import bfs

class Maze:
    def __init__(self):
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"

        self.screen = turtle.Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("white")
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)
        self.turtle.penup()
        self.turtle.shape("square")
        self.turtle.shapesize(1.5, 1.5)
        self.turtle.color("orange")

        self.text_turtle = turtle.Turtle()
        self.text_turtle.speed(0)
        self.text_turtle.penup()
        self.text_turtle.hideturtle()
        self.text_turtle.goto(0, 250)

    def draw_maze(self):
        self.screen.tracer(0)  
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                screen_x = -200 + x * 40
                screen_y = 200 - y * 40
                if cell == "X":
                    self.turtle.penup()
                    self.turtle.goto(screen_x, screen_y)
                    self.turtle.pendown()
                    self.turtle.begin_fill()
                    for _ in range(4):
                        self.turtle.forward(40)
                        self.turtle.right(90)
                    self.turtle.end_fill()
        self.screen.tracer(1)  

    def draw_player(self):
        screen_x = -200 + self.ply.x * 40
        screen_y = 200 - self.ply.y * 40
        self.turtle.penup()
        self.turtle.goto(screen_x, screen_y)
        self.turtle.pendown()

    def is_in_bound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print_end(self):
        self.screen.clear()
        self.screen.bgcolor("white")
        self.turtle.goto(0, 0)
        self.turtle.write(">>>>> Congratulation!!! <<<<<", align="center", font=("Arial", 24, "normal"))
        self.screen.bye()
          
class pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x

if __name__ == '__main__':
    m = Maze()
    m.draw_maze()
    m.draw_player()

    while True:
        if keyboard.is_pressed("q"):
            m.text_turtle.clear()
            m.text_turtle.write("Quit Program", align="center", font=("Arial", 16, "normal"))
            m.screen.tracer(0)  
            break
        if keyboard.is_pressed("d"):
            m.text_turtle.clear()
            m.text_turtle.write("Running DFS...", align="center", font=("Arial", 16, "normal"))
            m.screen.tracer(0)  
            if dfs(m):
                m.text_turtle.clear()
                m.text_turtle.write("DFS Found the Exit!", align="center", font=("Arial", 16, "normal"))
            else:
                m.text_turtle.clear()
                m.text_turtle.write("DFS No Solution!", align="center", font=("Arial", 16, "normal"))
            m.screen.tracer(1) 
        if keyboard.is_pressed("b"):
            m.text_turtle.clear()
            m.text_turtle.write("Running BFS...", align="center", font=("Arial", 16, "normal"))
            m.screen.tracer(0)  
            if bfs(m):
                m.text_turtle.clear()
                m.text_turtle.write("BFS Found the Exit!", align="center", font=("Arial", 16, "normal"))
            else:
                m.text_turtle.clear()
                m.text_turtle.write("BFS No Solution!", align="center", font=("Arial", 16, "normal"))
            m.screen.tracer(1)  