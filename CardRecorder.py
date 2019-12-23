# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:02:04 2019

@author: xplir

Easy Function to Record Card of Game DouDiZhu
"""

class Cardgame:
    CardSet = {}
    
    def init(self):
        for i in range(1,11):
            self.CardSet[str(i)] = 4
        self.CardSet["j"] = 4
        self.CardSet["q"] = 4
        self.CardSet["k"] = 4
        self.CardSet["w"] = 2
        #print(self.CardSet)

    def change(self,in_str):
        if in_str in self.CardSet.keys():
            if self.CardSet[in_str] > 0:
                self.CardSet[in_str] = self.CardSet[in_str] - 1
                #self.display()
            else:
                print("There is no card left, Try again pls!") 
        elif in_str!="0" and in_str!="r":
            print("The input string is not valid, Try again pls!") 
            
    def display(self):
        print("The Present Card Left:")
        for key,value in self.CardSet.items():
            print('{key}:{value}'.format(key = key, value = value))
        
myCardGame = Cardgame()
myCardGame.init()
#myCardGame.display()

index =  True
while(index == True):
    myinput_ = input("pls input a card:")
    myinput_list = myinput_.split(' ')
    #print(myinput)
    for myinput in myinput_list:
        if (myinput=="r"):
            index = False
            print("quit the game")
            break
        if (myinput=="0"):
            print("restart te game")
            myCardGame.init()
            break
        myCardGame.change(myinput)
    myCardGame.display()
myCardGame.display()



    