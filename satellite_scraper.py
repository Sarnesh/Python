import requests
import pandas
from bs4 import BeautifulSoup

satellite_website = requests.get("https://spaceflightnow.com/launch-schedule/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
info = satellite_website.content

soup = BeautifulSoup(info,"html.parser")

all_content = soup.find_all("div",{"class":"entry-content clearfix"})

data_list = []

for items in all_content:
    
    date = items.find_all("span",{"class":"launchdate"})
    mission = items.find_all("span",{"class":"mission"})
    launch_time = items.find_all("span",{"class":"strong"})
    data = items.find_all("div",{"class":"missiondata"})
    
    
    for date, mission, launch_time, data in zip(date, mission, launch_time, data):
        
        satellite_dictionary = {}
        
        try:
            satellite_dictionary["Launch Date"]=date.text.replace("\n","").replace(" "," ")
        except:
            pass

        try:
            satellite_dictionary["Mission"]=mission.text.replace("\n","").replace(" "," ")
        except:
            pass

        try:
            satellite_dictionary["Launch Time"]=launch_time.text.replace("\n","").replace(" "," ")
        except:
            pass
        
        try:
            satellite_dictionary["Data"]=data.text.replace("\n","").replace(" "," ")
        except:
            pass
        
       
        data_list.append(satellite_dictionary)

df=pandas.DataFrame(data_list)

df.to_csv("Current_Missions.csv")
