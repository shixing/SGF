# process the penn treebank corpus
# usage: python corpusPennTreeBank.py <22/23/train> <tree/words>

from nltk.tree import Tree
import os
import sys
from corpusUtil import *

def _list_train(root):
    paths = []
    for name in os.listdir(root):
        path = os.path.join(root,name)
        path = os.path.join(path,"penntree")
        if os.path.isdir(path):            
            paths += _list_dir(path)
    return paths

def _list_dir(dir):
    sys.stderr.write(dir+'\n')
    paths = []
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        if os.path.isfile(path):
            paths.append(path)
    return paths
    



def file2Trees(fn):
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
    return trees


def main():
    corpus_dir = sys.argv[1]
    action = sys.argv[2]
    option = sys.argv[3]
    paths = []
    if action == "train":
        paths = _list_train(corpus_dir)
    
    trees = []

    for path in paths:
        trees += file2Trees(path)
    
    if option == "evalline":
        for tree in trees:
            print tree2line(tree)
    elif option == "words":
        for tree in trees:
            tree2cleantree(tree)
            print tree2words(tree)
    elif option == "trainline":
        for tree in trees:
            tree2cleantree(tree)
            print tree2trainline(tree)
    elif option == "trainwords":
        for tree in trees:
            tree2cleantree(tree)
            print ptb_detokenizer(tree2words(tree))


def test():
    fn = sys.argv[1]
    trees = file2Trees(fn)
    
if __name__ == "__main__":
    main()
    #test()
