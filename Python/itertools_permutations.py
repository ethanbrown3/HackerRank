'''
HackerRank Challenge: itertools.permutations()
Takes a word followed by a postiive int and generates
the permutations of the letters
'''

from itertools import permutations


def word_permutation(word, num):
    '''
    Takes string : word and creates all permuations from the letters in the string
    with a length of int : num
    '''
    permuts = list(permutations(word, int(num)))
    permuts.sort()
    print '\n'.join(''.join(i) for i in permuts)


def main():
    '''
    Entry point
    '''
    word, num = raw_input().split(' ')
    word_permutation(word, num)


if __name__ == '__main__':
    main()
