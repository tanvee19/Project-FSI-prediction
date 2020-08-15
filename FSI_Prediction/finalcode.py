import pickle
import numpy as np
import pandas as pd
import webbrowser
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk,StringVar,Frame, Tk, Button
from tkinter.messagebox import showinfo       
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from PIL import Image, ImageTk

with open('model_pickle','rb') as f: 
    classifier = pickle.load(f)
data = pd.read_csv('data.csv', delimiter = ',')
list_col=['Country', 'Year', 'Rank', 'Total', 'Security Apparatus',
       'Factionalized Elites', 'Group Grievance','Economy',
       'Economic Inequality', 'Human Flight and Brain Drain',
       'State Legitimacy', 'Services', 'Human Rights',
       'Demographic Pressures', 'Refugees and IDPs',
       'External Intervention']

def pred_class(l):
    # for prediction of FSI Class
    l=np.array(l)
    l=l.reshape(1,-1)
    pred_1=classifier.predict(l)
    return pred_1

def pred_value():
    # pop up for Prediction
    root1 = tkinter.Tk()
    root1.title("Prediction of FSI Class")
    root1.geometry("390x500+0+0")
    tk.Label(root1,text="Security Apparatus",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=0,column=0)
    tk.Label(root1,text="Factionalized Elites",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=1,column=0)
    tk.Label(root1,text="Group Grievance",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=2,column=0)
    tk.Label(root1,text="Economy",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=3,column=0)
    tk.Label(root1,text="Economic Inequality",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=4,column=0)
    tk.Label(root1,text="Human Flight and Brain Drain",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=5,column=0)
    tk.Label(root1,text="State Legitimacy",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=6,column=0)
    tk.Label(root1,text="Services",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=7,column=0)
    tk.Label(root1,text="Human Rights",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=8,column=0)
    tk.Label(root1,text="Demographic Pressures",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=9,column=0)
    tk.Label(root1,text="Refugees and IDPs",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=10,column=0)
    tk.Label(root1,text="External Intervention",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=11,column=0)
    tk.Label(root1,text="FSI Value",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=13,column=0, padx=5, pady=5)   
    tk.Label(root1,text="Predicted FSI Class",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=14,column=0, padx=5, pady=5)
    # enter intialising
    e1 = tk.Entry(root1)
    e2 = tk.Entry(root1)
    e3 = tk.Entry(root1)
    e4 = tk.Entry(root1)
    e5 = tk.Entry(root1)
    e6 = tk.Entry(root1)
    e7 = tk.Entry(root1)
    e8 = tk.Entry(root1)
    e9 = tk.Entry(root1)
    e10 = tk.Entry(root1)
    e11 = tk.Entry(root1)
    e12 = tk.Entry(root1)
    # making grids
    e1.grid(row=0, column=1, padx=5, pady=5)
    e2.grid(row=1, column=1, padx=5, pady=5)
    e3.grid(row=2, column=1, padx=5, pady=5)
    e4.grid(row=3, column=1, padx=5, pady=5)
    e5.grid(row=4, column=1, padx=5, pady=5)
    e6.grid(row=5, column=1, padx=5, pady=5)
    e7.grid(row=6, column=1, padx=5, pady=5)
    e8.grid(row=7, column=1, padx=5, pady=5)
    e9.grid(row=8, column=1, padx=5, pady=5)
    e10.grid(row=9, column=1, padx=5, pady=5)
    e11.grid(row=10, column=1, padx=5, pady=5)
    e12.grid(row=11, column=1, padx=5, pady=5)
    # calculations and predictions
    def show():
        final=int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get())+int(e6.get())+int(e7.get())+int(e8.get())+int(e9.get())+int(e10.get())+int(e11.get())+int(e12.get())
        tk.Label(root1,text=str(final)).grid(row=13,column=1, padx=5, pady=5)
        final=[int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get()),int(e6.get()),int(e7.get()),int(e8.get()),int(e9.get()),int(e10.get()),int(e11.get()),int(e12.get())]
        val=int(pred_class(final))
        tk.Label(root1,text=str(val)).grid(row=14,column=1, padx=5, pady=5)  
    tk.Button(root1, text='Final FSI Score',command=show,font=("Helvetica", 13)).grid(row=15,column=1,sticky=tk.W,padx=5, pady=15)            
    

    

