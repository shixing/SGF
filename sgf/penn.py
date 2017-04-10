# The PENN feature: constituional parser tree using stanford parser

from sgf.feature import Feature
import subprocess as sp
import sys
from sgf.util import *
import os

class Penn(Feature):
    
    def train(self,mpid,config_fn):  
        # speed: 1.42 sentence / sec

        config = get_config(config_fn)

        fnin = config.get('sgf','penn_in') 
        fnout = config.get('sgf','penn_out')

        if mpid != None:
            fnin +=  '.' + str(mpid)
            fnout += '.' + str(mpid)
        bash_path = config.get('sgf','penn_sh')

        # stanford-parser
        fntmp = fnout+'.tmp'
        cmd = 'bash {} {} {}'.format(bash_path,fnin,fntmp)
        cmd = cmd.split()
        sp.call(cmd)
        
        # reformat the output
        ftmp = open(fntmp)
        fout = open(fnout,'w')
        
        while True:
            line = ftmp.readline()
            if line == '':
                break
            line = line.strip()
            if line == '(())' or line == 'SENTENCE_SKIPPED_OR_UNPARSABLE':
                fout.write("\n")
            else:
                # process the buffer
                fout.write(line+'\n')

        ftmp.close()
        fout.close() 
        os.remove(fntmp)

if __name__ == "__main__":
    penn = Penn()
    #penn.train(3,sys.argv[1])
    penn.train_mpi(sys.argv[1])
    
