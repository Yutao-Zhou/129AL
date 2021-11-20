import requests

r=requests.get('http://web.physics.ucsb.edu/~phys129/lipman/')
#change the data received to text
rt=r.text
#Find update time we want and deal with unrelated information
rts=rt.split('\n')
for line in rts:
    if line.find("Latest")!=-1:
        line=line.replace('<span class="greenss">','')
        line=line.replace('</span></p>','')
        line=line.replace('&nbsp;',' ')
        print(line)