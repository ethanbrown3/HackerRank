# https://www.hackerrank.com/challenges/capitalize/problem

# first solution
# Complete the solve function below.
'''
def solve(s):
    out = ''
    is_new_word = True
    for c in s:
        if c == ' ':
            out += ' '
            is_new_word = True
        elif is_new_word:
            out += c.capitalize()
            is_new_word = False
        else:
            out += c
    return str(out)
'''

def solve(s):
    for x in s[:].split(): # split string into list and iterate through words
        s = s.replace(x, x.capitalize()) # replace words with capitalized ones in string
    return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
