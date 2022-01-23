import requests
import json

list = [] #list that has the info
list.append(input("Name: "))
list.append(input("Email Address: "))
list.append(input("Phone Number: "))
file = open('testPrint.txt','w')
file.truncate(0)
for item in list:
    r = requests.get("https://serpapi.com/search.json?engine=google&q="+item.replace(" ","+")+"&num=50&api_key=204efcd56a57bee1a50277f9f8fd5bdfe8ac4e45deb15d0e2d0c77afb0d15d88")
    r = r.json()
    if 'organic_results' in r:
        for i in r['organic_results']:
            if 'snippet' in i:
                if item in i['snippet']:
                    file.write(i['title'] + "\n")
                    file.write(i['snippet'] + "\n")
                    file.write(i['link'] + "\n" + "\n")
                    print(i['title'])
                    print(i['snippet'])
                    print(i['link'] + "\n")
file.close()
# input()