# mwe features


from sgf.feature import Feature
from sgf.mweList import MweList
import subprocess as sp
import sys
from sgf.util import *
import os
from sgf.mwe_search import get_searcher

class Mwe(Feature):
    
    def train(self,mpid,config_fn):
        
        config = get_config(config_fn)

        fnin = config.get('sgf','mwe_in') 
        fnout = config.get('sgf','mwe_out')

        if mpid != None:
            fnin +=  '.' + str(mpid)
            fnout += '.' + str(mpid)
        
        fin = open(fnin)
        fout = open(fnout,'w')
            
        phrase_fn = config.get('sgf','mwe_list_file')
        verb_tense_fn = config.get('sgf','verb_tense_file')
        
        searcher, _ = get_searcher(phrase_fn,verb_tense_fn)
        
        # the gap that a mwe can have
        max_gap = 0
        for line in fin:
            sentence = line.split()
            res = searcher(sentence,max_gap)
            fout.write(json.dumps(res)+'\n')
            
        fin.close()
        fout.close()
        

if __name__ == "__main__":
    mwe = Mwe()
    mwe.train_mpi(sys.argv[1])
