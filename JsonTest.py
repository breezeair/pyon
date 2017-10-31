import json

di = [{"name":"test1", "sex":"test2", "others":[1,2,"8888888"]}]
# print(json.dumps(di, indent=4))
# new_dict = json.dumps(di, indent=4)

# with open("record.json", "a") as f:
#     json.dump(di, f, indent=4, separators=(',',':'), ensure_ascii=False)
#     print("加载入文件完成...")

with open("record.json", "r") as f:
    date = json.load(f)
print(date)
date += di
print(date)

with open("record.json", "w") as f:
    json.dump(date, f, indent=4, separators=(',',':'), ensure_ascii=False)

#     json.dump(di, date)
#     json.dump(di, f, indent=4, separators=(',',':'), ensure_ascii=False)

# readed = json.load(open('record.json', 'r'))
# readed = json.dumps(di)
# json.dump(readed, open('record.json', 'w'))