'''

Last Man Standing
A king gathers all the men in the kingdom who are to be put to death for their crimes, but because of his mercy, he will pardon one. He gathers the men into a circle and gives the sword to one man. The man kills the man to his left, and gives the sword to the man to the dead man's left. The last man alive is pardoned. 

With 5 men, the 3rd is the last man alive. 

Write a program that accepts a single parameter: a number N that represents the number of criminals to start with. The program should output the number of the last two men alive.

Example #1: myProgram 5

would output:

5, 3

Example #2: myProgram 7

would output:

3, 7
'''


def last_man_standing(num):
    
    #define the cirlce
    circle_criminals = list(range(1,num + 1))
    
    while len(circle_criminals) > 2: # as long as there are two survivors
        
        #start from the first criminal
        standing = circle_criminals[0] 
        circle_criminals.pop(0) #remove the standing one from the front
        circle_criminals.append(standing) #add survivor to the end of the circle so next one alive gets the sword
        circle_criminals.pop(0) #remove the next one who is killed

    #display last 2 winners
    print(str(circle_criminals[1]) + "," + str(circle_criminals[0]))



last_man_standing(7) # output 3, 7
last_man_standing(5) # output 5, 3
last_man_standing(2) # output 2, 1