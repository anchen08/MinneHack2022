import requests

list = []
list.append(input("Name: "))
list.append(input("Email Address: "))
list.append(input("Phone Number: "))
for item in list:
    r = requests.get("https://serpapi.com/search.json?engine=google&q="+item.replace(" ","+")+"&num=50&api_key=204efcd56a57bee1a50277f9f8fd5bdfe8ac4e45deb15d0e2d0c77afb0d15d88")
    r = r.json()
    for i in r['organic_results']:
        if item in i['snippet']:
            print(i['title'])
            print(i['snippet'])
            print(i['link']+"\n")
input()