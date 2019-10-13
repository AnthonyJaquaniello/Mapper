#!/usr/bin/env python
# coding: utf-8

# In[2]:


seq = "CAATGCAA"


# In[3]:


def BWTg(seq):
    seq = ["$"] + list(seq)
    mat_seq = []
    for i in range(len(seq)):
        mat_seq.append(seq[(len(seq)-i):len(seq)]+seq[0:(len(seq)-i)])
    mat_seq_sorted = sorted(mat_seq)
    return mat_seq_sorted


# In[4]:


mat_seq = BWTg(seq)
mat_seq


# In[8]:


def dollar(mat):
    dollar = []
    for sublist in mat:
        dollar.append(sublist.index('$'))
    return dollar


# In[9]:


def first(mat):
    first_col = []
    for sublist in mat:
        first_col.append(sublist[0])
    return first_col


# In[10]:


def last(mat):
    last_col = []
    for sublist in mat:
        last_col.append(sublist[-1])
    return last_col


# In[22]:


indexage = dollar(mat_seq)
first_col = first(mat_seq)
last_col = last(mat_seq)


# In[12]:


print(indexage)
print(first_col)
print(last_col)


# In[13]:


mat_seq


# In[14]:


super_liste = []

for i in range(len(first_col)):
    doublet = []
    doublet.append(first_col[i])
    doublet.append(last_col.index(first_col[i]))
    last_col[last_col.index(first_col[i])] = "guillaume"
    super_liste.append(doublet)


# In[15]:


super_liste


# In[16]:


revert_seq = []
flag = 0
for i in range(len(super_liste)):
    revert_seq.append(super_liste[flag][0])
    flag = super_liste[flag][1]
    


# In[17]:


revert_seq.remove("$")
revert_chain = "".join(revert_seq)


# In[18]:


revert_chain


# In[19]:


first_col


# In[ ]:


for i in range(len(first_col)):
    if first_col[i] == 'A':
        


# Construire un index qui compte, combien j'ai de A avant le $ de la sequence courante... etc

# In[20]:


mat_seq


# In[23]:


last_col


# In[26]:


index = []

for i in range(len(last_col)+1):
    if i ==0:
        d = {"$":0,"A":0,"C":0,"G":0,"T":0}
    else:
        d = {"$":last_col[0:i].count("$"),
             "A":last_col[0:i].count("A"),
             "C":last_col[0:i].count("C"),
             "G":last_col[0:i].count("G"),
             "T":last_col[0:i].count("T")}
    index.append(d)


# In[27]:


index


# In[31]:


print(index[-1])
surindex = {"$":0,"A":0,"C":0,"G":0,"T":0}


# In[34]:


surindex["$"] = 0
surindex["A"] = index[-1]["$"]
surindex["C"] = index[-1]["$"]+index[-1]["A"]
surindex["G"] = index[-1]["$"]+index[-1]["A"]+index[-1]["C"]
surindex["T"] = index[-1]["$"]+index[-1]["A"]+index[-1]["C"]+index[-1]["G"]


# In[37]:


print(surindex)
index


# In[41]:


def final(read, surindex, index, last_col):
    p = len(read)-1
    carac = read[p]
    b =  surindex[carac]
    e = b + index[len(last_col)][carac]
    end = []
    while (p >0 and e > b):
        p -= 1
        carac = read[p]
        b =  surindex[carac] + index[b][carac]
        e = surindex[carac] + index[e][carac]
    end.append(b)
    end.append(e)
    return end


# In[49]:


fin = final("CAA",surindex, index, last_col)


# In[53]:


print(fin)
nb_hit = fin[1] - fin[0]
print(nb_hit)


# In[85]:


indexage


# In[74]:


appariement = zip(indexage, last_col)


# In[75]:


my_appar = list(appariement)


# In[83]:


my_appar_sorted = sorted(my_appar, reverse = True)


# In[84]:


my_appar_sorted


# In[90]:


seq_initiale = []
for tuples in my_appar_sorted:
    caract = tuples[1]
    seq_initiale.append(caract)
seq_initiale.remove("$")
str_seq_initiale = "".join(seq_initiale)


# In[92]:


print(str_seq_initiale)


# In[ ]:




