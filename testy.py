import my_sort
import random
import time
import string

 test = list(string.ascii_lowercase*444)
 random.shuffle(test)
 test = ''.join(test)


 # Sorowanie babelkowe

 t1 = time.time()
 sb = my_sort.sortowanie_babelkowe(test)
 t2 = time.time()
 print "Sorowanie babelkowe zajelo", round(t2 - t1, 4), "sekund."

 # Sortowanie przez wstawianie

 t1 = time.time()
 spw = my_sort.sortowanie_przez_wstawianie(test)
 t2 = time.time()
 print "Sortowanie przez wstawianie zajelo", round(t2 - t1, 4), "sekund."

 # Szybkie sorowanie

 t1 = time.time()
 ss = ''.join(my_sort.szybkie_sortowanie(test))
 t2 = time.time()
 print "Szybkie sortowanie zajelo", round(t2 - t1, 4), "sekund."

 assert sb == spw == ss

my_sort.sortowanie_babelkowe('losiu')