def country_fsi(country_name):
    # giving data of fsi to country selecetd 
    x_axis = list(data[data['Country']==country_name]['Year'])
    y_axis = list(data[data['Country']==country_name]['Total'])
    return x_axis,y_axis
 
def country_select():
    # pop up for selecting a country
    root = tkinter.Tk()
    root.geometry("800x500+0+0")
    root.title("Choose a Country")  
    # Add a grid
    mainframe = Frame(root)
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)   
    # Create a Tkinter variable
    tkvar = StringVar(root)   
    # Dictionary with options
    choices = set(data['Country'])
    tkvar.set('Choose One') # set the default option
    # guven specification
    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="You just need to select one Country from the dropdown",font=("Helvetica", 16)).grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)    
    # on change dropdown value
    def change_dropdown(*args):
        print( tkvar.get() )
        button = tkinter.Button(master=root, text=tkvar.get(), command=country_wise_graph(tkvar.get()))
        button.pack(side=tkinter.BOTTOM)
        _quit()
    # calling when value changes to anything
    tkvar.trace('w', change_dropdown)
    # definig function for quit  
    def _quit():
        root.quit()   
        root.destroy() 
    # quit button               
    button = tkinter.Button(master=root, text="Quit", command=_quit,font=("Helvetica", 16))
    button.pack(side=tkinter.BOTTOM)
    # root classifications
    root.mainloop()
    
    
def country_wise_graph(country_name):  
    # root strat
    root = tkinter.Tk()
    root.geometry("800x500+0+0")
    root.wm_title(country_name.upper())
    # figure specifications
    fig = Figure(figsize=(5, 4), dpi=100)   
    a,b=country_fsi(str(country_name))
    fig.add_subplot(111).plot(a,b)
    # A tk.DrawingArea.
    canvas = FigureCanvasTkAgg(fig, master=root)  
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)    
    # that foloow up bar 
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)    
    canvas.mpl_connect("key_press_event", on_key_press)
    # defining function for quiting  
    def _quit():
        root.quit()   
        root.destroy()    
    # button to quit                
    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)  
    # main loop finished
    tkinter.mainloop()

def popup_showinfo():
    showinfo("Hello")

def aboutw():
    # root strat
    root = tk.Tk()
    tk.Label(root,text="Security Apparatus",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=0,column=0, padx=5, pady=5)
    tk.Label(root,text="Factionalized Elites",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=1,column=0, padx=5, pady=5)
    tk.Label(root,text="Group Grievance",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=2,column=0, padx=5, pady=5)
    tk.Label(root,text="Economy",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=3,column=0, padx=5, pady=5)
    tk.Label(root,text="Economic Inequality",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=4,column=0, padx=5, pady=5)
    tk.Label(root,text="Human Flight and Brain Drain",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=5,column=0, padx=5, pady=5)
    tk.Label(root,text="State Legitimacy",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=6,column=0, padx=5, pady=5)
    tk.Label(root,text="Services",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=7,column=0, padx=5, pady=5)
    tk.Label(root,text="Human Rights",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=8,column=0, padx=5, pady=5)
    tk.Label(root,text="Demographic Pressures",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=9,column=0, padx=5, pady=5)
    tk.Label(root,text="Refugees and IDPs",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=10,column=0, padx=5, pady=5)
    tk.Label(root,text="External Intervention",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=11,column=0, padx=5, pady=5)
    tk.Label(root,text="FSI Value",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=13,column=0, padx=5, pady=5)   
    tk.Label(root,text="Predicted FSI Class",relief=tk.RIDGE,font=("Helvetica", 13)).grid(row=14,column=0, padx=5, pady=5)

    tk.Label(root,text="",relief=tk.RIDGE,font=("Helvetica", 11),bg="white").grid(row=0,column=1, padx=5, pady=5, columnspan=6)

    root.geometry("800x500+0+0")
    root.wm_title("About FSI Indicators")
    tkinter.mainloop()
    
