#fizzbuzz with a while loop
x= 1
while x <=100:
    if x % 3== 0 and x % 5 ==0:
        print ('fizzbuzz')
    elif x % 3==0:
        print('fizz')
    elif x % 5 == 0:
        print('buzz')
    elif x % 5 !=0 and x% 3!=0:
        print(x)
    x += 1
    
  
# execute fizzbuzz with a for loop, taking out some lines of code
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i) 
