import time
import os

millis = int(round(time.time() * 1000))
count = 0
while int(round(time.time() * 1000))<=millis+10000:
	count += 1
	os.system("cal >> a.txt")
os.system("printf 'Count: \n\n{}'' >> a.txt".format(count))


millis=$(date +%s)
count=0
endtime=$((millis+10))
while [ "$millis" -lt "$endtime" ]
do
	count=$((count+1))
	cal >> a.txt
done
printf 'Count: \n\n$count' >> a.txt