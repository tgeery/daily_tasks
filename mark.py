import json
import sys
import time
import datetime
import os


LOG_FNAME="history.log"


class Element:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.parents = []

    def setValue(self, v):
        self.val = int(v)

    def getValue(self):
        return self.val

    def getKey(self):
        return self.key

    def addParent(self, obj):
        self.parents.append(obj)

    def getParents(self):
        return self.parents


def add_to_history(key, ts):
    if not os.path.isfile(LOG_FNAME):
        open(LOG_FNAME, "a")
    with open(LOG_FNAME, "a") as f:
        f.write("{}={}\n".format(key, int(ts)))


def iterate_objs(json_dat, curr_time, el):
    for obj in json_dat:
        if type(json_dat[obj]) != int:
            el.addParent(obj)
            iterate_objs(json_dat[obj], curr_time, el)
        else:
            if obj == el.key:
                el.setValue(curr_time.timestamp())
                add_to_history(obj, curr_time.timestamp())


if __name__ == "__main__":
    el = Element(sys.argv[1], 0)
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    with open("repeating.json", "r") as f:
        repeat_json = json.loads(f.read())
        iterate_objs(repeat_json, timestamp, el)
        if el.getValue() != 0:
            f.close()
            with open("repeating.json", "w") as f:
                obj = repeat_json
                for p in el.getParents():
                    obj = obj[p]
                obj[el.getKey()] = el.getValue()
                json.dump(repeat_json, f)