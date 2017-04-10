# Split a big file into multiple files:
#       do not tokenize
#       each line is a sentence
#       
# Output:
#       One sentence per line. 

from sgf.feature import Feature
import subprocess as sp
import sys
from sgf.util import *
import os

class SplitFile(Feature):
    
    def train(self,mpid,config_fn):            
        config = get_config(config_fn)

        fnin = config.get('sgf','word_in') 
        fnout = config.get('sgf','word_out')
        
        #fdir = os.path.dirname(os.path.abspath(fnout))
        #os.mkdir(fdir)
        
        if mpid != None:
            fnout += '.' + str(mpid)

        npid = config.getint('sgf','word_npid')
        fin = open(fnin)
        fout = open(fnout,'w')
        iline = 0
        for line in fin:
            if iline % npid == mpid:
                fout.write(line)
            iline += 1
        fout.close()
        fin.close()

    def stream(self,fnin):
        fin = open(fnin)
        for line in fin:
            ll = line.split()
            yield ll
        fin.close()

if __name__ == "__main__":
    wt = SplitFile()
    wt.train_mpi(sys.argv[1])
