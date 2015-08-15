# locate multiple phrases in a given sentences.


import sys
import json
from collections import deque

def build_tree(phrase_fn):
    f = open(phrase_fn)
    tree = {}
    phrases = []
    for line in f:
        j = json.loads(line)
        words = j['lemmas']
        pid = int(j['pid'])
        phrases.append(tuple(words))
        local_tree = tree
        for word in words:
            if not word in local_tree:
                local_tree[word] = {}
            local_tree = local_tree[word]
        local_tree['_pid_'] = pid
    f.close()
    return tree,phrases


def build_tense_dict(tense_fn,synts):
    
    f = open(tense_fn)
    tense_dict = {}
    for line in f:
        j = json.loads(line)
        words = j['words']
        stem = j['stem']
        synt = j['synt']
        if not synt in synts:
            continue
        for word in words:
            tense_dict[word] = stem
    f.close()
    return tense_dict

def _wildcard(word,local_tree):
    wcs = []
    if 'someone' in local_tree:
        if word in ['him','us','it','her','me','you','them']:
            wcs.append('someone')
    if "one's" in local_tree:
        if word in ["'s",'my','your','their','our','his','her','its']:
            wcs.append("one's")
    if "oneself" in local_tree:
        if word in ['himself','herself','itself','oneself','themself','yourself','myself','ourself']:
            wcs.append("oneself")
    return wcs


def search(sentence,tree,max_other_words,tense_dict):
    # sentence : ['this','is','a','sentence']
    #            sentence should be lower cased
    # return [(phrase_id,[idx1,idx2,idx3]),...]
    m = max_other_words
    results = []

    for i in xrange(len(sentence)):
        nskip = 0
        current = i
        local_tree = tree
        idxs = []
        queue = deque()
        
        word = sentence[current]
        if word in local_tree:
            queue.append((local_tree[word],current+1,nskip,[current]))
        wcs = _wildcard(word,local_tree)
        if wcs:
            for wc in wcs:
                queue.append((local_tree[wc],current+1,nskip,[current]))
        if word in tense_dict:
            stem = tense_dict[word]
            if stem != word and stem in local_tree:
                queue.append((local_tree[stem],current+1,nskip,[current]))
                
        while len(queue) > 0:
            local_tree, current, nskip, idxs = queue.popleft()
            
            if nskip > m:
                continue

            if '_pid_' in local_tree and current == idxs[-1]+1:
                pid = local_tree['_pid_']
                results.append((pid,tuple(idxs)))

            if current >= len(sentence):
                continue
            
            if len(local_tree) == 1 and '_pid_' in local_tree:
                continue

            word = sentence[current]
            
            if word in local_tree:
                queue.append((local_tree[word],current+1,nskip,idxs+[current,]))
            wcs = _wildcard(word,local_tree)

            if wcs:
                for wc in wcs:
                    queue.append((local_tree[wc],current+1,nskip,idxs + [current,]))

            if word in tense_dict:
                stem = tense_dict[word]
                if stem != word and stem in local_tree:
                    queue.append((local_tree[stem],current+1,nskip,idxs+[current,]))
            
            queue.append((local_tree,current+1,nskip+1,list(idxs)))

            
    return results


def get_searcher(phrase_fn,tense_fn):
    
    #phrase_fn = config.get('path','phrase_file')
    #tense_fn = config.get('path','tense_file')
    
    tree,phrases = build_tree(phrase_fn)
    synts = ['S-VERB','S-NOUN','S-INTR-VERB','S-TR-VERB','S-PSEUDO-PASSIVIZING-VERB','S-DITR-VERB']
    tense_dict = build_tense_dict(tense_fn,synts)
    
    searcher = lambda x,y: search(x,tree,y,tense_dict)
    return searcher, phrases





def test():
    phrase_fn = sys.argv[1]
    data_fn = sys.argv[2]
    tense_fn = sys.argv[3]
    
    tree,phrases = build_tree(phrase_fn)
    synts = ['S-VERB','S-NOUN','S-INTR-VERB','S-TR-VERB','S-PSEUDO-PASSIVIZING-VERB','S-DITR-VERB']
    tense_dict = build_tense_dict(tense_fn,synts)
    
    sentence = "I will catch yourself up"
    results =  search(sentence.split(),tree,2,tense_dict)
    print results
    for r in results:
        print phrases[r[0]]
if __name__ == "__main__":
    test()
    
