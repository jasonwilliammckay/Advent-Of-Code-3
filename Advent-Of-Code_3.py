def move (x, y):
		if (c == '<'):
			x = x - 1
		elif (c == '>'):
			x = x + 1
		elif (c == '^'):
			y = y + 1
		elif (c == 'v'):
			y = y - 1
		return x, y

x_santa = y_santa = x_robo = y_robo = 0
santaTurn = True

hashmap = {}
hashmap[0,0] = "Visited"

with open ('input.txt', 'r') as fileInput:

	while True:
		c = fileInput.read(1)

		if not c:
			break
		
		if (santaTurn == True):
			x_santa, y_santa = move(x_santa, y_santa)
			hashmap[x_santa,y_santa] = "Visited"
		else:
			x_robo, y_robo = move(x_robo, y_robo)
			hashmap[x_robo,y_robo] = "Visited"
		
		santaTurn = ~santaTurn
		
print "%s houses were given presents." % len(hashmap)
