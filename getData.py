import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import os

slangList = ['Trump']

for slang in slangList: 
    params = {
        "content": slang,
        "year_start": "1960",
        "year_end": "2020"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
    }

    #Grab the NGRAM Data
    html = requests.get("https://books.google.com/ngrams/json", params=params, headers=headers, timeout=30).text
    time_series = pd.read_json(html, typ="series")
    
    #Then Formats the Data into A Nice List
    dataToSlice = str(time_series[0])
    startPoint = dataToSlice.find("[") + 1
    endPoint = dataToSlice.find("]")
    dataToFormat = dataToSlice[startPoint:endPoint]
    data = dataToFormat.split(",")
    
    with open(f'Data\{slang}.csv', 'w', newline="") as csvfile:   #Create New CSV File
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        startingYear = params.get('year_start')  
        YearInt = int(startingYear) 
        
        for eachValue in data:
            toWrite = [(YearInt),(eachValue)]
            YearInt = YearInt + 1
            filewriter.writerow(toWrite)
       
        csvfile.close()
