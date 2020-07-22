import sys
import time
import json

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: expecting two parameters")
        exit(1)
    key = sys.argv[1]
    val = sys.argv[2]
    try:
        utc = int(time.mktime(time.strptime(val, "%m/%d/%YT%H:%M:%S")))
    except ValueError:
        print("Error: bad time string\n Usage e.g. 07/22/2020T12:00:00")
        exit(1)
    print("{} {}".format(key, utc))
    dat = []
    with open("unique.json", "r") as f:
        dat = json.load(f)
        dat[key] = utc
    with open("unique.json", "w") as f:
        json.dump(dat, f)
