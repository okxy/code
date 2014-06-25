import urllib.request as ur
import time
import random
import os
import re

with open('data.txt', 'r', encoding='utf-8') as f:
    code = f.read()
    data = eval(code[code.find('['):])
    # print(data[:10])

files = os.listdir()
print(files)

for i in data:
    title = i['title'].strip() + r'.pdf'  # well, automatically discarded by os
    url = re.sub('<.*?>', '', i['pdf']).translate(str.maketrans(':/','_-')) + r'?intermediate=true'
    
    if not title in files:
        try:
            ur.urlretrieve(url, title)
            print(title,'downloaded')
            time.sleep(random.randint(3,10))
        except:
            print(title, 'FAILED.')  # to make it easily distinguishable
    else:
        continue
else: print('finished.')
 


	
