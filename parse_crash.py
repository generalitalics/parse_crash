# -*- coding: utf-8 -*-

import os
import re
import sys
from datetime import datetime

time_start = datetime.now()
print os.path
source = os.path.join(".", sys.argv[1])
print 'sys.argv[0] = '+sys.argv[0]
print 'sys.argv[1] = '+sys.argv[1]
#source = sys.argv[1] - путь к файлу
print 'source = ' + source
data = None
with open(source) as f:
    lines = f.readlines()


res_dir = os.path.join(".", "results")
print 'res_dir = '+res_dir
if not os.path.exists(res_dir):
    os.makedirs(res_dir)
# makedirs - создает папку по директории с результатами, если ее нету
result = {}
#line - это строка во всем lines
for line in lines:
    # в переменную l записывается list со значениями из каждого line
    print line
    l = line.split(",")
    key = l[5]
    # с помощью регулярных выражений убираем лишнее
    key = re.sub(r"\d+-\d", "", key)
    key = re.sub(r"\d+$", "", key)
    if result.get(key, False) is False:
        result[key] = []
    result[key].append("|".join(l))

for k, s in result.iteritems():
    text = "".join(s)
    with open(os.path.join(".", res_dir, k + ".csv"), "w") as w:
        w.write(text)

time_end = datetime.now()
time_delta = time_start - time_end
print "Total time: %d s" % -time_delta.total_seconds()