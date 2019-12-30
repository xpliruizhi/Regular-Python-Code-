# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:02:04 2019

@author: xplir
A card recorder with UI interaction

"""
import tkinter

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

def hit_me(myCardGame,myinput,list_box):
    #print("hit success")

    myCardGame.change(myinput)
   # myCardGame.display()  
    # update Listbox
    list_card = list(myCardGame.CardSet.keys())
    if list_box.size()>0 and len(list_card)>0:
        list_card.reverse()
        #print(list_card)
        myindex = list_card.index(myinput)
        list_box.delete(myindex)
        list_box.insert(myindex,'{key}:{value}'.format(key = myinput, value = myCardGame.CardSet[myinput]))    

def restart_game(myCardGame,list_box):
    myCardGame.init()
    list_box.delete(0,tkinter.END)
    for key,value in myCardGame.CardSet.items():
        list_box.insert(0,'{key}:{value}'.format(key = key, value = value))
      
myCardGame = Cardgame()
myCardGame.init()
#myCardGame.display()

master = tkinter.Tk()
master.title("Auto Card Record Machine")
master.geometry("700x450")
main_win = tkinter.Label(master,text="Push the button to adjust the Card Number")
main_win.pack()

my_new = set(myCardGame.CardSet.keys())
list_box = tkinter.Listbox(master,height=15,selectmode="BROWSE")
list_box.place(x=100,y=100)
#list_box.insert(0,"a")

for key,value in myCardGame.CardSet.items():
    list_box.insert(0,'{key}:{value}'.format(key = key, value = value))


icount = 0
createVar = locals()
for content in myCardGame.CardSet.keys():
    print(content)
    createVar["b"+str(content)] = tkinter.Button(master, text=str(content), width=5,command=lambda x= myCardGame, y=str(content),z=list_box :hit_me(x,y,z)).place(x=icount*50,y=50)
    icount += 1

restart_btn = tkinter.Button(master, text="Restart", width=5,command=lambda x= myCardGame, z=list_box :restart_game(x,z)).place(x=250,y=100)

#new_set = [1,2,3,4,5,6]

#myListbox = tkinter.Listbox(master)
master.mainloop()





##### Work in CMD, no interface###########
#index =  True
#while(index == True):
#    myinput_ = input("pls input a card:")
#    myinput_list = myinput_.split(' ')
#    #print(myinput)
#    for myinput in myinput_list:
#        if (myinput=="r"):
#            index = False
#            print("quit the game")
#            break
#        if (myinput=="0"):
#            print("restart te game")
#            myCardGame.init()
#            break
#        myCardGame.change(myinput)
#    myCardGame.display()
#myCardGame.display()



    