import webbrowser
import schedule
import time
from tkinter import *

url="https://teams.microsoft.com/_#/school/conversations/General?threadId=19:1382a9071b3c4aafb644598ae8efda65@thread.tacv2&ctx=channel"




def openClassReal(a):
        print('ok')
        webbrowser.open_new(a)
def openClass():
        openClassReal(url)
        root.destroy()
def closeWindow():
    root.destroy()





def DoStuff():
    url=url_entry.get()
    time=time_entry.get()
    day=day_entry.get().strip().lower()
    print(day)
    def openClass():
        openClassReal(url)


    if(day=="sunday"):
        schedule.every().sunday.at(time).do(openClass)
        root.destroy()
        while True:
            schedule.run_pending()
    if(day=="monday"):
        schedule.every().monday.at(time).do(openClass)
        root.destroy()
        while True:
            schedule.run_pending()
    if(day=="tuesday"):
        schedule.every().tuesday.at(time).do(openClass)
        root.destroy()
        while True:
            schedule.run_pending()
    if(day=="wednesday"):
        schedule.every().wednesday.at(time).do(openClass)
        root.destroy()
        while True:
            schedule.run_pending()
    if(day=="thursday"):
        schedule.every().thursday.at(time).do(openClass)
        root.destroy()
        while True:
            schedule.run_pending()
    if(day=="friday"):
        schedule.every().friday.at(time).do(openClass)
        root.destroy()
        while True:
            schedule.run_pending()
    if(day=="saturdayday"):
        schedule.every().saturdayday.at(time).do(openClass)
        root.destroy()
        while True:
            schedule.run_pending()
    


    
    
  


# print("                                                                      ")
# print ("                                             ZOOM CLASS SCHELDULER")
# print("=========================================================================================================================")
# print("                                                                      ")
# site=input("Please Enter the link to your zoom class: ")
# print("                                                                      ")
# time=input("Please Enter the time of your zoom class(e.g: 05:12): ")
# print("                                                                      ")
# DoStuff(site, time)


#========================================================================

#           CREATING THE GUI

#========================================================================
root=Tk()
root.geometry('500x600')
root.configure(background="#F9E79F")
root.title("Zoom Class Scheduler")

empty=Label(root,text="               ",bg="#F9E79F").grid(row=0,column=0)
empty=Label(root,text="               ",bg="#F9E79F").grid(row=1,column=0)
title_label=Label(root, text="  ZOOM CLASS SCHEDULER  ",bg='#C2F77B',fg="#444",font=("Cambria",18)).grid(row=2,column=1)

empty=Label(root,text="               ",bg="#F9E79F").grid(row=3,column=0)
empty=Label(root,text="               ",bg="#F9E79F").grid(row=4,column=0)

Label0=Label(root,text="Enter the day of the week (e.g. sunday): ",bg="#F9E79F",font="Cambria").grid(row=5,column=1)
day_entry = Entry(root, font="Cambria",width=40)
day_entry.grid(row=6,column=1)

empty=Label(root,text="               ",bg="#F9E79F").grid(row=7,column=0)

Label1=Label(root,text="Enter the url of your zoom meeting: ",bg="#F9E79F",font="Cambria").grid(row=8,column=1)
url_entry = Entry(root, font="Cambria",width=40)
url_entry.grid(row=9,column=1)
empty=Label(root,text="               ",bg="#F9E79F").grid(row=10,column=0)

Label2=Label(root,text="Enter the time of your zoom meeting (e.g. 05:05):",bg="#F9E79F",font="Cambria").grid(row=11,column=1)
time_entry = Entry(root, font="Cambria",width=40)
time_entry.grid(row=12,column=1)

empty=Label(root,text="               ",bg="#F9E79F").grid(row=13,column=0)

button = Button(root, text='Enter Automatically',command=DoStuff).grid(row=14,column=1)
empty=Label(root,text="               ",bg="#F9E79F").grid(row=15,column=0)

Label2=Label(root,text="The screen will close once you click the button.",bg="#F9E79F",font="Cambria").grid(row=17,column=1)
Label2=Label(root,text=" But don't panic. ",bg="#F9E79F",font="Cambria").grid(row=18,column=1)
Label2=Label(root,text=" The programme will still run in the background",bg="#F9E79F",font="Cambria").grid(row=19,column=1)
empty=Label(root,text="               ",bg="#F9E79F").grid(row=20,column=0)

Label2=Label(root,text="It's been a long day. Go sleep now...",bg="#F9E79F",font="Cambria").grid(row=21,column=1)


root.mainloop()