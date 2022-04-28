import os
import pandas as pd

folder='C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\'

dataframedic = {}

subfolders = [ f.name for f in os.scandir(folder) if f.is_dir() ]
subfolders = ['CWE15_External_Control_of_System_or_Configuration_Setting', 
              'CWE23_Relative_Path_Traversal', 
              'CWE36_Absolute_Path_Traversal', 
              'CWE78_OS_Command_Injection', 
              'CWE89_SQL_Injection']

for name in subfolders [:5]: 
    filepath= os.listdir(folder + name)
    #codelist = []
    
    for filename in filepath:
        comfilepath = folder + name + '\\' + filename
        with open( comfilepath, 'r') as file:
            data = file.read().replace('\n', ' ')
        dataframedic [data] = name

dataframe = pd.DataFrame(dataframedic.items(), columns=['code','category'])
df_shuffled = dataframe.sample(frac=1).reset_index().drop(columns=['index' ])
df_shuffled.to_csv('C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln_dataset.csv')


    
    