# process the penn treebank corpus
# usage: python corpusPennTreeBank.py <22/23/train> <tree/words>

from nltk.tree import Tree
import os
import sys

def _list_train(root):
    paths = []
    for name in os.listdir(root):
        path = os.path.join(root,name)
        if os.path.isdir(path):
            if name == "22" or name == "23":
                continue
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
    temp = ""
    firstTime = True
    while True:
        line  = f.readline()
        if not line:
            break
        line = line.decode("utf8")
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
    if action == "22" or action == "23":
        paths = _list_dir(os.path.join(corpus_dir,action))
    elif action == "train":
        paths = _list_train(corpus_dir)
    
    trees = []
    for path in paths:
        trees += file2Trees(path)
    
    if option == "tree":
        for tree in trees:
            print tree2line(tree)
    elif option == "words":
        for tree in trees:
            print tree2words(tree)


def test():
    fn = sys.argv[1]
    trees = file2Trees(fn)
    
if __name__ == "__main__":
    main()
    #test()
