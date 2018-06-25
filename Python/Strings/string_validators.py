'''
https://www.hackerrank.com/challenges/string-validators/problem
Python has built-in string validation methods
isalnum()
isalpha()
isdigit()
islower()
isupper()
'''

if __name__ == '__main__':
    st = raw_input()
    print any(s.isalnum() for s in st)
    print any(s.isalpha() for s in st)
    print any(s.isdigit() for s in st)
    print any(s.islower() for s in st)
    print any(s.isupper() for s in st)