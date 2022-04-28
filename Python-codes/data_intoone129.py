import re
import sys
import glob
import os
import fileinput
import csv

sourcefilepath = 'C:\\Users\\User\\Desktop\\Java\\codes\\'

read_cwe129 = glob.glob("C:\\Users\\User\\Desktop\\Java\\codes\\CWE129_Improper_Validation_of_Array_Index\\*.java")
file_cwe129='CWE129_Improper_Validation_of_Array_Index.txt'
new_file_cwe129='CWE129_Improper_Validation_of_Array_Index1.txt'
 
def removeCurlyBraces129():
    
    with open(sourcefilepath+file_cwe129, 'r') as my_file:
        text = my_file.read()
        text = text.replace("{", "")
        text = text.replace("}", "")
        

# save the updates back into a cleaned up file
    with open(sourcefilepath+file_cwe129, 'w') as my_file:
        my_file.write(text)
        
def removeSpecLines129():

    bad_words = ['import', 'try', 'catch', 'finally', 'else', 'CWE', 'Buffer']

    with open(sourcefilepath+file_cwe129) as oldfile, open(sourcefilepath+ new_file_cwe129, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
    
    os.remove(sourcefilepath+file_cwe129)              
    os.rename(sourcefilepath+new_file_cwe129, sourcefilepath+file_cwe129 )
    
def removeSpecWord():
    
    delete_list = ["goodG2B"]
    with open(sourcefilepath+file_cwe129) as fin, open(sourcefilepath+ new_file_cwe129, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)
                
    os.remove(sourcefilepath+file_cwe129)              
    os.rename(sourcefilepath+new_file_cwe129, sourcefilepath+file_cwe129 )
    
def removewordsdoublequotes():
    
    with open(sourcefilepath+file_cwe129) as infile, open(sourcefilepath+ new_file_cwe129, 'w') as outfile:
        for line in infile:
            #Delete anything inside of quotes after the header
            if '"' in line:
                line = re.sub('".*?"', '', line)
                outfile.write(line)

            #Write everything else 
            else:
                outfile.write(line)
                
    os.remove(sourcefilepath+file_cwe129)              
    os.rename(sourcefilepath+new_file_cwe129, sourcefilepath+file_cwe129 )
                
            
def removeEmptyLine129():

   with open(sourcefilepath+file_cwe129) as infile, open(sourcefilepath+ new_file_cwe129, 'w') as outfile:
     for line in infile:
         if not line.strip(): continue  # skip the empty line
         outfile.write(line)  # non-empty line. Write it to output
        
   os.remove(sourcefilepath+file_cwe129)              
   os.rename(sourcefilepath+ new_file_cwe129, sourcefilepath+file_cwe129)       
         
   with open(sourcefilepath+file_cwe129) as fin, open(sourcefilepath+ new_file_cwe129, 'w') as fout:
    for line in fin:
        fout.write(line.replace('\t', ''))
        
   os.remove(sourcefilepath+file_cwe129)              
   os.rename(sourcefilepath+ new_file_cwe129, sourcefilepath+file_cwe129)
        
def removeIndent():
    
    inf = open(sourcefilepath+file_cwe129)
    stripped_lines = [l.lstrip() for l in inf.readlines()]
    inf.close()

# write the new, stripped lines to a file
    outf = open(sourcefilepath+ new_file_cwe129, "w")
    outf.write("".join(stripped_lines))
    outf.close()
    
    os.remove(sourcefilepath+file_cwe129)              
    os.rename(sourcefilepath+ new_file_cwe129, sourcefilepath+file_cwe129)
    
def replaceVar():
    
    with open(sourcefilepath+file_cwe129) as f:
        lines = f.read().replace("data","user_variable").replace("badPrivate","user_variable").replace("readerBuffered","user_variable").replace("dbConnection ","user_variable").replace("socket","user_variable").replace("bad","user_method").replace("good","user_method")
    with open(sourcefilepath+ new_file_cwe129,"w") as f1:
        f1.write(lines)
     
    os.remove(sourcefilepath+file_cwe129)              
    os.rename(sourcefilepath+ new_file_cwe129, sourcefilepath+file_cwe129)

def fileInput():
    
    with open(sourcefilepath+file_cwe129, 'r+') as f:
        _text = ''
        for line in f:
            if line.startswith('public void bad') or line.startswith('public void good'):
                _text += '-----------------------------------------------------------------\n'

            _text += line

        f.seek(0)
        f.write(_text)
        f.truncate()
        

removeCurlyBraces129()
# removewordsdoublequotes() 
removeEmptyLine129()
removeIndent()
fileInput()
removeSpecLines129()
removeSpecWord()
replaceVar()