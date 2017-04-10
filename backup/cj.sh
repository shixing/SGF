#!/bin/bash


infile=$1
outfile=$2

split -d -l 500 $infile $infile.

for i in $infile.*;
do
python /home/nlg-05/xingshi/workspace/tools/BLLIP/parser.py $i $i.tree;
rm $i;
done

cat $infile.*tree > $outfile
rm $infile.*tree