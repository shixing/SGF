# The NER feature

from sgf.feature import Feature
import subprocess as sp
import sys
from sgf.util import *
import os

class NER(Feature):
    
    def train(self,mpid,config_fn):            
        config = get_config(config_fn)

        fnin = config.get('sgf','ner_in') 
        fnout = config.get('sgf','ner_out')

        if mpid != None:
            fnin +=  '.' + str(mpid)
            fnout += '.' + str(mpid)
        bash_path = config.get('sgf','ner_sh')

        cmd = 'bash {} {} {}'.format(bash_path,fnin,fnout)
        cmd = cmd.split()
        sp.call(cmd)
        
    
    def stream(self,fnin):
        # [(word,'O'),(word,'MONEY')]
        fin = open(fnin)
        for line in fin:
            ll = line.split()
            yield ll
        fin.close()

if __name__ == "__main__":
    ner = NER()
    #ner.train(128,sys.argv[1])
    ner.train_mpi(sys.argv[1])
    
