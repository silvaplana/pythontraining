
################################################
# exo : composition
################################################
print("============== exo : composition ================")


# retrouver la suite de fibonnacci

#a,b,i = 1,1,0
a=1
b=1
i=0

while i<20:
    a ,b, i = b, a+b, i+1
    print (b)
