# "= heading = " is a heading 
# "== heading == " is a heading
import re 
# Path: dataset.py/test.py
#fething the data from the file\
with open("/workspaces/codespaces-blank/dataset.py/data.txt","r") as f:
    datas = f.read()
    data = datas.split("\n").pop(0)
    #create a list of all the headings
    heading1 = re.search(r'^\s*=\s*([^=]+)\s*=\s*$', datas, re.MULTILINE).group(1)
    headings =re.findall("\n={2}\s(?P<header>.+?)\s={2}\n", datas)
    print(headings)
    print(heading1)
    