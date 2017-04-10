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

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),"../corpus/"))

from corpusUtil import *

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

def sln(fn,level):
    f = open(fn)
    
    for line in f:
        res = []
        tree = Tree.fromstring(line)
        tree = tree2cleantree(tree)
        nleaf = len(tree.leaves())
        for i in xrange(nleaf):
            pt = tree.leaf_treeposition(i)
            if len(pt) >= level + 1:
                pt = pt[:-level]
                label = tree[pt].label()
                if label == "S":
                    label = "-"
                res.append(label)
            else:
                res.append("-")
        print " ".join(['-'] + res[::-1])
    f.close()

def sln_last(fn,level):
    f = open(fn)
    
    for line in f:
        res = []
        tree = Tree.fromstring(line)
        tree = tree2cleantree(tree)
        nleaf = len(tree.leaves())
        father_positions = []

        for i in xrange(nleaf):
            pt = tree.leaf_treeposition(i)
            if len(pt) >= level + 1:
                pt = pt[:-level]
                label = tree[pt].label()
                if label == "S":
                    label = "-"
                if len(father_positions) > 0: 
                    if pt == father_positions[-1]:
                        label = "-"
                res.append(label)
                father_positions.append(pt)
            else:
                res.append("-")
                father_positions.append(None)
            
        print " ".join(['-'] + res[::-1])
        
    f.close()



def sl1(fn):
    sln(fn,1)

def sl2(fn):
    sln(fn,2)

def sl3(fn):
    sln(fn,3)
    
def sl4(fn):
    sln(fn,4)

def sl2_last(fn):
    sln_last(fn,2)

def sl3_last(fn):
    sln_last(fn,3)

def sl4_last(fn):
    sln_last(fn,4)
    

funcs = {}
funcs['s1'] = s1
funcs['s2'] = s2
funcs['sl1'] = sl1
funcs['sl2'] = sl2
funcs['sl3'] = sl3
funcs['sl4'] = sl4
funcs['sl2_last'] = sl2_last
funcs['sl3_last'] = sl3_last
funcs['sl4_last'] = sl4_last


def main():
    fn = sys.argv[2]
    func = sys.argv[1]
    if not func in funcs:
        return
    
    funcs[func](fn)
    
if __name__ == '__main__':
    main()
