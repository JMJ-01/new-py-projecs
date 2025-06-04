x= int(input('What is your first number? '))
y= int(input('What is your second number? '))
n= int(input('How many irrerations do you want to run the code? '))

i= 0
lt= [x , y ] 

for i in range (0,n,1):
    z= x+y
    lt.append(z)
    x= y
    y=z
    
print(lt)