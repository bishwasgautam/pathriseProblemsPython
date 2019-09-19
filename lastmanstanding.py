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