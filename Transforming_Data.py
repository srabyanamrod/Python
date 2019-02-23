

# 1) pandas hızlı ve etkili for dataframes
# 2) csv ve text dosyalarına acip inceleyip sonuclarımıza bu dosya tiplerine rahat bir sekilde kaydedeblir.
# 3) pandas bizim isimizi kolaylastırıyor for missing data
# 4) reshape yspıp datayı daha etkili bir şekilde kullanabiliriz.
# 5) slicing indexing kolay
# 6) time series data analizinde çok yardımcı
# 7) ayrıca herşeyden önemlisi hız pandas hız açısından optimizze edilmiş bir kütüphane

import pandas as pd
dictionary = {"NAME":["Barış","Aybars","Ferhat","Mustafa","Onur","Berk","Murat"],
               "AGE":[22,23,27,24,23,23,21],
              "MAAS": [100,150,240,350,110,300,400]}
dataFrame1 = pd.DataFrame(dictionary)
print(dataFrame1)
head = dataFrame1.head()
print(head)
tail= dataFrame1.tail()
print(tail)


# %%
# Pandas basic method
"""print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.size)
print(dataFrame1.dtypes)"""

# %% İndexing and Slicing
"""
print(dataFrame1["NAME"])
print(dataFrame1["AGE"])
dataframe1["yeni_feature"]= [-1,-2,-3,-4,-5,-6]
print(dataFrame1.doc[:,"AGE"])
print(dataFrame1.loc[:3,"AGE"])
print(dataFrame1.loc[3,["AGE","NAME""]])
print(dataFrame1.loc[::-1,:])
print(dataFrame1.loc[:,:"NAME"])
print(dataFrame1.iloc[:,"NAME"])
print(dataFrame1.iloc[:,2])
"""
"""
# %% filtering
print("----------------------\n Filtering")
filtre1 = dataFrame1.MAAS > 200
filrelenmis_data = dataFrame1[filtre1]
print(filrelenmis_data)
print("\n-----------------------\n Age Filtering")
filtre2 = dataFrame1.AGE < int(23)
print(filtre2)
print(dataFrame1[filtre1 & filtre2])
"""
# %% List Comprehension
import numpy as np
ortalama_maas = dataFrame1.MAAS.mean()

# ortalama_maas_np = np.mean(dataFrame1.MAAS)
dataFrame1["maas_seviyesi"] = ["Low" if ortalama_maas > each else "High" for each in dataFrame1.MAAS]
"""
for each in dataFrame1.MAAS:
    if(ortalama_maas > each):
        print("Low")
    else
        print("High")"""

dataFrame1["list_comp"]= [each*2 for each in dataFrame1.AGE]
print(dataFrame1)

def multiply(AGE):
    return AGE*3

dataFrame1["apply_metodu"] = dataFrame1.AGE.apply(multiply)
print(dataFrame1)








