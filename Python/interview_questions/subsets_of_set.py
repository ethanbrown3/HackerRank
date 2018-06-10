'''
https://www.youtube.com/watch?v=bGC2fNALbNU&t=90s
print out all subsets of a set.
example:
    input: [1, 2]

    output:
        { }
        {1}
        {2}
        {1, 2}

2**n subsets
'''

def find_subsets(given_array):
    subset = [i for i in range(len(given_array))]
    _helper(given_array, subset, 0)

def _helper(given_array, subset, i):
    if i == len(given_array):
        print_array(subset)
    else:
        subset[i] = None
        _helper(given_array, subset, i+1)
        subset[i] = given_array[i]
        _helper(given_array, subset, i+1)

def print_array(array):
    print ','.join([str(i) for i in array if i != None])

if __name__ == '__main__':
    main_set = raw_input('Enter space seperated set: ').split()
    
    find_subsets(main_set)
