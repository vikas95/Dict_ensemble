from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))
Common_words=["Tissue","activator","recombinant",]


file1=open("Res_AWS_GPU_BEST_96","r")
#dict_file=open("DrugBank_Approved_dict.txt","r")
dict_file=open("DrugBank_Approved_dict","r")

Out_file=open("test_all_CRF_dict.txt","w")
#Out_file=open("train_all_CRF.txt","w")
drug_list=[]
for drug_name in dict_file:
    drug_name=drug_name.split()
    drug_list.append(drug_name[0])



new_line=""
dict_val=""
for line in file1:
    if line=="\n":
       if prev_line=="\n":
          pass
       else:
          Out_file.write(line)
    else:
       words1=line.split()
       if words1[0].lower() in drug_list:
          dict_val="yes"
       else:
          dict_val="no"

       new_line=words1[1] + "\t" + words1[2] + "\t" + words1[0] + "\t" + dict_val
       Out_file.write(new_line+"\n")

    prev_line=line


