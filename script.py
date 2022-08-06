from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
with open("USN.txt","r") as f:
    sheet = {}
    for line in f:
        striped = line.strip()
        url = "http://14.99.184.178:8080/birt/output?__report=mydsi/exam/Exam_Result_Sheet_dsce.rptdesign&USN="+striped+"&&__format=html&__pageoverflow=0&__overwrite=false"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")  
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        count,usn,sgpa,l=0,"","",[]
        for i in text:
            if(count==9 and i!='\n'):usn+=i
            if(count==83):sgpa+=i
            if(i=='\n'):count+=1
        try:sheet[usn]=float(sgpa)
        except: print(usn)
        with open('data.csv', 'w') as data:
            for key in sheet.keys():
                data.write("%s, %s\n" % (key, sheet[key]))       