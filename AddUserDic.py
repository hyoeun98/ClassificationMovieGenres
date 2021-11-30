#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pickle
import re
import pandas as pd
import pprint
import hgtk
import gzip
from konlpy.tag import Mecab


# In[7]:


nng = pd.read_csv('../NNG.csv')['Column1'] # 일반 명사
nng = nng.tolist()


# In[8]:


with open('CharacterNames.txt','rb') as f:
    character_names = pickle.load(f)


# In[9]:


with open('RequireTitle.txt','rb') as f:
    require_title = pickle.load(f)


# In[10]:


character_names = pd.unique(character_names).tolist() # 중복 제거


# In[11]:


for i,v in enumerate(character_names): # 정규 표현식으로 cleaning
    translate=re.sub("\(.+\)", "", v)
    translate=re.sub("\.\.\.", "", translate)
    translate=re.sub("목소리.*", "", translate)
    translate=re.sub("\W", " ", translate)
    translate=re.sub("\d", "", translate)
    translate=re.sub(" 역", "",translate)
    character_names[i] = translate 


# In[12]:


clean_names = []
for i in character_names:
    clean_names.extend(i.split(' '))

clean_names = list(set(clean_names))
result = [word for word in clean_names if not word in nng]


# In[13]:


with open('CleanCharacterNames.txt','wb') as f:
    pickle.dump(result,f)


# In[14]:


has_final_syllable = []
non_final_syllable = []
non_korean = []
del result[0]


# In[15]:


for i in result:
    if hgtk.checker.is_hangul(i):
        if hgtk.checker.has_batchim(i[-1]):
            has_final_syllable.append(i)
        else:
            non_final_syllable.append(i)
    else:
        non_korean.append(i)


# In[16]:


with open('C:/mecab/user-dic/nnp.csv', 'a', encoding='UTF-8') as f:
    for i in has_final_syllable:
        f.write(f'{i},,,,NNP,*,T,{i},*,*,*,*,*\n')
    for i in non_final_syllable:
        f.write(f'{i},,,,NNP,*,F,{i},*,*,*,*,*\n')