def about():
    # root strat
    root = tk.Tk()
    tk.Label(root,text="Mounting demographic pressures and tribal, ethnic and/or religious conflicts",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=0,column=0, padx=5, pady=5)
    tk.Label(root,text="Massive internal and external displacement of refugees, creating severe humanitarian emergencies, like issues.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=1,column=0, padx=5, pady=5)
    tk.Label(root,text="Widespread vengeance-seeking group grievances.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=2,column=0, padx=5, pady=5)
    tk.Label(root,text="Chronic and sustained human flight.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=3,column=0, padx=5, pady=5)
    tk.Label(root,text="Delegitimization of the state.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=4,column=0, padx=5, pady=5)
    tk.Label(root,text="Deterioration of public services.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=5,column=0, padx=5, pady=5)
    tk.Label(root,text="Suspension or arbitrary application of law; widespread human rights abuses.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=6,column=0, padx=5, pady=5)
    tk.Label(root,text="Security forces operating as a state within a state often with impunity.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=7,column=0, padx=5, pady=5)
    tk.Label(root,text="Rise of factionalized elites.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=8,column=0, padx=5, pady=5)
    tk.Label(root,text="Intervention of external political agents and foreign states.",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=9,column=0, padx=5, pady=5)
    tk.Label(root,text="The list has been cited by journalists and academics in making broad comparative points",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=10,column=0, padx=5, pady=5)
    tk.Label(root,text="External Intervention",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=11,column=0, padx=5, pady=5)
    tk.Label(root,text="FSI Value",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=12,column=0, padx=5, pady=5)   
    tk.Label(root,text="Predicted FSI Class",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=14,column=0, padx=5, pady=5)

    root.geometry("800x500+0+0")
    root.wm_title("About FSI")
    tkinter.mainloop()
    
def scores():
    root = Tk()
    # labels
    tk.Label(root,text="Name of the Model Trained",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=0,column=0, padx=5, pady=5)
    tk.Label(root,text="------------------------------------------------------------------------------",font=("Helvetica", 12)).grid(row=1,column=0, padx=5, pady=5)
    tk.Label(root,text="MultinomialNB",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=2,column=0, padx=5, pady=5)
    tk.Label(root,text="BernoulliNB",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=3,column=0, padx=5, pady=5)
    tk.Label(root,text="KNeighborsClassifier",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=4,column=0, padx=5, pady=5)
    tk.Label(root,text="Rbf SVC",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=5,column=0, padx=5, pady=5)
    tk.Label(root,text="Poly SVC",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=6,column=0, padx=5, pady=5)
    tk.Label(root,text="Linear SVC",relief=tk.RIDGE,bg="white",font=("Helvetica", 12), fg="blue").grid(row=7,column=0, padx=5, pady=5)
    tk.Label(root,text="Random Forest",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=8,column=0, padx=5, pady=5)
    tk.Label(root,text="Decision Tree",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=9,column=0, padx=5, pady=5)
    tk.Label(root,text="Logistic regression",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=10,column=0, padx=5, pady=5)
    tk.Label(root,text="GaussianNB",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=11,column=0, padx=5, pady=5)
    tk.Label(root,text="-----------------------------------------------------------------------------",font=("Helvetica", 12)).grid(row=12,column=0, padx=5, pady=5)   
    tk.Label(root,text="Best Model",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=13,column=0, padx=5, pady=5)    
    # middles
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=0,column=1, padx=5, pady=5)    
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=1,column=1, padx=5, pady=5)    
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=2,column=1, padx=5, pady=5)
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=3,column=1, padx=5, pady=5)    
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=4,column=1, padx=5, pady=5)   
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=5,column=1, padx=5, pady=5)    
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=6,column=1, padx=5, pady=5)
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=7,column=1, padx=5, pady=5)    
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=8,column=1, padx=5, pady=5)   
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=9,column=1, padx=5, pady=5)    
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=10,column=1, padx=5, pady=5)
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=11,column=1, padx=5, pady=5)    
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=12,column=1, padx=5, pady=5)
    tk.Label(root,text="     |     ",font=("Helvetica", 12)).grid(row=13,column=1, padx=5, pady=5)    
    # scores
    tk.Label(root,text="Score of the Model Trained",relief=tk.RIDGE,bg="white",font=("Helvetica", 12)).grid(row=0,column=2, padx=5, pady=5)
    tk.Label(root,text="---------------------------------------------------------------",font=("Helvetica", 12)).grid(row=1,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.45 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=2,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.34 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=3,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.95 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=4,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.95 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=5,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.97 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=6,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.98 ",relief=tk.RIDGE,bg="white",font=("Helvetica", 12), fg="blue").grid(row=7,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.96 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=8,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.87 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=9,column=2, padx=5, pady=5)
    tk.Label(root,text=" 0.63 ",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=10,column=2, padx=5, pady=5)
    tk.Label(root,text="0.94",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=11,column=2, padx=5, pady=5)
    tk.Label(root,text="---------------------------------------------------------------",font=("Helvetica", 12)).grid(row=12,column=2, padx=5, pady=5)   
    tk.Label(root,text="Linear SVC",relief=tk.RIDGE,font=("Helvetica", 12)).grid(row=13,column=2, padx=5, pady=5)    
    # root
    root.geometry("800x500+0+0")
    root.wm_title("All Scores of All Models")
    root.mainloop()

def linksa():
    root = Tk()
    def callback(url):
        webbrowser.open_new(url)
    # labels
    lab1=Label(root, text="---------------The link Used for the Content as--------------", fg="black",font=("Helvetica", 13))
    lab1.grid(row=0,column=0, padx=5, pady=5)
    link1 = Label(root, text="--------------------------The links------------------------", fg="blue",font=("Helvetica", 13))
    link1.grid(row=0,column=1, padx=5, pady=5)   
    lab2=Label(root, text="FSI Official Website", fg="black",font=("Helvetica", 13))
    lab2.grid(row=1,column=0, padx=5, pady=5)
    link2 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link2.grid(row=1,column=1, padx=5, pady=5)
    link2.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/"))   
    lab3=Label(root, text="World data Official Data", fg="black",font=("Helvetica", 13))
    lab3.grid(row=2,column=0, padx=5, pady=5)
    link3 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link3.grid(row=2,column=1, padx=5, pady=5)
    link3.bind("<Button-1>", lambda e: callback("https://datacatalog.worldbank.org/"))   
    lab4=Label(root, text="Global Data", fg="black",font=("Helvetica", 13))
    lab4.grid(row=3,column=0, padx=5, pady=5)
    link4 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link4.grid(row=3,column=1, padx=5, pady=5)
    link4.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/data/"))   
    lab5=Label(root, text="All Datasets", fg="black",font=("Helvetica", 13))
    lab5.grid(row=4,column=0, padx=5, pady=5)
    link5 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link5.grid(row=4,column=1, padx=5, pady=5)
    link5.bind("<Button-1>", lambda e: callback("https://datacatalog.worldbank.org/search/type/dataset"))    
    lab6=Label(root, text="Country Dashboard", fg="black",font=("Helvetica", 13))
    lab6.grid(row=5,column=0, padx=5, pady=5)
    link6 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link6.grid(row=5,column=1, padx=5, pady=5)
    link6.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/country-data/"))    
    lab7=Label(root, text="Comparartive Analysis", fg="black",font=("Helvetica", 13))
    lab7.grid(row=6,column=0, padx=5, pady=5)
    link7 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link7.grid(row=6,column=1, padx=5, pady=5)
    link7.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/comparative-analysis/"))
    lab8=Label(root, text="Download Data", fg="black",font=("Helvetica", 13))
    lab8.grid(row=7,column=0, padx=5, pady=5)
    link8 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link8.grid(row=7,column=1, padx=5, pady=5)
    link8.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/excel/"))    
    lab9=Label(root, text="Recent Analysis", fg="black",font=("Helvetica", 13))
    lab9.grid(row=8,column=0, padx=5, pady=5)
    link9 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link9.grid(row=8,column=1, padx=5, pady=5)
    link9.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/category/analysis/fragile-states-index-2019/"))    
    lab10=Label(root, text="All FSI Indicators", fg="black",font=("Helvetica", 13))
    lab10.grid(row=9,column=0, padx=5, pady=5)
    link10 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link10.grid(row=9,column=1, padx=5, pady=5)
    link10.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/indicators/"))    
    lab11=Label(root, text="Methodology", fg="black",font=("Helvetica", 13))
    lab11.grid(row=10,column=0, padx=5, pady=5)
    link11 = Label(root, text="Links", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link11.grid(row=10,column=1, padx=5, pady=5)
    link11.bind("<Button-1>", lambda e: callback("https://fragilestatesindex.org/methodology/"))   
    lab12=Label(root, text="The Fund for Peace", fg="black",font=("Helvetica", 13))
    lab12.grid(row=11,column=0, padx=5, pady=5)
    link12 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link12.grid(row=11,column=1, padx=5, pady=5)
    link12.bind("<Button-1>", lambda e: callback("https://fundforpeace.org/"))    
    lab13=Label(root, text="Contact FSI", fg="black",font=("Helvetica", 13))
    lab13.grid(row=12,column=0, padx=5, pady=5)
    link13 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link13.grid(row=12,column=1, padx=5, pady=5)
    link13.bind("<Button-1>", lambda e: callback("https://fundforpeace.org/get-involved/contact-us/"))    
    lab14=Label(root, text="Donate to Fund For Peace", fg="black",font=("Helvetica", 13))
    lab14.grid(row=13,column=0, padx=5, pady=5)
    link14 = Label(root, text="Link", fg="blue", cursor="hand2",font=("Helvetica", 13))
    link14.grid(row=13,column=1, padx=5, pady=5)
    link14.bind("<Button-1>", lambda e: callback("https://fundforpeace.org/get-involved/donate/"))
    # root     
    root.geometry("800x500+0+0")
    root.mainloop()  
    
def show_img():
    load = Image.open("one.png")
    render = ImageTk.PhotoImage(load)
    # labels can be text or images
    img = Label( image=render)
    img.image = render
    img.place(x=70, y=100)

class Application(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        root.title("Fragile State Index")
        self.master = master
        self.pack()        
        show_img()
        
        button_showinfo1 = ttk.Button(self, text="Country Wise FSI", command=country_select)
        button_showinfo1.pack(padx=15, pady=10, side=tk.LEFT)

        button_showinfo2 = ttk.Button(self, text="Predict Value Of", command=pred_value)
        button_showinfo2.pack(padx=15, pady=10, side=tk.LEFT)  

        button_showinfo2 = ttk.Button(self, text="About Data", command=about)
        button_showinfo2.pack(padx=15, pady=10, side=tk.LEFT) 
                
        button_showinfo2 = ttk.Button(self, text="About Indicators", command=aboutw )
        button_showinfo2.pack(padx=15, pady=10, side=tk.LEFT) 
        
        button_showinfo2 = ttk.Button(self, text="About FSI", command=linksa )
        button_showinfo2.pack(padx=15, pady=10, side=tk.LEFT) 
               
        button_showinfo = ttk.Button(self, text="Scores", command=scores)
        button_showinfo.pack(padx=15, pady=40, side=tk.LEFT)

root = tk.Tk()
app = Application(root)
root.geometry("800x500+0+0")

root.mainloop()