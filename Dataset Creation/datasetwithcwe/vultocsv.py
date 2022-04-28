
# importing pandas
import pandas as pd

vuln_data='C:\\Users\\User\\Desktop\\Java\\codes\Cleaned\\vuln\\vuln_dataset.csv'
non_vuln_data='C:\\Users\\User\\Desktop\\Java\\codes\Cleaned\\non_vuln\\non_vuln_dataset.csv'
dataset='C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\dataset.csv'
  
# merging two csv files
df = pd.concat(
    map(pd.read_csv, [vuln_data, non_vuln_data]), ignore_index=True)

df_shuffled = df.sample(frac=1).reset_index().drop(columns=['index' ]).drop(columns=['Unnamed: 0']) 
df_shuffled.to_csv(dataset)



