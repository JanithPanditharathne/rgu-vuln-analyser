from shutil import copyfile
import os
import re
import glob
import shutil
import pandas as pd

root_path = "C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\"
folders = ["CWE15_External_Control_of_System_or_Configuration_Setting",
                  "CWE23_Relative_Path_Traversal",
                  "CWE36_Absolute_Path_Traversal",
                  "CWE78_OS_Command_Injection",
                  "CWE89_SQL_Injection",
                  "CWE80_XSS",
                  "CWE113_HTTP_Response_Splitting",
                  "CWE129_Improper_Validation_of_Array_Index"]

def deleteDirecotories():
    for folder in folders:
        shutil.rmtree(os.path.join(root_path,folder))
        
def createDirectories():
    for folder in folders:
        os.mkdir(os.path.join(root_path,folder))
        
def vuln_dataset():

    cwe15_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE15_External_Control_of_System_or_Configuration_Setting'
    paths = os.listdir(cwe15_origin)
    dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE15_External_Control_of_System_or_Configuration_Setting'

    for src in paths:
        r = re.search(r'(\d*)\.txt', src)

        if r and int(r.group(1)) % 2 == 1:
            copyfile(os.path.join(cwe15_origin, src), os.path.join(dst_dir, r.group()))
        

    cwe23_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE23_Relative_Path_Traversal'
    paths = os.listdir(cwe23_origin)
    dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE23_Relative_Path_Traversal'

    for src in paths:
        r = re.search(r'(\d*)\.txt', src)

        if r and int(r.group(1)) % 2 == 1:
            copyfile(os.path.join(cwe23_origin, src), os.path.join(dst_dir, r.group()))
        
    cwe36_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE36_Absolute_Path_Traversal'
    paths = os.listdir(cwe36_origin)
    dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE36_Absolute_Path_Traversal'

    for src in paths:
        r = re.search(r'(\d*)\.txt', src)

        if r and int(r.group(1)) % 2 == 1:
            copyfile(os.path.join(cwe36_origin, src), os.path.join(dst_dir, r.group()))
        
    cwe78_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE78_OS_Command_Injection'
    paths = os.listdir(cwe78_origin)
    dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE78_OS_Command_Injection'

    for src in paths:
        r = re.search(r'(\d*)\.txt', src)

        if r and int(r.group(1)) % 2 == 1:
            copyfile(os.path.join(cwe78_origin, src), os.path.join(dst_dir, r.group()))
        
    cwe89_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE89_SQL_Injection'
    paths = os.listdir(cwe89_origin)
    dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE89_SQL_Injection'

    for src in paths:
        r = re.search(r'(\d*)\.txt', src)

        if r and int(r.group(1)) % 2 == 1:
            copyfile(os.path.join(cwe89_origin, src), os.path.join(dst_dir, r.group()))
            
    # cwe80_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE80_XSS'
    # paths = os.listdir(cwe80_origin)
    # dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE80_XSS'

    # for src in paths:
    #     r = re.search(r'(\d*)\.txt', src)

    #     if r and int(r.group(1)) % 2 == 1:
    #         copyfile(os.path.join(cwe80_origin, src), os.path.join(dst_dir, r.group()))
            
    # cwe113_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE113_HTTP_Response_Splitting'
    # paths = os.listdir(cwe113_origin)
    # dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE113_HTTP_Response_Splitting'

    # for src in paths:
    #     r = re.search(r'(\d*)\.txt', src)

    #     if r and int(r.group(1)) % 2 == 1:
    #         copyfile(os.path.join(cwe113_origin, src), os.path.join(dst_dir, r.group()))
            
    # cwe129_origin = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE129_Improper_Validation_of_Array_Index'
    # paths = os.listdir(cwe129_origin)
    # dst_dir = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\CWE129_Improper_Validation_of_Array_Index'

    # for src in paths:
    #     r = re.search(r'(\d*)\.txt', src)

    #     if r and int(r.group(1)) % 2 == 1:
    #         copyfile(os.path.join(cwe129_origin, src), os.path.join(dst_dir, r.group()))
 
def texttocsv():

    folder='C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\'

    dataframedic = {}

    folders = [ f.name for f in os.scandir(folder) if f.is_dir() ]

    for name in folders [:8]: 
        filepath= os.listdir(folder + name)
        #codelist = []
    
        for filename in filepath:
            comfilepath = folder + name + '\\' + filename
            with open( comfilepath, 'r') as file:
                data = file.read().replace('\n', ' ')
                dataframedic [data] = 'vuln'
    
    
    #dataframe = pd.DataFrame.from_dict([dataframedic])
    dataframe = pd.DataFrame(dataframedic.items(), columns=['code','category'])
    df_shuffled = dataframe.sample(frac=1).reset_index().drop(columns=['index' ])
    df_shuffled.to_csv('C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln\\vulnlabeled_dataset.csv')
        
# deleteDirecotories()
# createDirectories()
# vuln_dataset()
texttocsv()