# the general feature class

from sgf.util import *
from sgf.mpi_framework import mpi_call

class Feature:
    
    def train_mpi(self,config_fn):
        mpi_call(config_fn,self)
        
    def train(self,mpid,config_fn):
        pass

    def load(self,fnin):
        # return list a results
        return list(self.stream(fnin))
        pass

    def stream(self,fnin):
        # yield results one by one
        pass

    
