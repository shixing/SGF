from sgf.util import *
from sgf.resource import Resource

import json

class MweList(Resource):
    
    def load(self, config_fn):
        config = get_config(config_fn)
        mwe_list_fn = config.get('sgf','mwe_list_file')
        
        mwes = {}
        f = open(mwe_list_fn)
        for line in f:
            j = json.loads(line)
            pid = int(j['pid'])
            mwes[pid] = j
        f.close()
        
        return mwes
