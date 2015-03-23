from sgf.util import *
from sgf.resource import Resource

class VerbTense(Resource):
    
    def load(self,config_fn):
        config = get_config(config_fn)
        tense_fn = config.get('sgf','verb_tense_file')
        f = open(tense_fn)
        tense_dict = {}
        for line in f:
            j = json.loads(line)
            words = j['words']
            stem = j['stem']
            synt = j['synt']
            if not synt in ['S-VERB']:
                continue
            for word in words:
                tense_dict[word] = stem
        f.close()
        return tense_dict

    
