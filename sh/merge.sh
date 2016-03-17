
source=../data/base/10k.en
invalid=../data/base/10k.en.invalid
version=v4
num=15

python ../sgf/merge.py ../data/$version/words words.txt $num
python ../sgf/merge.py ../data/$version/pos pos.txt $num
python ../sgf/merge.py ../data/$version/ner ner.txt $num
python ../sgf/merge.py ../data/$version/penn penn.txt $num
python ../sgf/merge.py ../data/$version/dep dep.txt $num
python ../sgf/invalid.py $source ../data/$version/words/words.txt $invalid
