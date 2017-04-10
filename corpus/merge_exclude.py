
def load_file(fn,d):
    with open(fn) as f:
        for line in f:
            d.add(line)

wsj22 = "./wsj.22.trainwords"
wsj23 = "./wsj.23.trainwords"

d = set()

load_file(wsj22,d)
load_file(wsj23,d)

fout_words = open("9m.train.trainwords",'w')
fout_penn = open("9m.train.trainline",'w')

def output_file(fn_words,fn_penn,d):
    f1 = open(fn_words)
    f2 = open(fn_penn)

    n = 0
    m = 0
    while True:
        l1 = f1.readline()
        l2 = f2.readline()
        if not l1:
            break
        if not l1 in d:
            m += 1
            fout_words.write(l1)
            fout_penn.write(l2)
        else:
            n += 1
            
    print fn_words,m, n
            
        
    f1.close()
    f2.close()

fns = ["wsj.train", "onto.train","ewtb.train","8m.train"]    

for fn in fns:
    output_file(fn+".trainwords", fn+".trainline",d)

fout_words.close()
fout_penn.close()


