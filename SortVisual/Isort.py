# importing pygame 
import pygame
import numpy as np

pygame.init() 

# setting window size 
win = pygame.display.set_mode((800, 550)) 

# setting title to the window 
pygame.display.set_caption("insertion sort") 

# initial position 
x = 20
y = 20

# width of each bar 
width = 3
#('choose the random distribution: 1.gaussian  2.uniform')
#1.gaussian
##height = np.random.normal(10, 200, 150) 
##height = [abs(i) for i in height]

#2.uniform
height = np.arange(1,150,1)
np.random.shuffle(height)


# height of each bar (data to be sorted) 

M = max(height)
height = [int((i/M)*500) for i in height]

M = max(height)


run = True

# method to show the list of height 
def show(height): 

	# loop to iterate each item of list 
	for i in range(len(height)): 

		# drawing each bar with respective gap 
		pygame.draw.rect(win, (int((height[i]/M)*255), 0, 150), (x + 5 * i, y, width, height[i])) 

# infinite loop 
while run: 

	# execute flag to start sorting 
	execute = False

	# time delay 
	pygame.time.delay(10) 

	# getting keys pressed 
	keys = pygame.key.get_pressed() 

	# iterating events 
	for event in pygame.event.get(): 

		# if event is to quit 
		if event.type == pygame.QUIT: 

			# making run = false so break the while loop 
			run = False

	# if space bar is pressed 
	if keys[pygame.K_SPACE]: 
		# make execute flag to true 
		execute = True

	# checking if execute flag is false 
	if execute == False: 

		# fill the window with black color 
		win.fill((135, 206, 235)) 

		# call the height method to show the list items 
		show(height) 

		# update the window 
		pygame.display.update() 

	# if execute flag is true 
	else: 

		# start sorting using bubble sort technique 
		for i in range(1,len(height)): 
			key = height[i]
			# after this iteration max element will come at last 
			j = i - 1
			while j>= 0 and key < height[j]: 
				#min_idx = i
				# starting is greater then next element 
				height[j+1] = height[j] 
				j -= 1      	 
					 
			height[j+1] = key		 

			# fill the window with black color 
			win.fill((135, 206, 235)) 

			# call show method to display the list items 
			show(height) 

			# create a time delay 
			pygame.time.delay(50) 

			# update the display 
			pygame.display.update() 

# exiting the main window 
pygame.quit() 
