# merge.py folder prefix number
# e.g merge.py words/ words.txt 15
# The program will merge words.txt.[0-15] to words.txt

import sys
import os

def main():
    folder = sys.argv[1]
    prefix = sys.argv[2]
    n  = int(sys.argv[3])
    
    
    lines = []
    for i in xrange(n):
        fin = open(os.path.join(folder, "{}.{}".format(prefix,i)))
        lines.append([])
        for line in fin:
            lines[i].append(line)
        fin.close()

    fout = open(os.path.join(folder,prefix),'w')
    k = 0
    to_break = False
    while True:
        if to_break:
            break
        to_break = True
        for i in xrange(n):
            if k >= len(lines[i]):
                continue
            to_break = False
            fout.write(lines[i][k])
        k += 1
    fout.close()

if __name__ == "__main__":
    main()
