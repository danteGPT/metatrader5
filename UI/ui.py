import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from products.productsServices import ProductsServices
from functools import cache
import random

class UI(ProductsServices):
    def __init__(self, mt5):
        super().__init__(mt5)
        self.dataframe = self.teste()
        self.conts = 1
        
    def teste(self):
        preco = self.priceVol()
        return preco
    
    @cache
    def construc(self):
        
        dfvalues = self.priceVol()
        dfindex = self.toTimeFrame()
        print(dfindex)
        time = self.convertToList(dfindex['time'], dfvalues['PVOL'], 'x')
        pvol = self.convertToList(dfindex['time'], dfvalues['PVOL'], 'y')
            #pvol = self.cutListHour(pvol)
            #time = self.cutListHour(time)
        print('aaaa') 
        print(time)
        print('cccc')
        print(pvol)
        position = range(0, 50)   
        #on Dynamic ui    
        plt.ion() 
        plt.subplots(layout='constrained', figsize = (50 , 6))
        #plt.style.use('ggplot') 
        while self.conts <= 20:
            plt.cla()
            plt.clf()
            if len(pvol) > 50:
                pvols = self.maxIndex(pvol, self.conts)
                times = self.maxIndex(time, self.conts)
            else:
                pvols = self.addListDynamics(pvol)
                times = self.addListDynamics(times)           
            self.showGraphBar(position, pvols, times)
            self.conts +=1
            plt.pause(5)        
        plt.ioff()   
        plt.show()
        
    def redBar(self, x, sort):
        maxLen = len(sort)
        reList = []
        for number in x:
            if number != sort[maxLen -1]:
                reList.append(0)
            else:
                reList.append(number)
        print('ahaha')
        print(reList)
        return reList
       
    def showGraphBar(self, position, pvol, time): 
        plt.bar(position, pvol, width= 0.4) 
        self.redBarGraph(pvol, position)   
        plt.xticks(position, time, rotation = 90)
        plt.title('Volume graph')      
              
    def redBarGraph(self, pvol, position):
        pvolSorted = sorted(pvol)
        redbar = self.redBar(pvol, pvolSorted) 
        plt.bar(position, redbar, color = 'red', width = 0.4)
        plt.yticks(pvol)
        #plt.Axes.set_yticklabels(pvolSorted)
        
   
        