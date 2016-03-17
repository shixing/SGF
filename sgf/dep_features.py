# the additional features that can be derived from DEP
# python penn_features.py s1 ../data/v5/penn/penn.txt
# abspos
# relpos
#
#
#

import re
import sys
import os

invalid_number = 12345

def abspos(fn,fnwords, to_print=True, relative=False):
    f = open(fn)
    fwords = open(fnwords)
    
    p = re.compile(r'.+\(.+-([0-9]+)\'?,.+-([0-9]+)\'?\)')
    while True:
        depline = f.readline()
        line = fwords.readline()
        if not line:
            break
        words = line.split()
        depwords = depline.split()

        deps = {}
        # parse deps
        for depword in depwords:
            print >> sys.stderr, depword
            m = p.match(depword)
            head = int(m.group(1))
            current = int(m.group(2))
            deps[current] = head
            if relative:
                deps[current] = head - current

        r = []
        for i in xrange(1, len(words)+1):
            if i in deps:
                r.append(str(deps[i]))
            else:
                r.append(str(invalid_number))
            
        print " ".join(r)
        
        
def relpos(fn,fnwords, to_print=True):
    abspos(fn,fnwords,to_print,relative = True)

        

    

funcs = {}
funcs['abs'] = abspos
funcs['rel'] = relpos

def main():
    fn = sys.argv[2]
    fnwords = sys.argv[3]
    func = sys.argv[1]
    if not func in funcs:
        return
    
    funcs[func](fn,fnwords)
    
if __name__ == '__main__':
    main()
