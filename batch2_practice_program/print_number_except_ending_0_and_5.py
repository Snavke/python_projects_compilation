# use for loop to create range from 1-100
for i in range (0,100):
# filter out numbers ending by 0 and 5 by using modulus by 5, if returned 0, then it is a number ending either in 5 or 0
    if i % 5 != 0:
# print number except ending 0 and 5
        print (i)