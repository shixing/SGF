# the additional features that can be derived from PENN
# python penn_features.py s1 ../data/v5/penn/penn.txt
# s1
# s2
#
#
#

from nltk.tree import Tree
import sys
import os

def s1(fn, to_print=True):
    f = open(fn)
    # feature "s1" means the children under the root
    r = []
    for line in f:
        t = Tree.fromstring(line)
        s = t[0]
        labels = []
        for node in s:
            label = node.label()
            if label[0].isalpha():
                labels.append(label)
        l = "_".join(labels)
        r.append(l)
        if to_print:
            print l
        
    return r

def s2(fn):
    # feature "s2" means the children under the root
    # only top 20 labels. 

    r = s1(fn,to_print=False)
    count = {}
    for label in r:
        if not label in count:
            count[label] = 0
        count[label] += 1
    to_sort = []
    for label in count:
        to_sort.append((label,count[label]))
    to_sort = sorted(to_sort,key=lambda x: -x[1])
    topmap = set()
    for i in xrange(min(20,len(to_sort))):
        l, c = to_sort[i]
        topmap.add(l)
    for l in r:
        if l in topmap:
            print l
        else:
            print "Other"
    

    

funcs = {}
funcs['s1'] = s1
funcs['s2'] = s2

def main():
    fn = sys.argv[2]
    func = sys.argv[1]
    if not func in funcs:
        return
    
    funcs[func](fn)
    
if __name__ == '__main__':
    main()
