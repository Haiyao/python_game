# -*- coding:utf-8 -*-

from tkinter import *
import time
import random

#创建窗体，大小不可调整(resizable),总在所有窗口之前(wm_attributes-topmost)
tk = Tk()
tk.title("Game-ball")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=400,height=500,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

#创建一个Ball类
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        
        start = [-1,-2,-3,3,2,1]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        #winfo_height获取当前画布的高度
        self.canvas_width = self.canvas.winfo_width()
        #winfo_width获取当前画布的宽度值
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #画布函数coords获取id当前坐标
        if pos[0] <= 0:
            self.x = 3
        if pos[1] <= 0:
            self.y = 3
        if pos[2] >=self.canvas_width:
            self.x = -3
        if pos[3] >= self.canvas_height:
            self.y = -3
        
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(100,300,150,310,fill=color)
    
    def draw(self):
        pass

ball = Ball(canvas, 'red')
paddle = Paddle(canvas, 'blue')

while 1:
    paddle.draw()
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)