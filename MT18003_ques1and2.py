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
Document_id=[]
Doc_id=[]
Posting={}
parent="C:/Users/Devashi Jain/Desktop/Information Retrieval/20_newsgroups/20_newsgroups"
for folder_name in os.listdir(parent):
    for file_name in os.listdir(os.path.join(parent,folder_name)): 
        Doc_id.append(folder_name+file_name)
        files=[]
        token_files=[]
        after_removing_stopwords=[]
        after_lower=[]
        after_lemmatizer=[]
        after_stemming=[]
        unique_words=[]
        sorted_list=[]
        fd=codecs.open(parent+'/'+folder_name+'/'+file_name,'r',errors='ignore')
        files.append(fd.read())
        tokenizer = RegexpTokenizer(r'\w+')
        token_files=(tokenizer.tokenize(files[0]))
        for i in range(len(token_files)):
            after_lower.append(token_files[i].lower())
        for r in after_lower:
                if r not in stop_words:
                    after_removing_stopwords.append(r)
        for i in range(len(after_removing_stopwords)):
            after_lemmatizer.append(wordnet_lemmatizer.lemmatize(after_removing_stopwords[i]))
        for i in range(len(after_lemmatizer)):
            after_stemming.append(porter_stemmer.stem(after_lemmatizer[i]))
        unique_words=set(after_stemming)
        unique_words=list(unique_words)
        sorted_list=sorted(unique_words)
        for i in range(len(sorted_list)):
            if sorted_list[i] in Posting:
                Posting[sorted_list[i]].append(folder_name+file_name)
            else:
                Posting[sorted_list[i]] = [folder_name+file_name]


# In[2]:


import collections
Dictionary_Posting=collections.OrderedDict(sorted(Posting.items()))


# In[15]:


import sys
Search_Query=(str(input()))
x=Search_Query.split()
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
a=Search_Query.split()
y=x[1]
query_lower=[]
lemmatize_query=[]
stemmed_query=[]
if(len(a)==3):
    x.remove(x[1])
    print(x)
    for i in range(len(x)):
        query_lower.append(x[i].lower())
        lemmatize_query.append(wordnet_lemmatizer.lemmatize(query_lower[i]))
        stemmed_query.append(porter_stemmer.stem(lemmatize_query[i]))
    for word in stemmed_query:
        if word not in Dictionary_Posting:
            print("not found")
            sys.exit()
    if(y=='or' or y=='OR' or y=='Or'):
                    list1=(Dictionary_Posting[stemmed_query[0]])
                    list2=Dictionary_Posting[stemmed_query[1]]
                    list3=set(list1+list2)
                    list3=list(list3)
    elif(y=='and' or y=='And' or y=='AND'):
            list1=(Dictionary_Posting[stemmed_query[0]])
            list2=(Dictionary_Posting[stemmed_query[1]])
            for i in list1:
                if i in list2:
                    list3.append(i)
elif(len(a)==4):
    x.remove(x[1])
    x.remove(x[1])
    
    for i in range(len(x)):
        query_lower.append(x[i].lower())
        lemmatize_query.append(wordnet_lemmatizer.lemmatize(query_lower[i]))
        stemmed_query.append(porter_stemmer.stem(lemmatize_query[i]))
    for word in stemmed_query:
        if word not in Dictionary_Posting:
            print("not found")
            sys.exit()
    if(y=='or' or y=='OR' or y=='Or'):
                list1=Dictionary_Posting.values()
                list2=Dictionary_Posting[stemmed_query[0]]
                list4=Dictionary_Posting[stemmed_query[1]]
                for i in Doc_id:
                    if i not  in list4:
                        list5.append(i)
                list3=list(set(list5+list2))
    elif(y=='and' or y=='And' or y=='AND'):
            list1=(Dictionary_Posting[stemmed_query[0]])
            list2=(Dictionary_Posting[stemmed_query[1]])
            for i in list1:
                if i not  in list2:
                    list3.append(i)
print(len(list3))
print(list3)



# In[ ]:




