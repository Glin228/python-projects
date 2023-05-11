import math, random, time
from tkinter import *
tk = Tk()
tk.title("Кораблик")
c = Canvas(width = 500, height = 500, background="white")
c.pack()

meteors = []

def dist(x1, x2, y1, y2):
	return math.sqrt((x1-x2)**2 + (y1 - y2)**2)

def check_collisions():
	global meteors, sh
	for i in meteors:
		if dist(sh.x, i.x, sh.y, i.y) < i.size + 5:
			return True
	return False

def movement(press):
	if press.keysym == "Up":
		sh.move("up", 10)
	elif press.keysym == "Right":
		sh.move("right", 10)
	elif press.keysym == "Left":
		sh.move("left", 10)
	elif press.keysym == "Down":
		sh.move("down", 10)
	print(press.keysym)
tk.bind_all('<Key>', movement)

class meteor():
	global score, meteors
	def __init__(self, x, y, size, direction):
		self.x, self.y, self.size, self.direction = x, y, size, direction
	def move(self):
		self.x += math.sin(self.direction)*0.01*score
		self.y += math.cos(self.direction)*0.01*score
		if self.y > 500+self.size:
			meteors.remove(self)
	def draw(self):
		c.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill = "grey")

class ship():
	def __init__(self):
		self.x = 250
		self.y = 250
	def move(self, dir, speed):
		if dir == "up":
			self.y-=speed
		elif dir == "down":
			self.y+=speed
		elif dir == "right":
			self.x+=speed
		elif dir == "left":
			self.x-=speed
	def data(self):
		print(f"X:{self.x}, Y:{self.y}")
	def draw(self):
		c.create_polygon(self.x-10, self.y, self.x, self.y-10, self.x+10, self.y)

sh = ship()
if __name__ == '__main__':
	t1 = time.time()
	tmr = t1
	while True:
		score = round(time.time()-t1)
		c.update()
		c.delete("all")
		sh.draw()
		for i in meteors:
			i.move()
			i.draw()
		c.create_text(50+len(str(score))*10, 10, text = f"Счёт: {score}", font="Helvetica") 
		if check_collisions():
			t1 = time.time()
			meteors.clear()
			sh = ship()
		if time.time()-tmr>10/(score+1):
			tmr = time.time()
			meteors.append(meteor(random.randint(20, 490), -10, random.randint(20, 40), 0))