#! /bin/bash
# content
# 1. wsj22 words and tree
# 2. wsj23 words and tree
# 3. wsj_train words and tree
# 4. EnglishWebTreeBank words and tree
# 5. OntoNotes words and tree

PY=/home/nlg-05/xingshi/workspace/misc/SGF/corpus/
WSJ=/home/nlg-05/xingshi/workspace/data/treebank2/combined/wsj/
EWTB=/home/nlg-05/xingshi/workspace/data/eng_web_tbk/data/
ONTO=/home/nlg-05/xingshi/workspace/data/ontonotes-release-5.0/data/files/data/english/annotations/
PARSED=/home/nlg-05/xingshi/workspace/misc/SGF/data/v6/penn/

BASE=/home/nlg-05/xingshi/workspace/misc/SGF/data/parse/


python $PY/corpusOntoNotes.py $ONTO train evalline > $BASE/onto.train.evalb
: <<'END'

python $PY/corpusPennTreeBank.py $WSJ 22 evalline > $BASE/wsj.22.evalb
python $PY/corpusPennTreeBank.py $WSJ 22 words > $BASE/wsj.22.word
python $PY/corpusPennTreeBank.py $WSJ 22 trainwords > $BASE/wsj.22.trainwords
python $PY/corpusPennTreeBank.py $WSJ 22 trainline > $BASE/wsj.22.trainline

python $PY/corpusPennTreeBank.py $WSJ 23 evalline > $BASE/wsj.23.evalb
python $PY/corpusPennTreeBank.py $WSJ 23 words > $BASE/wsj.23.words
python $PY/corpusPennTreeBank.py $WSJ 23 trainwords > $BASE/wsj.23.trainwords
python $PY/corpusPennTreeBank.py $WSJ 23 trainline > $BASE/wsj.23.trainline

python $PY/corpusPennTreeBank.py $WSJ train trainline > $BASE/wsj.train.trainline
python $PY/corpusPennTreeBank.py $WSJ train words > $BASE/wsj.train.words
python $PY/corpusPennTreeBank.py $WSJ train trainwords > $BASE/wsj.train.trainwords

python $PY/corpusEnglishWebTreeBank.py $EWTB train trainline > $BASE/ewtb.train.trainline
python $PY/corpusEnglishWebTreeBank.py $EWTB train words > $BASE/ewtb.train.words
python $PY/corpusEnglishWebTreeBank.py $EWTB train trainwords > $BASE/ewtb.train.trainwords

python $PY/corpusOntoNotes.py $ONTO train trainline > $BASE/onto.train.trainline
python $PY/corpusOntoNotes.py $ONTO train words > $BASE/onto.train.words
python $PY/corpusOntoNotes.py $ONTO train trainwords > $BASE/onto.train.trainwords

python $PY/corpusParsed.py $PARSED train trainline > $BASE/8m.train.trainline
python $PY/corpusParsed.py $PARSED train trainwords > $BASE/8m.train.trainwords

END
