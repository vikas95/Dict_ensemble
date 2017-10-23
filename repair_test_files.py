file1=open("test_fold_4.txt","r")
Out_file=open("test_fold_4_new.txt","w")
prev_line=""
for line in file1:
    if line=="\n":
       if prev_line=="\n":
          pass
       else:
          Out_file.write(line)
    else:
       Out_file.write(line)

    prev_line=line


