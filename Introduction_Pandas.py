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
print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.size)
print(dataFrame1.dtypes)










