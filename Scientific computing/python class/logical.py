x=10
y=5
print(x==y)
x=10
y=10
print(x!=y)
test1=eval(input('Enter Score in Test-I'))
test2=eval(input('Enter Score in Test-II'))
test3=eval(input('Enter Score in test-III'))
average=(test1+test2+test3)/3
print('Your Average score is:',average)
if average>90:
    print('Congratulations on a High Average')

x=eval(input('Enter a number'))
if (x%2==0):
    print('Even number')
x=eval(input('Enter a number'))
y=eval(input('Enter a number'))
if (x-y) <= 10:
    print('Entered numbers are  closed')
else: 
    print('Entered numbers are not closed')