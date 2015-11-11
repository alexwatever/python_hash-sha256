import hashlib
import csv

# open list of emails
with open("list.txt") as f:
    data = f.readlines()

# create file
file = csv.writer(open("hashes.csv", "w"))

# write headers
file.writerow(["Original", "Hashed"])


# create number for logging lines
num = 1

# start looping through emails
for e in data:

    # write to file
    file.writerow([e, hashlib.sha256(e).hexdigest()])

    # log line
    print 'Line %d is written.' % num
    num += 1

print 'All done.'


