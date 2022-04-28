import re
import sys
import glob
import os
import fileinput
import csv

sourcefilepath = 'C:\\Users\\User\\Desktop\\Java\\codes\\'

read_cwe23 = glob.glob("C:\\Users\\User\\Desktop\\Java\\codes\\CWE23_Relative_Path_Traversal\\*.java")

file_cwe23='CWE23_Relative_Path_Traversal.txt'

new_file_cwe23='CWE23_Relative_Path_Traversal1.txt'
            
 
def removeCurlyBraces():
    
    with open(sourcefilepath+file_cwe23, 'r') as my_file:
        text = my_file.read()
        text = text.replace("{", "")
        text = text.replace("}", "")
        

# save the updates back into a cleaned up file
    with open(sourcefilepath+file_cwe23, 'w') as my_file:
        my_file.write(text)
        
def removeSpecLines():

    bad_words = ['import', 'try', 'catch', 'finally', 'else', 'CWE']

    with open(sourcefilepath+file_cwe23) as oldfile, open(sourcefilepath+ new_file_cwe23, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
    
    os.remove(sourcefilepath+file_cwe23)              
    os.rename(sourcefilepath+new_file_cwe23, sourcefilepath+file_cwe23 )
                

def removeSpecWord():
    
    delete_list = ["goodG2B"]
    with open(sourcefilepath+file_cwe23) as fin, open(sourcefilepath+ new_file_cwe23, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)
                
    os.remove(sourcefilepath+file_cwe23)              
    os.rename(sourcefilepath+new_file_cwe23, sourcefilepath+file_cwe23 )
    
def removewordsdoublequotes():
    
    with open(sourcefilepath+file_cwe23) as infile, open(sourcefilepath+ new_file_cwe23, 'w') as outfile:
        for line in infile:
            #Delete anything inside of quotes after the header
            if '"' in line:
                line = re.sub('".*?"', '', line)
                outfile.write(line)

            #Write everything else 
            else:
                outfile.write(line)
                
    os.remove(sourcefilepath+file_cwe23)              
    os.rename(sourcefilepath+new_file_cwe23, sourcefilepath+file_cwe23 )            

def removeEmptyLine():

   with open(sourcefilepath+file_cwe23) as infile, open(sourcefilepath+ new_file_cwe23, 'w') as outfile:
     for line in infile:
         if not line.strip(): continue  # skip the empty line
         outfile.write(line)  # non-empty line. Write it to output
        
   os.remove(sourcefilepath+file_cwe23)              
   os.rename(sourcefilepath+ new_file_cwe23, sourcefilepath+file_cwe23)       
         
   with open(sourcefilepath+file_cwe23) as fin, open(sourcefilepath+ new_file_cwe23, 'w') as fout:
    for line in fin:
        fout.write(line.replace('\t', ''))
        
   os.remove(sourcefilepath+file_cwe23)              
   os.rename(sourcefilepath+ new_file_cwe23, sourcefilepath+file_cwe23)
        
def removeIndent():
    
    inf = open(sourcefilepath+file_cwe23)
    stripped_lines = [l.lstrip() for l in inf.readlines()]
    inf.close()

# write the new, stripped lines to a file
    outf = open(sourcefilepath+ new_file_cwe23, "w")
    outf.write("".join(stripped_lines))
    outf.close()
    
    os.remove(sourcefilepath+file_cwe23)              
    os.rename(sourcefilepath+ new_file_cwe23, sourcefilepath+file_cwe23)
    
def replaceVar():
    
    with open(sourcefilepath+file_cwe23) as f:
        lines = f.read().replace("data","user_variable").replace("root","user_variable").replace("socket","user_variable").replace("readerInputStream ","user_variable").replace("readerBuffered","user_variable").replace("streamFileInputSink","user_variable").replace("readerInputStreamSink","user_variable").replace("readerBufferdSink","user_variable").replace("bad","user_method").replace("good","user_method")
    with open(sourcefilepath+ new_file_cwe23,"w") as f1:
        f1.write(lines)
     
    os.remove(sourcefilepath+file_cwe23)              
    os.rename(sourcefilepath+ new_file_cwe23, sourcefilepath+file_cwe23)

def fileInput():
    
    with open(sourcefilepath+file_cwe23, 'r+') as f:
        _text = ''
        for line in f:
            if line.startswith('public void bad()') or line.startswith('public void good()'):
                _text += '-----------------------------------------------------------------\n'

            _text += line

        f.seek(0)
        f.write(_text)
        f.truncate()
     
removeCurlyBraces()
# removewordsdoublequotes()
removeEmptyLine()
removeIndent()
fileInput()
removeSpecLines()
removeSpecWord()
replaceVar()

 