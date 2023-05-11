from tkinter import *
import math, time, random

Dir = 0
X = 250
Y = 250
_tail_ = []
Score = 0
AppleX = random.randint(100, 400)
AppleY = random.randint(100, 400)

tk = Tk()
tk.geometry("500x500")
tk.title("Змейка")
c = Canvas(width = 500, height = 500)
c.pack()

def check_on_border(x, y):
	if x > 480 or y > 480 or x < 0 or y < 0:
		return True
	else:
		return False

def control(press):
	global Dir
	if press.keysym == "Up":
		Dir = 0
	elif press.keysym == "Down":
		Dir = 180
	elif press.keysym == "Right":
		Dir = 90
	elif press.keysym == "Left":
		Dir = 270
	else:
		print(press.keysym)
c.bind_all('<Key>', control)

class tail:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def draw(self):
		c.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y +20, fill="black")
	def check_collision(self):
		global X, Y
		if self.x == X and self.y == Y:
			return True
		else:
			return False

def Apple():
	global AppleX, AppleY, X, Y, Score
	c.create_rectangle(AppleX-10, AppleY-10, AppleX+10, AppleY+10, fill="Green")
	if (lambda x1, y1, x2, y2: math.sqrt((x1-x2)**2+(y1-y2)**2))(X, Y, AppleX, AppleY)<40:
		Score+=1
		AppleX = random.randint(100, 400)
		AppleY = random.randint(100, 400)

def head():
	global Dir, X, Y, c
	_tail_.append(tail(X, Y))
	if Dir == 0:
		Y-=40
	if Dir==180:
		Y+=40
	if Dir == 270:
		X-=40
	if Dir == 90:
		X+=40
	c.create_rectangle(X-20, Y-20, X+20, Y+20, fill="Red")

def draw_snake(_tail_):
	global Score, X, Y
	cols = []
	while len(_tail_) > Score:
		_tail_.pop(0)
	for i in range(len(_tail_)):
		_tail_[i].draw()
		if not i == len(_tail_)-1:
			cols.append(_tail_[i].check_collision())
	#print(cols.count(True), Score, check_on_border(X, Y))
	if cols.count(True) >= 1 or check_on_border(X, Y):
		Score = 0 
		X = 250
		Y = 250

def main():
	global _tail_, score, c
	while True:
		c.delete("all")
		Apple()
		head()
		draw_snake(_tail_)
		c.update()
		time.sleep(0.3)

if __name__ == '__main__':
	main()
	tk.mainloop()
