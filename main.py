# Phoenix Valent
	#U3 PROJECT
		# "Recursive trees more like dumb trees" -Conner

# (%) baby modulo is also there

import turtle as t
import random


"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""

def colorPicker():
	colorsList = [
	['#880808', '#800020', '#8B0000', '#DC143C'], # red
	['#CC5500', '#F28C28', '#FFAC1C', '#E97451'], # orange
	['#FFBF00', '#FFFF8F', '#FFEA00', '#E49B0F'], # yellow
	['#50C878', '#228B22', '#4F7942', '#5F8575'], # green
	['#00008B', '#6495ED', '#6082B6', '#ADD8E6'], # blue
	['#301934', '#5D3FD3', '#702963', '#CF9FFF'], # purple
	['#DE3163', '#AA336A', '#DA70D6', '#F33A6A'], # pink
	['#818589', '#D3D3D3', '#899499', '#E5E4E2'] # grayscale
	]
	return random.choice(colorsList)

SCHEME = colorPicker() #ik this is bad programming practice but Sean told me to

def treetle(t, pen, branchLength, angle=90, direction='L'): # for random branches and stuff, add branch = 2
	if pen == 1: # based case, leaves
		t.color(random.choice(SCHEME))
		t.pensize(10)

		if direction == 'L':
			t.lt(angle)
		elif direction == 'R':
			t.rt(angle)

		t.pendown()
		t.forward(branchLength)
		t.penup()

		t.backward(branchLength)
		if direction == 'L':
			t.rt(angle)
		elif direction == 'R':
			t.lt(angle)


	else:
		if direction == 'L':
			t.lt(angle)
		elif direction == 'R':
			t.rt(angle)
		
		t.pendown()
		t.pensize(pen)
		t.forward(branchLength)
		treetle(t, pen-1, branchLength-4, random.randint(15, 45), 'L')
		t.color('#402300')
		treetle(t, pen-1, branchLength-4, random.randint(15, 45), 'R')
		'''
		if branch == 1:
			treetle(t, pen-1, branchLength-4, random.randint(15, 45), random.choice(['L', 'R']), random.randint(0, 2))
		elif branch == 2:
			treetle(t, pen-1, branchLength-4, random.randint(15, 45), 'L', random.randint(0, 2))
			treetle(t, pen-1, branchLength-4, random.randint(15, 45), 'R', random.randint(0, 2))
		''' # random branches look ugly but here's how I would do it
		
		
		t.penup()

		t.backward(branchLength)
		if direction == 'L':
			t.rt(angle)
		elif direction == 'R':
			t.lt(angle)

			
def main():
	t.Screen().bgcolor("black")
	t.speed(0)
	t.color('#402300')
	t.penup()
	t.rt(90)
	t.forward(100)
	t.lt(90)
	treetle(t, 10, 50)
	t.mainloop()

if __name__ == "__main__":
	main()