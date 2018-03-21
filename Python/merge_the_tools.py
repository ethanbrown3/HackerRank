# https://www.hackerrank.com/challenges/merge-the-tools/copy-from/68183439

def merge_the_tools(string, k):
    for x in range(0, len(string), k):
        out = string[x:x+k]
        print ''.join(sorted(set(out), key=out.index))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)