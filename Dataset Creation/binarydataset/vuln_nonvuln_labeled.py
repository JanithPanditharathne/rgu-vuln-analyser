
# importing pandas
import pandas as pd
import numpy as np
  
# merging two csv files
df = pd.concat(
    map(pd.read_csv, ['C:\\Users\\User\\Desktop\\Java\\codes\Cleaned\\vuln\\vulnlabeled_dataset.csv', 'C:\\Users\\User\\Desktop\\Java\\codes\Cleaned\\non_vuln\\non_vuln_dataset.csv']), ignore_index=True)

df_shuffled = df.sample(frac=1).reset_index().drop(columns=['index' ]).drop(columns=['Unnamed: 0']) 
df_shuffled.to_csv('C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\binary.csv')



