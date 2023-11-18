import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker


import numpy as np
import csv
 

slangList = ['Shit','Fuck']

def createFrequencyGraph(years, values):
    floatValues = []
    
    for eachValue in values:
        floatValues.append(float(eachValue))    
    fig, ax = plt.subplots()
    ax.tick_params(axis="x",which='major',)
    ax.xaxis.set_major_locator(ticker.MaxNLocator())

    #ax.yaxis.set_major_formatter(FormatStrFormatter('%.10f'))
    ax.plot(years,floatValues)
    ax.set_title(f'Relative Frequency of {slang}')
    fig.supxlabel('Year')
    fig.supylabel(f'Relative Use/Yr')
    fig.savefig(f"ProcessedData/{slang}-Frequency")

   
    
def createRateChangeGraph(years, values):
    years.pop(len(years) - 1)
    fig2, ax = plt.subplots()
    ax.plot(years,values)
    ax.xaxis.set_major_locator(ticker.AutoLocator())
    fig2.supxlabel('Year')
    fig2.supylabel('Rate of Change (Relative Use/Yr)')
    ax.set_title(f'Rate of Change of Relative Use of {slang}')
    fig2.savefig(f"ProcessedData/{slang}-ROC")
    

def normalizeData(input):
    output = []
    minInput = float(min(input))
    maxInput = float(max(input))
    range = maxInput - minInput
    
    for eachItem in input:
        currentItem = float(eachItem)
        toAdd = ((currentItem - minInput) / range)
        output.append(toAdd)
        #print(toAdd)
        
    return output
        
def findRateOfChange(input):
    output = []
    index = 1
    
    while index < len(input):
        toAdd = (float(input[index])) - float(input[index - 1]) 
        output.append(float(toAdd))
        index = index + 1
    
    return output

def convertToDecimal(input):
    output = []
    
    for eachRow in input:
        output.append(("%.17f" % (float(eachRow))).rstrip('0').rstrip('.'))

    #outPutFloat = []
    
    #for eachValue in output:
    #    outPutFloat.append((eachValue))
        
    #print(outPutFloat)
    
    return output

for slang in slangList:
    dataYears = []
    dataValues =[]
    
    with open(f'Data\{slang}.csv', 'r') as csvfile:   #Open Relevant Data File
        filereader= csv.reader(csvfile, delimiter=',') 
        for row in filereader:
            #extractData 
            dataYears.append(row[0])
            dataValues.append(row[1])
        
        #Convert From Scientific Notation to Decimal  
        dataValues = convertToDecimal(dataValues)   
        
    csvfile.close()  
    
    freqValues = normalizeData(dataValues)  #
    createFrequencyGraph(dataYears, dataValues)
    rateOfChangeValues = findRateOfChange(dataValues)
    #rateOfChangeValues = normalizeData(rateOfChangeValues)
    createRateChangeGraph(dataYears, rateOfChangeValues)
    