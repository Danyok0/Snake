from tkinter import *
from random import randint


class Game:
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_coords = [[14, 14]]  #Начальная позиция змеи
        self.initial_snake_coords = list(self.snake_coords)  #Запоминаем начальное состояние
        self.apple_coords = None
        self.set_apple()
        self.vector = {
            "Up": (0, -1),
            "Down": (0, 1),
            "Left": (-1, 0),
            "Right": (1, 0)
        }
        self.direction = self.vector["Right"]  #Начальное направление
        self.score = 0
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.set_direction)
        self.GAME()

    def set_apple(self):
        #Генерируем новую позицию яблока
        while True:
            new_x, new_y = randint(0, 29), randint(0, 29)
            if [new_x, new_y] not in self.snake_coords:
                break
        self.apple_coords = [new_x, new_y]

    def set_direction(self, event):
        #Обработка нажатия клавиш управления направлением змеи
        if event.keysym in self.vector:
            self.direction = self.vector[event.keysym]

    def draw(self):
        #Рисуем игровое поле (яблоко и змею)
        self.canvas.delete("all")
        x_apple, y_apple = self.apple_coords
        self.canvas.create_rectangle(
            x_apple * 10,
            y_apple * 10,
            (x_apple + 1) * 10,
            (y_apple + 1) * 10,
            fill="red",
            width=0
        )
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(
                x * 10,
                y * 10,
                (x + 1) * 10,
                (y + 1) * 10,
                fill="green",
                width=0
            )

    @staticmethod
    def coord_check(coord):
        #Проверка границ игрового поля
        return coord % 30

    def reset_game_state(self):
        #Возвращаем змею в начальное положение и сбрасываем очки
        self.snake_coords = list(self.initial_snake_coords)
        self.score = 0
        label1.config(text=f'SCORE: {self.score}')

    def eat_apple(self):
        #Обрабатываем ситуацию съедения яблока
        self.score += 10
        label1.config(text=f'SCORE: {self.score}')
        self.set_apple()

    def GAME(self):
        #Основной игровой цикл
        self.draw()
        x, y = self.snake_coords[0]
        dx, dy = self.direction
        next_x = self.coord_check(x + dx)
        next_y = self.coord_check(y + dy)

        #Проверяем столкновение с самим собой
        if [next_x, next_y] in self.snake_coords[:-1]:
            self.reset_game_state()
        else:
            self.snake_coords.insert(0, [next_x, next_y])
            if next_x != self.apple_coords[0] or next_y != self.apple_coords[1]:
                self.snake_coords.pop()
            else:
                self.eat_apple()

        self.canvas.after(100, self.GAME)

# Настройка окна и канваса
root = Tk()
canvas = Canvas(width=300, height=320, bg="black")
canvas.pack()
label1 = Label(root, text=f'SCORE: {0}', font='AirbusDisp2 12', bg='black', fg='#48bcff', anchor='center')
label1.place(x=2, y=300)
game = Game(canvas)
root.mainloop()