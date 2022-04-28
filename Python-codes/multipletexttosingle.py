import os

old_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\'
cwe15_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE15_External_Control_of_System_or_Configuration_Setting'
cwe23_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE23_Relative_Path_Traversal'
cwe36_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE36_Absolute_Path_Traversal'
cwe78_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE78_OS_Command_Injection'
cwe89_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE89_SQL_Injection'
cwe80_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE80_XSS'
cwe113_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE113_HTTP_Response_Splitting'
cwe129_new_path = 'C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\CWE129_Improper_Validation_of_Array_Index'


file_cwe15='CWE15_External_Control_of_System_or_Configuration_Setting.txt'
file_cwe23='CWE23_Relative_Path_Traversal.txt'
file_cwe36='CWE36_Absolute_Path_Traversal.txt'
file_cwe78='CWE78_OS_Command_Injection.txt'
file_cwe89='CWE89_SQL_Injection.txt'
file_cwe80='CWE80_XSS.txt'
file_cwe113='CWE113_HTTP_Response_Splitting.txt'
file_cwe129='CWE129_Improper_Validation_of_Array_Index.txt'


# CWE15
os.chdir(cwe15_new_path)   
    
with open(old_path + file_cwe15) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()

# CWE23

os.chdir(cwe23_new_path)   
    
with open(old_path + file_cwe23) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()
 
# CWE36
os.chdir(cwe36_new_path)   
    
with open(old_path + file_cwe36) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()
    
# CWE78
os.chdir(cwe78_new_path)   
    
with open(old_path + file_cwe78) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()
    
# CWE89
os.chdir(cwe89_new_path)   
    
with open(old_path + file_cwe89) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()
    
# CWE80
os.chdir(cwe80_new_path)   
    
with open(old_path + file_cwe80) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()
    
# CWE113
os.chdir(cwe113_new_path)   
    
with open(old_path + file_cwe113) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()
    
# CWE113
os.chdir(cwe129_new_path)   
    
with open(old_path + file_cwe129) as fo:
    
    op=''
    start=0
    cntr=1
    
    for x in fo.read().split("\n"):
        if (x=="-----------------------------------------------------------------"):
            if (start==1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op=''
                    cntr+=1
                   
            else:
                    start=1
        else:
            if (op==''):
                op=x
                
            else:
                op = op + '\n' + x
           
           
    fo.close()