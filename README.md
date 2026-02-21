# Coding Notes

## …or push an existing repository from the command line

Git Bash
``` bash
git remote add origin git@github.gov:progressivepull/PythonCode.git
git branch -M main
git push -u origin main
```

## Change Directory

Git Bash
``` bash
$ cd /C/PythonCode
```

Anaconda Powershell Prompt
```
(base) PS C:> cd C:\PythonCode\
```

# Programs

## Defaultdict Python Method

* [Defaultdict.py](https://github.com/progressivepull/AI-Python-Code/blob/main/Syntax/Defaultdict.py)

This Python example demonstrates how to use **defaultdict** from the **collections** module to automatically create dictionary values with a default type.

A **defaultdict(list)** is created, which means that if a key does not already exist in the dictionary, it will automatically be assigned an empty list as its default value. This allows you to append items to a key without first checking whether the key exists.

In the example, items are grouped into two categories: **fruits** and **vegetables**. The program appends several fruit names **(apple, banana, melons)** to the **'fruits'** key and several vegetable names **(carrot, peas, tomato)** to the **'vegetables'** key. Since defaultdict automatically initializes missing keys with empty lists, no prior key setup is required.

Finally, the program prints:

The entire dictionary.

1. A separator line.
2. The list of fruits.
3. The list of vegetables.

This example shows how **defaultdict** simplifies grouping and organizing data without needing to manually check for key existence.

Anaconda Powershell Prompt
```
(base) PS C:\PythonCode\Syntax> python .\Defaultdict.py
defaultdict(<class 'list'>, {'fruits': ['apple', 'banana', 'melons'], 'vegetables': ['carrot', 'peas', 'tomato']})
_______________________
 fruits : ['apple', 'banana', 'melons']
vegetables: ['carrot', 'peas', 'tomato']
```

## Next Word Predicted

* [Corpus.py](https://github.com/progressivepull/AI-Python-Code/blob/main/NextWord_PREDICATE/Corpus.py)

This Python program builds a simple word prediction model by analyzing pairs of consecutive words in a small text sample and storing possible next words for each word. When given an input word, it randomly selects and returns one of the words that previously followed it in the text.

Anaconda Powershell Prompt
``` 
(base) PS C:\PythonCode\NextWord_PREDICATE>python ./Corpus.py
Input: 'the'
Predicted next word: 'worst'
```

## Test If Can Read Microsoft Excel Document

* [run.py](https://github.com/progressivepull/AI-Python-Code/blob/main/Util/Excel_PRINT/run.py)
* [vehicle.xlsx](https://github.com/progressivepull/AI-Python-Code/blob/main/Util/Excel_PRINT/vehicle.xlsx)

This Python script uses pandas to read an Excel file named vehicle.xlsx, display its structure (columns, data types, and first five rows), and then filter the data based on specific vehicle colors. It selects and prints only the rows where the colors column contains "Black", "Blue", or "Red".

Anaconda Powershell Prompt
``` 
(base) PS C:\PythonCode\Util\Excel_PRINT> python .\run.py
=== File Structure ===
Columns: ['colors', 'owners', 'make', 'model', 'home town']

Data Types:
colors       object
owners        int64
make         object
model        object
home town    object
dtype: object

First 5 Rows:
   colors  owners       make   model home town
0     Red       1     Toyota   Camry    Dallas
1    Blue       2      Honda   Civic   Atlanta
2   Black       1       Ford   F-150    Denver
3   White       3  Chevrolet  Malibu   Chicago
4  Silver       2     Nissan  Altima   Phoenix

=== Black, Blue, and Red Vehicles ===
  colors  owners    make  model home town
0    Red       1  Toyota  Camry    Dallas
1   Blue       2   Honda  Civic   Atlanta
2  Black       1    Ford  F-150    Denver

``` 
## Check if "pandas", "sklearn", "openpyxl" is Installed

* [Lib_Installed_CHECK.py](https://github.com/progressivepull/AI-Python-Code/blob/main/Util/Lib_Installed_CHECK.py)

This Python script checks whether specific libraries are installed in the current environment using the **importlib.util** module.

A list of library names **(pandas, sklearn, and openpyxl)** is defined. The script loops through each library and uses **importlib.util.find_spec()** to determine if the module can be found. If the function returns a valid result (not **None**), it means the library is installed, and the script prints **"yes"** next to its name. If it returns None, the library is not available, and the script prints **"no"**.

A note in the code explains that although the package is installed as **scikit-learn**, it is imported using the name **sklearn**. This example demonstrates a simple way to programmatically verify whether required dependencies are available before running a program.

Anaconda Powershell Prompt
``` 
(base) PS C:\PythonCode\Util> python .\Lib_Installed_CHECK.py
pandas: yes
sklearn: yes
openpyxl: yes
``` 


# Income Predicate

* [people.xlsx](https://github.com/progressivepull/AI-Python-Code/blob/main/Income_PREDICATE/people.xlsx)

# Documents
* [AI Terms](https://github.com/progressivepull/AI-Python-Code/blob/main/DOCUMENTS/AI_Terms.docx)
* [ChatGPT Weekly Searches](https://github.com/progressivepull/AI-Python-Code/blob/main/DOCUMENTS/ChatGPT_Weekly_Searches.docx)