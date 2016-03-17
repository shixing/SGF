
source=../data/base/43.en
invalid=../data/base/43.en.invalid
version=v5
num=7

python ../sgf/merge.py ../data/$version/words words.txt $num
python ../sgf/merge.py ../data/$version/pos pos.txt $num
python ../sgf/merge.py ../data/$version/ner ner.txt $num
python ../sgf/merge.py ../data/$version/penn penn.txt $num
python ../sgf/merge.py ../data/$version/dep dep.txt $num
python ../sgf/invalid.py $source ../data/$version/words/words.txt $invalid
