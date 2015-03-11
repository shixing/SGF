# SGF
Stanford NLP feature General Framework in python and MPI

## Description ##
This package allow you to extract NLP features from some really big files using multiple machine and multiple cores

### Supported NLP Features ###
1. Word Tokenize
2. Sentence Split
3. Part-of-Speech Tagging
4. Dependency Parsing
5. Constitutional Parsing
6. Named Entity Recognition

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

### Prerequisite ###
We need several stanford nlp packages:
1. Stanford-parser
2. Stanford-postagger
3. Stanford-ner
4. mpi4py
5. multiple machines with multicores.

Once you have those Stanford packages installed, copy those *.sh in **/sh_backup/** to corresponding Stanford packages folders. Then config the corresponding path in **config.cfg** file

### How to Run ###
Run on a single machine with 4 cores:

    $ bash run_standalone.sh
Run on a HPC cluster with PBS

    $ qsub run_hpc.jobs

### Speed ###
The slowest part is Dependency parsing: about 1.4 sentence / second on a single core. 


### Question###
contact me: Xing Shi (xingshi@usc.edu)
