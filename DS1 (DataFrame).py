#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.DataFrame({"a":[4,5,6],"b":[7,8,9],"c":[10,11,12]},index=[1,2,3])
print(df)


# In[4]:


import pandas as pd
data=[1,2,3,4]
df=pd.DataFrame(data)
print(df)


# In[5]:


import pandas as pd
data=[['Bob',10],['Alex',12]]
df=pd.DataFrame(data,index=["Name","Age"])
print(df)


# In[6]:


import pandas as pd
data={'car':["BMW","Audi","Ford"],'passing':[3,7,2]}
myvar=pd.DataFrame(data)
print(myvar)


# In[11]:


import pandas as pd
data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(data)
print(df)
print()
df=pd.DataFrame(data,index=['First','Second'])
print(df)
print()
df1=pd.DataFrame(data,index=['First','Second'],columns=['a','b'])
print(df1)


# In[29]:


import pandas as pd
data={'Name':['AAA','BBB','CCC'],'Age':[20,21,22],'Height':[5.3,5.6,5.9]}
df=pd.DataFrame(data)
city=['Chennai','Bangalore','Pune']
df['City']=city
print(df)
degree=['Msc','B.com','Btech']
df['Degree']=degree
print()
print(df)
del df['Degree']
print()
print("After Deletion of Column 5")
print(df)
print()
df.drop(['City'],axis=1,inplace=True) #1= column, 0=row
print(df)
print()
df.pop('Age')
print(df)
print()
df.rename(columns={'Height':'HG'},inplace=True)
print(df)
print()
degree=['Msc','B.com','Btech']
df['Degree']=degree
print(df)
df.drop(0,axis=0,inplace=False)
print()
print(df)
print()
print(df[['Name','HG']])
print()
print(df.filter())


# In[15]:


import pandas as pd
df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df=pd.concat([df,df2],ignore_index=True)
print()
print(df)


# In[2]:


import pandas as pd
data={'Name':['Alice','Bob'],'Age':[20,21],'Gender':['F','M'],'Height':[5.3,5.8]}
df=pd.DataFrame(data)
print(df['Name'])
print()
print(df)


# In[1]:


import pandas as pd
data={'Name':['jai','anuj'],'age':[24,26],'address':['delhi','jaipur'],'height':[1.54,3.55]}
df=pd.DataFrame(data)

df.filter(like='eigh')


# In[2]:


import pandas as pd
data={'Name':['jai','anuj'],'age':[24,26],'address':['delhi','jaipur'],'height':[1.54,3.55]}
df=pd.DataFrame(data)
df.filter(regex='e|a',axis=1)


# In[3]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,24],'address':['delhi','jaipur','Chennai','Chennai'],'height':[1.54,3.55,4.2,4.2]}
df=pd.DataFrame(data)
df=df.drop_duplicates()
print()
df


# In[4]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano'],'age':[24,26,24,24],'address':['delhi','jaipur','Chennai','rajasthan'],'height':[1.54,3.55,4.2,4.5]}
df=pd.DataFrame(data)
df=df.drop_duplicates(subset=['Name','age'],keep='last')
print()
df


# In[6]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Mano','Nan'],'age':[24,26,24,24,20],'address':['delhi','jaipur','Chennai','rajasthan','Switz'],'height':[1.54,3.55,4.2,4.5,5]}
df=pd.DataFrame(data)
df_sample=df.sample(frac=0.2)
print(df_sample)
print()
df_sample=df.sample(n=2,axis=1)
print(df_sample)


# In[20]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
top_salaries=df.nlargest(2,columns='salary')
print(top_salaries)
print()
bottom_salaries=df.nsmallest(2,columns='salary')
print(bottom_salaries)
df=df.query('age>24 or salary>=50000')
print()
print(df)
print()
df=df.query('Name.str.contains("n")')
print(df)
print()
df=df.query('gender==["M"] and age<25')
print(df)


# In[23]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df.loc[:,'age']


# In[24]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df.iloc[:,2]


# In[26]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df.loc[:,['age','gender']]


# In[27]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df.iloc[:,0]


# In[30]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df_fil=df[df['age']>=24]
print(df_fil)


# In[31]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df_fil=df[(df['age']>=24) & (df['salary']>=50000)]
print(df_fil)


# In[38]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,20],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df_fil=df[df['Name'].str.startswith(('N','M'))]
print(df_fil)


# In[46]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,26],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
print(df.tail(2))
print()
print(df.head(1))
print()
df.info()


# In[47]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,26],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
print(df.describe())


# In[48]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan'],'age':[24,26,24,26],'salary':[20000,30000,50000,90000],'gender':['M','F','M','M']}
df=pd.DataFrame(data)
df_sort=df.sort_values(by='age',ascending=False)
print(df_sort)


# In[ ]:




