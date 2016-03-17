## feature s1
# for toy
version=v5
dataset=43
feature=s2
fn=../data/base/$dataset.en.$feature
dest=/home/nlg-05/xingshi/workspace/misc/lstm/visual_pa/data/$dataset/

python ../sgf/penn_features.py $feature ../data/$version/penn/penn.txt > $fn
cp $fn $dest

# for 10k
version=v4
dataset=10k
feature=s2
fn=../data/base/$dataset.en.$feature
dest=/home/nlg-05/xingshi/workspace/misc/lstm/visual_pa/data/$dataset/

python ../sgf/penn_features.py $feature ../data/$version/penn/penn.txt >$fn
cp $fn $dest
