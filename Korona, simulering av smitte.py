import matplotlib.pyplot as plt
import random
import numpy as np
import turtle

sc = turtle.Screen()
sc.title("Korona, simulering av smitte")
turtle.speed(0)
turtle.hideturtle()
infected = 1
counter = turtle.Turtle()
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(560, 375)

N = 150
sprites = 1000

positionsx = np.zeros(sprites)
positionsy = np.zeros(sprites)
sprites_infected = np.zeros(sprites)
sprites_infected_history = np.zeros(N)

sprites_infected[0] = 1

n = 0
while n < N:
	i = 0
	if n != 0:
		while i < sprites:
			positionsx[i] = random.randint(positionsx[i]-50, positionsx[i]+50)
			positionsy[i] = random.randint(positionsy[i]-50, positionsy[i]+50)
			i += 1
	else:
		while i < sprites:
			positionsx[i] = random.randint(-500, 500)
			positionsy[i] = random.randint(-300, 300)
			i += 1
	i = 0
	while i < sprites:
		a = 0
		while a < sprites:
			if np.sqrt(abs(positionsx[i]-positionsx[a])**2 + abs(positionsy[i]-positionsy[a])**2) < 10 and a != i:
				if sprites_infected[i] > 3 and sprites_infected[i] <= 14:
					if sprites_infected[a] == 0:
						sprites_infected[a] = 1
						infected += 1
				elif sprites_infected[a] > 3 and sprites_infected[a] <= 14:
					if sprites_infected[i] == 0:
						sprites_infected[i] = 1
						infected += 1
			a += 1
		i += 1
		
	i = 0
	turtle.clear()
	turtle.tracer(0, 0)
	while i < sprites:
		turtle.penup()
		if sprites_infected[i] == 0:
			turtle.pencolor("blue")
			turtle.fillcolor("blue")
			turtle.goto(positionsx[i], positionsy[i])
		elif sprites_infected[i] >= 1 and sprites_infected[i] <= 3:
			turtle.pencolor("purple")
			turtle.fillcolor("purple")
			turtle.goto(positionsx[i], positionsy[i])
			sprites_infected[i] += 1
		elif sprites_infected[i] > 3 and sprites_infected[i] <= 14:
			turtle.pencolor("red")
			turtle.fillcolor("red")
			turtle.goto(positionsx[i], positionsy[i])
			sprites_infected[i] += 1
		else:
			turtle.pencolor("green")
			turtle.fillcolor("green")
			turtle.goto(positionsx[i], positionsy[i])
   
		
		turtle.pendown()
		turtle.begin_fill()
		turtle.circle(3)
		turtle.end_fill()
		i += 1
		
	sprites_infected_history[n] = infected
	counter.clear()
	counter.write(f"Infected (total): {infected}", font=36)
	turtle.update()
	n += 1
turtle.exitonclick()

plt.plot(list(range(1, N+1)), sprites_infected_history)
plt.title("Total infected over time")
plt.show()















