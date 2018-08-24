import codecs
def chang(file,save):
    with codecs.open(file,"r","utf-8") as fr:
        with codecs.open(save,"w","utf-8") as fw:
            for line in fr :
                lines = line.strip().split()
                print(lines)
                if len(lines)!=0:
                    if lines[1] == "O":
                        fw.write(lines[0] + "	" + lines[1]+ "\n")
                    else:
                        tag = lines[1].split("-")
                        pre = tag[0]
                        ner = tag[1]
                        if pre == "M" or pre == "E":
                            newtag = "I" + "-" + ner
                            fw.write(lines[0] + "	" + newtag+ "\n")
                        elif pre == "S":
                            newtag = "B" + "-" + ner
                            fw.write(lines[0] + "	" + newtag + "\n")
                        else:
                            fw.write(lines[0] + "	" + lines[1]+ "\n")
                else:
                    fw.write("\n")

chang("train.char.bmes","weibo-train.txt")
chang("dev.char.bmes","weibo-dev.txt")
chang("test.char.bmes","weibo-test.txt")
