# Dataset Conversion

Space=' '
new_line=[]
Word_array=[]
ind=0
## if you want to train the first model, change the name if input file below to 'ned.train' or 'esp.train' and same goes with testing data.
linenum=0
list1=[70]

name1="WriteOutput"
for i1 in list1:
    linenum = 0
    name1 = "Fold_3_"
    name2=name1+str(i1)
    pred_file=open(name2,'r')
    for line in pred_file:
        word=line.split()
        Word_array.append(word)

    file3="Res_"+name2
    #empty_file=open(file3,'a')
    file5=open('test_fold_3_new.txt','r')

    for line in file5:                ## Spanish
        #print line + "\n"
        if linenum>30775:
           print("error, this is not the correct file")
        else:
            #print (linenum)
            linenum+=1
            words = list(line.split())
            # print words
            if len(words)>1:
               #new_line=line+'Space'.join(Word_array[ind])
               new_line=words[0]+Space+words[1]+Space+str("".join(Word_array[ind]))
               ind=ind+1
               with open(file3, "a") as myfile:
                    myfile.write(new_line+"\n")
               new_line=[]
            else:
                if len(Word_array[ind])!=0:

                   print ("Mismatch in line numbers- cross veryify")
                   print(linenum)
                   break
                with open(file3, "a") as myfile:
                     myfile.write("\n")
                ind=ind+1

