# The DEP feature

from sgf.feature import Feature
import subprocess as sp
import sys
from sgf.util import *
import os

class Dependency(Feature):
    
    def train(self,mpid,config_fn):  
        # speed: 1.42 sentence / sec
          
        config = get_config(config_fn)

        fnin = config.get('sgf','dep_in') 
        fnout = config.get('sgf','dep_out')

        if mpid != None:
            fnin +=  '.' + str(mpid)
            fnout += '.' + str(mpid)
        bash_path = config.get('sgf','dep_sh')

        # stanford-parser
        fntmp = fnout+'.tmp'
        cmd = 'bash {} {} {}'.format(bash_path,fnin,fntmp)
        cmd = cmd.split()
        sp.call(cmd)
        
        # reformat the output
        ftmp = open(fntmp)
        fout = open(fnout,'w')
        
        buf = []
        while True:
            line = ftmp.readline()
            if line == '':
                if len(buf) > 0:
                    fout.write(' '.join(buf)+'\n')
                break
            line = line.strip()
            if line == '(())' or line == 'SENTENCE_SKIPPED_OR_UNPARSABLE':
                fout.write("\n")
            elif line == '':
                # process the buffer
                fout.write(' '.join(buf)+'\n')
                buf = []
            else:
                buf.append(line.replace(' ',''))

        ftmp.close()
        fout.close() 
        os.remove(fntmp)


if __name__ == "__main__":
    dep = Dependency()
    dep.train_mpi(sys.argv[1])
    
