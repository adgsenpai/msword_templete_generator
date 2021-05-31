# msword_templete_generator
python program to convert data dictionaries to replace fields in word document

# Usage
```
pip install msworddictreplacer
```
# Application and Code Implementation
```
#replace variables with values

import mswordreplacerdict

yourdict = {
       "${yourvarname}: "what_ever_data_you_want"
    }

filetemplete = "templete.docx"

outputpath = "outputpath.docx"

mswordreplacerdict.ProcessDocument(filetemplete,outputpath,yourdict)

```

# Code Documentation and Functionality

```
1. to use program replace variables dictionary to your variables in your document

 variables = {
       "${yourvarname}: "what_ever_data_you_want"
    }

${yourvarname} indicates the field in word document to be replaced by.
"what_ever_data_you_want" is the field to be replaced by in word document


```
```
2. append your input and output file paths

    template_file_path = 'test.docx'
    output_file_path = 'result.docx'

replace 'test.docx' to your file that you wanna append
replace 'result.docx' to your output file
```
```
3. Run Script
```

# Requirements
```
pip install python-docx
```
# Diagram
<img src="https://raw.githubusercontent.com/ADGVLOGS/msword_templete_generator/main/doc.PNG">
 
