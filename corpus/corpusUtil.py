# -*- coding: utf-8 -*-

from nltk.tree import Tree

# because of a bug, parenthesis was removed

def add_parenthesis_on_tree(tree):
    def post_order(node):
        if type(node) == str:
            return
        if node.height() == 2:
            if node.label() == "PRN":
                node.insert(0,"-BR-")
                node.append("-BR-")
            return
        
        if node.height() > 2:
            for child in node:
                post_order(child)
        
            if node.label() == "PRN":
                node.insert(0,"-BR-")
                node.append("-BR-")
    post_order(tree)
    return tree


def tree2words(tree):
    r = u" ".join(tree.leaves())
    return r.encode('utf8')

def tree2line(tree):
    tree.set_label("TOP")
    a = tree.pformat()
    a = u" ".join(a.split())
    return a.encode('utf8')

def trainline2tree(line,words):
    ll = line.split()
    newll = []

    for word in ll:
        if word.startswith(")"):
            newll.append(")")
        else:
            newll.append(word)
            
    try:
        tree = Tree.fromstring(" ".join(newll))
    except:
        return "malform"
    if words == None:
        return tree

    #if len(tree.leaves()) != len(words):
    #    add_parenthesis_on_tree(tree)

    if len(tree.leaves()) != len(words):
        tree.pretty_print()
        print words
        return "wrong length"

    
    new_tree = tree.copy()
    for i in xrange(len(words)):
        tp = tree.leaf_treeposition(i)
        node = new_tree[tp[:-1]]
        leaf = new_tree[tp]
        if leaf == "-BR-":
            leaf = words[i]
        leafnode = Tree(leaf,[words[i]])
        node[tp[-1]] = leafnode
    
    return new_tree


def tree2trainline(tree):
    def _s(node):
        if node.height() == 2:
            return node.label()
        label = node.label()
        child_string = ["({}".format(label)]
        for child in node:
            child_string.append(_s(child))
        child_string.append("){}".format(label))
        return " ".join(child_string)
    
    return _s(tree)
        

def tree2cleantree(tree):
    # set top label TOP
    tree.set_label("TOP")
    # remove everay functional tags
    # recursively remove tags_to_remove
    tag_to_remove = ["-NONE-"]

    def post_order(node):
        label = node.label()
        if label in tag_to_remove:
            return True

        remove_this_node = False

        if node.height() >=3:
            to_remove = []
            nodes = []
            for child in node:
                to_remove.append(post_order(child))
                nodes.append(child)
            for i in xrange(len(to_remove)):
                if to_remove[i]:
                    node.remove(nodes[i])
            if len(node) == 0:
                remove_this_node = True

        index_dash = label.find("-")
        index_equal = label.find("=")
        end = len(label)
        if index_dash > 0 and index_dash < end:
            end = index_dash
        if index_equal > 0 and index_equal < end:
            end = index_equal
        new_label = label[0:end]
        node.set_label(new_label)
        return remove_this_node
        
    post_order(tree)
    
    return tree
    
ptb_map = {"''":'&quot;',
           "``":'&quot;',
           "-LRB-":"(",
           "-RRB-":")",
           "-LSB-":"&#91;",
           "-RSB-":"&#93;",
           "-LCB-":"{",
           "-RCB-":"}",
           '|':"&#124;",
           ">":"&gt;",
           "<":"&lt;",
           "&":"&amp;",
           }


            
def ptb_detokenizer(line):

    if type(line) != unicode:
        line = line.decode("utf8")
    words = line.split()
    newll = []

    for word in words:
        final_word = ""
        
        if word in ptb_map:
            final_word = ptb_map[word]
        else:
            word = word.replace("'","&apos;")
            if word == "n&apos;t" and len(newll) > 0:
                newll[-1] += "n"
                word = "&apos;t"
            final_word = word
            
        newll.append(final_word)
    
    r = u" ".join(newll)
    return r.encode('utf8')
        
    
    
    
