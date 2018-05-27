'''
FizzBuzz: Output numbers from 1 to x. If the number is divisible by 3, replace it with "Fizz". If 
it is divisible by 5, replace it with "Buzz". If it is divisible by 3 and 5 replace it with "FizzBuzz".
'''

def first_approach(x):
    for n in range(1, x+1):
        out = ''
        if n%3 == 0:
            out += 'Fizz'
        if n%5 == 0:
            out += 'Buzz'
        if out == '':
            out = n
        print out

def second_approach(x):
    out = "\n".join([(
        "Fizz" * (not i%3)
        + "Buzz" * (not i%5)
        + str(i) * (i%3 != 0 and i%5 != 0))
                     for i in range(1, x+1)])
    print out



if __name__ == '__main__':
    print 'First Approach to 15'
    first_approach(15)

    print '\n Second Approach to 15'
    second_approach(15)