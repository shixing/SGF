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

    def line2DAG(self,line):
        #build a DAG from line
        # dag = {(word,index):[(edge,(word,index))]}
        #
        # line = "nsubj(love-2,I-1) root(ROOT-0,love-2) dobj(love-2,you-3)"

        dag = {}
        ll = line.split()
        def rightdash(s):
            for i in xrange(len(s)-1,-1,-1):
                if s[i] == '-':
                    return i
        for dep in ll:
            il,ir,ic = 0,0,0
            for i in xrange(len(dep)):
                if dep[i] == '(':
                    il = i
                if dep[i] == ')':
                    ir = i
                if dep[i] == ',':
                    ic = i
            edge = dep[0:il]
            head = dep[il+1:ic]
            child = dep[ic+1:ir]
            ihd = rightdash(head)
            icd = rightdash(child)
            hword = head[0:ihd]
            hindex = head[ihd+1:]
            cword = child[0:icd]
            cindex = child[icd+1:]
            if (hword,hindex) not in dag:
                dag[(hword,hindex)] = []
            dag[(hword,hindex)].append((edge,(cword,cindex)))
        
        return dag


if __name__ == "__main__":
    dep = Dependency()
    dep.train_mpi(sys.argv[1])
    
