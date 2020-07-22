import json
import time


def is_today(curr, last):
    if curr.tm_year != last.tm_year:
        return False
    if curr.tm_mon != last.tm_mon:
        return False
    if curr.tm_mday != last.tm_mday:
        return False
    return True


def iterate_objs(json_dat, completed, incomplete, curr_time):
    for obj in json_dat:
        if type(json_dat[obj]) != int:
            iterate_objs(json_dat[obj], completed, incomplete, curr_time)
        else:
            last_time = time.localtime(json_dat[obj])
            if is_today(curr_time, last_time) == True:
                completed.append((obj, "{}:{}:{}".format(last_time.tm_hour, last_time.tm_min, last_time.tm_sec)))
            else:
                incomplete.append(obj)


if __name__ == "__main__":
    timestamp = time.localtime()
    completed = []
    incomplete = []
    with open("repeating.json") as f:
        repeat_json = json.loads(f.read())
        iterate_objs(repeat_json, completed, incomplete, timestamp)
    print("Still need to do:")
    for i in incomplete:
        print(i)
    print("\nCongrats completing:")
    for i in range(0, len(completed)):
        print("{} at {}".format(completed[i][0], completed[i][1]))
