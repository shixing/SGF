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

        fntmp = fnout+'.tmp'
        cmd = 'bash {} {} {}'.format(bash_path,fnin,fntmp)
        cmd = cmd.split()
        sp.call(cmd)
        
        # reformat the output
        # NER will split the sentence in a different way, so everything is according to words
        ftmp = open(fntmp)
        fout = open(fnout,'w')
        fin = open(fnin)
        for wordsline in fin:
            ner = []
            while len(ner) != len(wordsline.split()):
                if len(ner) > len(wordsline.split()):
                    raise Exception
                line = ftmp.readline()
                ll = line.split()
                ner += [x.split('/')[-1] for x in ll]
            fout.write(' '.join(ner)+"\n")

        fin.close()
        ftmp.close()
        fout.close() 
        os.remove(fntmp)


    
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
    
