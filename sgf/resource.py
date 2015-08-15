
from sgf.util import *
from sgf.mpi_framework import mpi_call

class Resource:
    
    def load(self,config_fn):
        pass

    def load_default(self):
        config_fn = "/Users/xingshi/Workspace/misc/SGF/config.cfg"
        return self.load(config_fn)
