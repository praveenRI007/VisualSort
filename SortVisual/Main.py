import os
import sys
print("Hi ! iam  a program for visualising the sorting algorithms:\n")
print("choose the below choices for viewing the sorting algorithms:\n")
print("1.Binary Sort")
print("2.Insertion Sort")
print("3.Merge Sort")
print("4.Quick Sort")
print("5.Selection Sort")
print('6.exit')

A = 1

while A:
    print("\nEnter your choice:\t")
    C = int(input())
    A = 0
    if C == 1:
        os.system('python BSort.py')
    elif C == 2:
        os.system('python Isort.py')
    elif C == 3:
        os.system('python Msort.py')
    elif C == 4:
        os.system('python Qsort.py')
    elif C == 5:
        os.system('python SSort.py')
    elif C == 6:
        sys.exit()

    print("do you wish to enter another choice (which has new randomised values) ?(y/n)")
    A = input()
    if A == 'Y' or A == 'y':
        continue
    else:
        sys.exit()
        

    


