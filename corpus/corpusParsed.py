# process the penn treebank corpus
# usage: python corpusPennTreeBank.py <22/23/train> <tree/words>

from nltk.tree import Tree
import os
import sys
from corpusUtil import *
from multiprocessing import Pool

def _list_train(root):
    paths = _list_dir(root)
    return paths

def _list_dir(dir):
    sys.stderr.write(dir+'\n')
    paths = []
    for name in os.listdir(dir):
        if not name.startswith("penn.txt"):
            continue
        path = os.path.join(dir,name)
        if os.path.isfile(path):
            paths.append(path)
    return paths
    
def file2Trees(arg):
    fn = arg[0]
    option = arg[1]
    sys.stderr.write(fn+'\n')

    trees = []
    f = open(fn)

    while True:
        line  = f.readline()
        if not line:
            break
        if line == "\n":
            continue
        line = line.decode('utf8')
        tree = Tree.fromstring(line)
        trees.append(tree)
    f.close()
    
    lines = process_tree(trees,option)

    return lines

def process_tree(trees,option):
    lines = []
    if option == "evalline":
        for tree in trees:
            lines.append(tree2line(tree))
    elif option == "words":
        for tree in trees:
            tree2cleantree(tree)
            lines.append( tree2words(tree))
    elif option == "trainline":
        for tree in trees:
            tree2cleantree(tree)
            lines.append( tree2trainline(tree))
    elif option == "trainwords":
        for tree in trees:
            tree2cleantree(tree)
            lines.append(ptb_detokenizer(tree2words(tree)))
    return lines

def main():
    corpus_dir = sys.argv[1]
    action = sys.argv[2]
    option = sys.argv[3]
    paths = []
    if action == "train":
        paths = _list_train(corpus_dir)
    
    ncore = 16
    p = Pool(ncore) # 16 cores
    for i in xrange(0,len(paths),ncore):
        sub_path = paths[i:i+ncore]
        args = [(x,option) for x in sub_path]
        lines_array = p.map(file2Trees, args)
        for lines in lines_array:
            for line in lines:
                print line
        
        
            
        



def test():
    fn = sys.argv[1]
    trees = file2Trees(fn)
    
if __name__ == "__main__":
    main()
    #test()
