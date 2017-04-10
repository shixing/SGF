# process the penn treebank corpus
# usage: python corpusPennTreeBank.py <22/23/train> <tree/words>

from nltk.tree import Tree
import os
import sys
from corpusUtil import *

def _list_train(root):
    # root should be ..../annotations/
    paths = []
    for name0 in os.listdir(root):
        path0 = os.path.join(root,name0)
        if os.path.isdir(path0): # level of bc
            for name1 in os.listdir(path0):
                path1 = os.path.join(path0,name1)
                if name1 == 'wsj':
                    continue
                if os.path.isdir(path1): # level of cctv
                    for name2 in os.listdir(path1):
                        path2 = os.path.join(path1,name2)
                        if os.path.isdir(path2):
                            paths += _list_dir(path2)
    return paths

def _list_dir(dir):
    sys.stderr.write(dir+'\n')
    paths = []
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        if os.path.isfile(path):
            if path.endswith("parse"):
                paths.append(path)
    return paths
    

def file2Trees(fn):
    trees = []
    f = open(fn)
    temp = ""
    firstTime = True
    while True:
        line  = f.readline()
        if not line:
            break
        line = line.decode('utf8')
        if line[0] == "(" :
            if not firstTime:
                temp = temp.replace("\n","")
                tree = Tree.fromstring(temp)
                trees.append(tree)
                temp = ""
            firstTime = False
        temp += line   
    if temp != "":
        temp = temp.replace("\n","")
        tree = Tree.fromstring(temp)
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
