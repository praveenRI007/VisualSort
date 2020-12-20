# importing pygame 
import pygame
import numpy as np

pygame.init() 

# setting window size 
win = pygame.display.set_mode((800, 550)) 

# setting title to the window 
pygame.display.set_caption("merge sort") 

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
            def merge(height, l, m, r): 
                    n1 = m - l + 1
                    n2 = r- m 

                    # create temp heightays 
                    L = [0] * (n1) 
                    R = [0] * (n2) 

                    # Copy data to temp heightays L[] and R[] 
                    for i in range(0 , n1): 
                            L[i] = height[l + i] 

                    for j in range(0 , n2): 
                            R[j] = height[m + 1 + j] 

                    # Merge the temp heightays back into height[l..r] 
                    i = 0	 # Initial index of first subheightay 
                    j = 0	 # Initial index of second subheightay 
                    k = l	 # Initial index of merged subheightay 

                    while i < n1 and j < n2 : 
                            if L[i] <= R[j]: 
                                    height[k] = L[i] 
                                    i += 1
                            else: 
                                    height[k] = R[j] 
                                    j += 1
                            k += 1
                            

                    # Copy the remaining elements of L[], if there 
                    # are any 
                    while i < n1: 
                            height[k] = L[i] 
                            i += 1
                            k += 1

                    # Copy the remaining elements of R[], if there 
                    # are any 
                    while j < n2: 
                            height[k] = R[j] 
                            j += 1
                            k += 1

                    # fill the window with black color 
                    win.fill((135, 206, 235))
                    # call show method to display the list items 
                    show(height)
                    # create a time delay 
                    pygame.time.delay(75)
                    # update the display 
                    pygame.display.update()    

                   
            # l is for left index and r is right index of the 
            # sub-heightay of height to be sorted 
            def mergeSort(height,l,r): 
                    if l < r: 

                            # Same as (l+r)//2, but avoids overflow for 
                            # large l and h 
                            m = (l+(r-1))//2

                            # Sort first and second halves 
                            mergeSort(height, l, m) 
                            mergeSort(height, m+1,r) 
                            merge(height, l, m, r)
                            
            mergeSort(height,0,len(height)-1)
# exiting the main window 
pygame.quit() 
