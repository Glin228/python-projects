from tkinter import *
import random

birth = ('3')
life = ('2', '3')

root = Tk()
root.geometry("500x500")
root.title("Игра жизнь или типа того")
c = Canvas(width = 500, height = 500)
c.pack()
field = []

def draw_cell(x, y):
	c.create_rectangle(x*10-5, y*10-5, x*10+5, y*10+5, fill="black")

def count_neighbours(x, y):
	global field
	neighbours = [field[x-1][y-1], field[x][y-1], field[x+1][y-1], field[x-1][y], field[x+1][y], field[x-1][y+1], field[x][y+1], field[x+1][y+1]]
	#print(neighbours.count(True))
	return neighbours.count(True)

def start():
	global field
	for x in range(51):
		field.append([])
		for y in range(50):
			field[x].append(random.choice([True, False]))
		field[x].append(False)
start()

def main():
	global field
	field2 = field
	for x in range(50):
		for y in range(50):
			if str(count_neighbours(x, y)) in birth and not field2[x][y]:
				field2[x][y] = True
			elif str(count_neighbours(x, y)) in life and field[x][y]:
				field2[x][y] = True
			else:
				field2[x][y] = False

	field = field2
	for x in range(50):
		for y in range(50):
			if field[x][y]:
				draw_cell(x, y)
	for x in range(50):
		for y in range(50):
			c.create_rectangle(x*10-5, y*10-5, x*10+5, y*10+5)
	c.update()
	c.delete("all")

if __name__ == '__main__':
	while True:
		main()