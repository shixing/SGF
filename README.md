# SGF
NLP feature General Framework in python and MPI

## Description ##
This package allow you to extract NLP features from some really big files using multiple machine and multiple cores

### Supported NLP Features ###
1. Word Tokenize
2. Sentence Split
3. Part-of-Speech Tagging
4. Dependency Parsing (Stanford)
5. Constitutional Parsing (Stanford)
6. Named Entity Recognition
7. Multi-word Predicate Identification (accroding to a mwe list)

### Supported Corpus Reader ###
1. Treebank
2. English Web Treebank
3. The Treebank of Ontonotes

### Pipeline Overview ###
Suppose you have the following directory structure:

    /data/
	base/
		big-file.txt
	v1/
		words/
		pos/
		dep/
		penn/
		ner/



The big-file is such a big file that you can not process it in a short time. Suppose you have 20 machines with 8 cores each. Our package will first split big-file.txt into 159 parts, then extract features on each subfiles. Finally, you will get the following structure:

    /data/
	base/
		big-file.txt
	v1/
		words/
			words.txt.0 
			... ...		
			words.txt.158
		pos/
			pos.txt.[0-158]
		dep/
			dep.txt.[0-158]
		penn/
			penn.txt.[0-158]
		ner/
			ner.txt.[0-158]

The pipeline will first split **big-file** into *$npid* parts.

If you choose **pos_corpus.sh**, the **big-file** is treated as untokenzied, un-sentence-split corpus, the **pos_corpus.sh** will split paragraphs into sentences and then tokenize it.

If you choose **pos.sh**, the **big-file** is treated as untokenzied, sentence-split corpus, each line is treated as a sentence. **pos.sh** will just tokenize each line.

Every other features will use words.txt.[0-158] directly without tokenization. 


### Prerequisite ###
We need several stanford nlp packages:
1. Stanford-parser
2. Stanford-postagger
3. Stanford-ner
4. mpi4py
5. multiple machines with multicores.

### How to Run ###
copy **ner.sh** stanford-ner/

copy **NER.java** stanford-ner/

compile **NER.java** by

'''
javac -cp stanford-ner.jar NER.java
'''

copy **pos.sh** stanford-postagger/
copy **pos_corpus.sh** stanford-postagger/

copy **POS.java** stanford-postagger/

compile **POS.java** by

'''
javac -cp stanford-postagger.jar POS.java
'''
copy **penn.sh** and **dep.sh** stanford-parser/

Run on a single machine with 4 cores:

    $ bash run_standalone.sh
Run on a HPC cluster with PBS

    $ qsub run_hpc.jobs

### Speed ###
The slowest part is Dependency parsing: about 1.4 sentence / second on a single core. 

### Python Code
There are two base classes: `Feature` and `Resourch`

#### sgf/merge.py
usages: merge.py <folder> <prefix> <number of parts>
'''
$ cd sgf/
$ python merge.py ../data/v5/words/ words.txt 159
'''
It will generate ../data/v5/words/words.txt. 

#### sgf/invalid.py
usages: invalid.py <original file> <merged tokenized file> <invalid list file>
It will compare each line between <original file> and <merged tokenized file>, if they have the same number of words, print 1 into <invalid list file>, otherwise print 0.

### Question###
contact me: Xing Shi (xingshi@usc.edu)
