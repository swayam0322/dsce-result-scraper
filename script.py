from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
with open("ECE.txt","r") as f:
    for u in f:
        striped = u.strip()
        url = "http://14.99.184.178:8080/birt/output?__report=mydsi/exam/Exam_Result_Sheet_dsce.rptdesign&USN="+striped+"&&__format=html&__pageoverflow=0&__overwrite=false"
        try:
            html = urlopen(url).read()
        except:
            print(striped)
            time.sleep(1)
            html = urlopen(url).read()
        finally:
            time.sleep(3)
            html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = [chunk for chunk in chunks if chunk]
        USN,GPA,name= text[9],text[-5],text[7]
        with open('data.csv', 'a') as data:
            data.write(USN+","+name+","+GPA+"\n")