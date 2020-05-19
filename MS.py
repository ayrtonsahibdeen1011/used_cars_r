
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:26:44 2020.

@author: Ayrton Sahibdeen and friends
"""
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns

import statistics
import random


year    = []
model	= []
price	= []
mileage = []
color	= []
transmission = []
labels = []

filename = 'usedcars.csv'
doc = pd.read_csv('usedcars.csv')
sns.set(style = 'white')

wallet_cash = random.randint(3800,21992) 

def importedData():
    with open(filename, 'r') as populationfile:
        reader = csv.reader(populationfile)
        i = 0
        for col in reader:
            if(i != 0):
                year.append(int(col[0]))
                model.append(col[1])
                price.append(int(col[2]))
                mileage.append(int(col[3]))
                color.append(col[4])
                transmission.append(col[5])
            else:
                labels.append(col[0])
                labels.append(col[1])
                labels.append(col[2])
                labels.append(col[3])
                labels.append(col[4])
                labels.append(col[5])
                
                
                i = 1
          


def promptUser():
    print('Enter:')
    print('1 - Current Statistics of Our Stock! ')
    print('2 - Comparative Analysis in Mileage and Price')
    print('3 - Transmission Distribution Amongst Cars in Stock')
    print('4 - Current Model Price Comparisons')
    print('5 - Make a Purchase!')
    print('6 - Current Auto Stock')



    
def graphlabels(xlabel, ylabel, title):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()

def piegraph():     
    plt.pie(doc['transmission'].value_counts(), labels=['auto', 'manual'])
    plt.axis('equal')
    plt.show()
def stats():
    
    print('Used Cars file preview')
    print('Header')
    print(doc.head(149))
    print('Statiscal Analysis')
    print(doc.describe())                   
                
def swarmplot():
    
    sns.swarmplot(x = 'model', y = 'price', data = doc); 
    
    plt.title('Model price comparison')
    
    plt.show() 
def comparative():
    modelNames = input('Enter Model Name: ')
    if modelNames in model:
        #index = model.index(modelNames)

        year1 = int(input('Enter Year 1: '))
        year2 = int(input('Enter Year 2: '))
        print('Year one Mean Data (Price,Mileage)' )
        meanData1 = getMeanData(modelNames, year1)
        print(meanData1[0:2])
        print('Year two Mean Data (Price,Mileage)')
        meanData2 = getMeanData(modelNames, year2)
        print(meanData2[0:2])

        if year1 in year and year2 in year:
           
            if meanData1[0:1] > meanData2[0:1]:
                print(' Price of ', modelNames, 'is usually more expensive in ', year1)
            if meanData1[1:2] > meanData2[1:2]:
                print('Mileage of', modelNames, 'is usually more in', year1)
            if meanData1[0:1] == meanData2[0:1]:
                print(' Price of ', modelNames, 'is usually equal for ', year1, 'and', year2)
            if meanData1[1:2] == meanData2[1:2]:
                print('The Mileage is equal in both years: ', year1 ,'and', year2)
            if meanData1[0:1] < meanData2[0:1]:
                print(' Price of ', modelNames, 'is more likely to be expensive in ', year2)
            if meanData1[1:2] < meanData2[1:2]:
                print(' Mileage of', modelNames, 'has a higher probability of being more expensive in', year2)
        else:
            print('error, something is wrong')
  
    else:
        print('Model Entered Is Invalid')
        print('\n')


                
def getMeanData(carModel, carYear):
    carPrices   = []
    carMileages = []

    if carYear in year:
        j = 0
        for i in year:
            if carYear == i:
                carPrices.append(price[j])
                carMileages.append(mileage[j])
            j += 1

    meanCarPrice    = statistics.mean(carPrices)
    meanCarMileage  = statistics.mean(carMileages)      
    return [meanCarPrice, meanCarMileage]


def Game():
    if wallet_cash > 3800:
        
        print('Welcome to the Auto Dealing Platform ')
        print('You are given $: ', wallet_cash)
        print('This is the money you have right now!\n\n')
        print('These are your options for buying!')
        print(doc[doc.price < wallet_cash])
    
        idEntered = int(input('\nEnter ID of Car You would like: '))
        carprice = doc.loc[doc.index == idEntered,'price'].values[0]
        print ('Very nice Choice! , it is currently selling for', carprice)
    


        if carprice > wallet_cash:
         print('We are very sorry! You have insufficient funds')
         Game()

        elif wallet_cash >= carprice:     
            print ('Would you like to buy it?')
            print('1 - Yes')
            print('2 - No, let me choose again')
            print('3 - Go to Main Menu')
            opt = input()
            if(opt == '1'):
                print('Congratulations, you now own.. ')
                print(doc.loc[idEntered])
                print('Your current balance is: $', wallet_cash - carprice)
                
                print('please come again!')
                
            if(opt == '2'):
                Game()
            if(opt == '3'):
                print()
                
            
            
        
                
                
def datatypecheck():
    print(doc.info)

def Main():
 
    importedData()

    while True:
        promptUser()
        opt = input()

        if(opt == '1'):
            stats()
        if(opt == '2'):
            comparative()    
        if(opt == '3'):
            piegraph()
        if(opt == '4'):
            swarmplot()
        if(opt == '5'):
            Game()
        if(opt == '6'):
            datatypecheck()
            break
   
    
    
    
    
Main()
