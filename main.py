#import and headers
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
req = urllib.request.Request(
    url="http://stats.espncricinfo.com/ci/engine/player/253802.html?class=2;template=results;type=batting;view=innings", 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)


#DATES column
f = urllib.request.urlopen(req)
soup = BeautifulSoup(f, 'lxml')
type(soup)
dates=[None]*235 #ADD HERE
i=0
count=0
for ana in soup.find_all('b'):
    if i<=2 or i>224: # ADD HERE to ONLY 2nd i.
        count+=1
    else:
        dates[i]=ana.text
    i+=1


while None in dates:
    dates.remove(None)
print(dates)  


#RUNS column
count=0
i=0
runs=[None]*224 #ADD HERE
for tr in soup.find_all('tr', attrs={'class':'data1'}):
    td = tr.find('td')
    if i==0:
        count=1
        
    else:
        runs[i-1]=td.text
    i=i+1

#Combining the 2 columns
combined = list(zip(dates,runs))
#print(combined)
print(len(combined))
test=['DNB', 'TDNB']
total_DNB=0
for x in range(1,len(combined)):
    if combined[x][1] in test:
        total_DNB+=1
updated_len=len(combined)-total_DNB   
#print(total_DNB)
for x in range(1,updated_len):
    if combined[x][1] in test:
        del combined[x]
        
#print(combined)   

#CONVERT to format for CSV
newl=combined
nostr = str.maketrans("", "", "*")
KohliF=[None]*len(newl)
for x in range(0,len(newl)):
    KohliF[x]=list(newl[x])
    KohliF[x] = [s.translate(nostr) for s in KohliF[x]]
    

#print(KohliF)

#EXPORT to CSV
with open("kly.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(KohliF)

