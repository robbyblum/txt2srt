# written by deciMae, minorly edited by glumbaron

import sys


if len(sys.argv) - 1 != 2 and len(sys.argv) - 1 != 3:
    print("Error: Wrong amount of arguments")
    print("""USAGE: python test.py importfile exportfile maxtime
    maxtime is optional; leaving it off will default all captions to 1s long
    time format: mm:ss""")
    exit()


exportf = sys.argv[2]
importf = sys.argv[1]
if len(sys.argv) - 1 == 3:
    maxmins, maxsecs = sys.argv[3].split(":")
    maxtime = int(maxmins) * 60 + int(maxsecs)
else:
    maxtime = 0

try:
    file = open(importf, "r")
except:
    print("Error: file not found")

numlines = sum(1 if line != "\n" else 0 for line in open(importf, "r"))

if maxtime != 0:
    timedelta = maxtime / numlines
else:
    timedelta = 2

outfile = open(exportf, "w")
i = 0
for x in file:
    if x == "\n":
        continue
    outfile.write(str(i) + "\n")
    time = i * timedelta
    nexttime = (i + 1) * timedelta
    hour = int(time / 3600)
    min = int(time / 60) % 60
    sec = int(time) % 60
    nexthour = int(nexttime / 3600)
    nextmin = int(nexttime / 60) % 60
    nextsec = int(nexttime) % 60
    outfile.write("%02d:%02d:%02d,000 --> %02d:%02d:%02d,000\n" %
                  (hour, min, sec, nexthour, nextmin, nextsec))
    outfile.write(x + "\n")
    i += 1
