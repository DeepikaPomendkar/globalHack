import requests
import json
import pandas as pd
import pprint

URL = 'https://jpmc.fa.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails?expand=all&onlyData=true&finder=ById;Id={id},siteNumber=CX_1001'
job_file = open("E:/PythonProjects/globalHack/job_ids.txt")
jobs = job_file.read()
job_ids = jobs.split("\n")
count = 0
# print(job_ids)

# URL =URL.format(210466831)
# # print(URL)
# r = requests.get(URL)
# data = json.loads(r.content)
# columns = data["items"][0].keys() + data["items"][0].keys()
# print(job_ids)
maindf = pd.DataFrame() 
for id in job_ids:
    # print(id)
    new_url = URL.format(id=str(id))
    # print(new_url)
    r = requests.get(new_url)
    data = json.loads(r.content)
    item = data["items"][0]
    # print(item)
    # print(item.keys())
    # print(item.values())
    location = data["items"][0]["workLocation"][0]
    value = list(item.values()) + list(location.values())
    keys = list(item.keys())+ list(location.keys())
    df = pd.DataFrame([value], columns=keys)
    if maindf.empty:
        maindf = df
    else:
        maindf = pd.concat([maindf, df], ignore_index=True)
        # maindf.append(df)
    if count >1000:
        break
    count+=1
maindf.to_csv('data.csv', index=False) 
