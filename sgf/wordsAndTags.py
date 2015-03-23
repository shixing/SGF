# Split a big file into multiple files:
#       tokenize
#       split sentences
#       POS tags
# Output:
#       One sentence per line. 

from sgf.feature import Feature
import subprocess as sp
import sys
from sgf.util import *
import os

class WordsAndTags(Feature):
    
    def train(self,mpid,config_fn):            
        config = get_config(config_fn)

        fnin = config.get('sgf','word_in') 
        fnout = config.get('sgf','word_out')
        posout = config.get('sgf','pos_out')
        bash_path = config.get('sgf','pos_sh')
        
        if mpid != None:
            fnout += '.' + str(mpid)
            posout += '.' + str(mpid)

        npid = config.getint('sgf','word_npid')
        fin = open(fnin)
        fntmp = fnout + '.tmp'
        ftmp = open(fntmp,'w')
        iline = 0
        for line in fin:
            if iline % npid == mpid:
                ftmp.write(line)
            iline += 1
        ftmp.close()

        # POS tags
        fntmppos = fntmp + '.pos'
        cmd = 'bash {} {} {}'.format(bash_path,fntmp,fntmppos)
        cmd = cmd.split()
        sp.call(cmd)
        os.remove(fntmp)

        #Split words and tags
        fout = open(fnout,'w')
        fpos = open(posout,'w')
        ftmppos = open(fntmppos)
        for line in ftmppos:
            ll = line.split()
            words =' '.join(['/'.join(x.split('/')[:-1]) for x in ll])
            pos = ' '.join([x.split('/')[-1] for x in ll])
            fout.write(words+'\n')
            fpos.write(pos+'\n')
        ftmppos.close()
        os.remove(fntmppos)

    
    def stream(self,fnin):
        fin = open(fnin)
        for line in fin:
            ll = line.split()
            yield ll
        fin.close()

if __name__ == "__main__":
    wt = WordsAndTags()
    wt.train_mpi(sys.argv[1])
