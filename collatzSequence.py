def collatz(number):
    if number%2==0:
        number=number//2
    else:
        number=3*number+1
    print(number)
    return number
print('enter an integer')
num=int(input())
a=0
a=collatz(num)
while a!=1:
    a=collatz(a)

print(a/2)
print(a//2)
