## feature s1
# for toy
version=v5
dataset=43
feature=abs
fn=../data/base/$dataset.en.$feature
dest=/home/nlg-05/xingshi/workspace/misc/lstm/visual_pa/data/$dataset/

python ../sgf/dep_features.py $feature ../data/$version/dep/dep.txt ../data/$version/words/words.txt > $fn

cp $fn $dest

feature=rel
fn=../data/base/$dataset.en.$feature
dest=/home/nlg-05/xingshi/workspace/misc/lstm/visual_pa/data/$dataset/

python ../sgf/dep_features.py $feature ../data/$version/dep/dep.txt ../data/$version/words/words.txt > $fn

cp $fn $dest


# for 10k
version=v4
dataset=10k
feature=abs
fn=../data/base/$dataset.en.$feature
dest=/home/nlg-05/xingshi/workspace/misc/lstm/visual_pa/data/$dataset/

python ../sgf/dep_features.py $feature ../data/$version/dep/dep.txt ../data/$version/words/words.txt > $fn

cp $fn $dest

feature=rel
fn=../data/base/$dataset.en.$feature
dest=/home/nlg-05/xingshi/workspace/misc/lstm/visual_pa/data/$dataset/

python ../sgf/dep_features.py $feature ../data/$version/dep/dep.txt ../data/$version/words/words.txt > $fn

cp $fn $dest

