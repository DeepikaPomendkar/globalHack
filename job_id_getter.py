import requests 
import json
URL = "https://jpmc.fa.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values,requisitionList.requisitionFlexFields&finder=findReqs;siteNumber=CX_1001,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BWORKPLACE_TYPES%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=1000,sortBy=POSTING_DATES_DESC,offset={}" 

f = open("E:/PythonProjects/globalHack/new_job_ids.txt", "a")
count = 0
offset = 0

while offset <8000:
    try:
        new_url = URL.format(offset)
        r = requests.get(new_url) 
        data = json.loads(r.content)
        for i in data["items"]:
            if i.get("requisitionList"):
                for job in i["requisitionList"]:
                    count = count    +1
                    f.write(job["Id"])
                    f.write("\n")
        offset = offset + 200
        print("Offset:" + str(offset))
        print("Count:" + str(count))
    except Exception as ex:
        print(new_url)
f.close()
