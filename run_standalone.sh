# tokenize and split sentence and pos tagging
mpiexec -n 4 python -m sgf.wordsAndTags config/config.cfg
# NER
mpiexec -n 4 python -m sgf.ner config/config.cfg
# dependency parsing
mpiexec -n 4 python -m sgf.dependency config/config.cfg
# constitutional parsing
mpiexec -n 4 python -m sgf.penn config/config.cfg

