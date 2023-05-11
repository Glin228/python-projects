from tkinter import *
import random, time
#from threading import *
from multiprocessing import Process

dots = []

colors = ["red", "blue", "Yellow"]

WIDTH = 100
HEIGHT = 100
DOT_SIZE = 7
DEBUG = False

for x in range(WIDTH+1):
	dots.append([])
	randomizer = 0
	for y in range(HEIGHT+1):
		if random.randint(0, 10) == 1:
			randomizer+=1
		dots[x].append(colors[randomizer%len(colors)])
	dots[x].append(None)
dots.append([])
for i in range(HEIGHT+1):
	dots[WIDTH+1].append(None)

def getNeighbours(x, y):
	global dots
	return [dots[x-1][y-1], dots[x][y-1], dots[x+1][y-1], dots[x-1][y], dots[x+1][y], dots[x-1][y+1], dots[x][y+1], dots[x+1][y+1]]

def setColor(x, y, new_dots):
	global dots, colors
	neighbours = getNeighbours(x, y)
	foundColors = []
	for color in colors:
		foundColors.append(neighbours.count(color))
	if DEBUG: 
		print(neighbours)
		print(dots[x][y])
		print(colors[foundColors.index(max(foundColors))])
	dots[x][y] = colors[foundColors.index(max(foundColors))]

def process():
	global dots
	new_dots = []
	new_dots = dots
	for x in range(WIDTH):
		for y in range(HEIGHT):
			colors.reverse()
			setColor(x, y, new_dots)
	dots = new_dots
	del new_dots

def render():
	global dots, DOT_SIZE
	root = Tk()
	canv = Canvas(width = WIDTH*DOT_SIZE-5, height = HEIGHT*DOT_SIZE-5)
	root.title("Вiйна")
	print("canv.pack()")
	canv.pack()
	while True:

		for x in range(len(dots)):
			for y in range(len(dots[x])):
				canv.create_rectangle(x*DOT_SIZE, 
					y*DOT_SIZE, 
					x*DOT_SIZE+DOT_SIZE, 
					y*DOT_SIZE+DOT_SIZE, 
					fill = dots[x][y], 
					outline = dots[x][y])

				#print(f"{x=}, {y=}")
		canv.update()
		canv.delete("all")
		process()
	root.mainloop()

if __name__ == '__main__':
	
	if DEBUG:
		render()
		process()
	else:
		t = Process(target = render, args = ())
		t.start()
