#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import codecs
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
after_stemming=[]
from nltk.stem.porter import PorterStemmer
porter_stemmer  = PorterStemmer()
Doc_id=[]
files=[]
All_word_dict={}
path1="C:/Users/Devashi Jain/Desktop/Information Retrieval/positional"
for folder_name in os.listdir(path1):
    for file_name in os.listdir(os.path.join(path1,folder_name)):
        files=[]
        token_files=[]
        after_lower=[]
        after_lemmatizer=[]
        after_stemming=[]
        Doc_id.append(file_name)
        fd=codecs.open(path1+'/'+folder_name+'/'+file_name,'r',errors='ignore')
        files.append(fd.read())
        tokenizer = RegexpTokenizer(r'\w+')
        token_files=tokenizer.tokenize(files[0])
        for i in range(len(token_files)):
            after_lower.append(token_files[i].lower())
        for i in range(len(after_lower)):
            after_lemmatizer.append(wordnet_lemmatizer.lemmatize(after_lower[i]))
            after_stemming.append(porter_stemmer.stem(after_lemmatizer[i]))
        x=folder_name+file_name
        for i in range(len(after_stemming)):
            if after_stemming[i] in All_word_dict:
                if x in All_word_dict[after_stemming[i]]:
                    All_word_dict[after_stemming[i]][x].append(str(i))
                else :
                    All_word_dict[after_stemming[i]][x]=[str(i)]
            else :
                    All_word_dict[after_stemming[i]]={x:[str(i)]}


# In[ ]:





# In[10]:


import sys
import os
import codecs
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
Search_Query=(str(input()))
a=Search_Query.split()
index_dic={}
if(len(a)>15):
    print("Not a valid Query")
elif(len(a)<=15):
        after_lower=[]
        after_lemmatizer=[]
        after_stemming=[]
        Keys=[]
        Values=[]
        for i in range(len(a)):
            after_lower.append(a[i].lower())
            after_lemmatizer.append(wordnet_lemmatizer.lemmatize(after_lower[i]))
            after_stemming.append(porter_stemmer.stem(after_lemmatizer[i]))
        for word in after_stemming:
            if word not in All_word_dict:
                print("not found")
                sys.exit()
        for i in range(len(after_stemming)):
                    Keys.append(All_word_dict[after_stemming[i]].keys()) 
                    Values.append(All_word_dict[after_stemming[i]].values())
        for x in Keys[0]:
            if x in Keys[1]:
                a=All_word_dict[after_stemming[0]][x]
                b=All_word_dict[after_stemming[1]][x]
                i=0
                j=0
                list1=[]
                while(i< len(a) and j< len(b)):
                    if(int(a[i])<int(b[j]) and int(a[i])+1==int(b[j])):
                        i=i+1
                        list1.append(b[j])
                    elif(int(a[i])<int(b[j])):
                        i=i+1
                    elif(int(a[i])>int(b[j])):
                        j=j+1
                    index_dic[x]=list1
        
        for k in range(2,len(after_stemming)):
            dict1={}
            for x in index_dic.keys():
                if x in Keys[k]:
                    a=index_dic[x]
                    b=All_word_dict[after_stemming[k]][x]
                    i=0
                    j=0
                    while(i< len(a) and j< len(b)):
                        list1=[]
                        if(int(a[i])<int(b[j]) and int(a[i])+1==int(b[j])):
                            i=i+1
                            list1.append(b[j])
                        elif(int(a[i])<int(b[j])):
                            i=i+1
                        elif(int(a[i])>int(b[j])):
                            j=j+1
                        dict1[x]=list1
                        index_dic[x]=list1
            list2=[]
            for word in dict1:
                if len(dict1[word])>0 :
                    list2.append(word)
                
print(list2)                       
print(len(list2))



