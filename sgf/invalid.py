# invalid.py source merged invalid_list
# e.g  python invalid.py data/base/10k.en data/v4/words/words.txt data/base/10k.en.invalid
# The program will merge words.txt.[0-15] to words.txt

import sys
import os

def main():
    fn1 = sys.argv[1]
    fn2 = sys.argv[2]
    fn3 = sys.argv[3]
    
    def get_lines(fn):
        f = open(fn)
        lines = []
        for line in f:
            lines.append(line)
        f.close()
        return lines

    lines1 = get_lines(fn1)
    lines2 = get_lines(fn2)
    
    fout = open(fn3,'w')
    for i in xrange(len(lines1)):
        l1 = lines1[i].split()
        l2 = lines2[i].split()
        if len(l1) == len(l2):
            fout.write('1\n')
        else:
            fout.write('0\n')
    fout.close()
    
if __name__ == "__main__":
    main()
