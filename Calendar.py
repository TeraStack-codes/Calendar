from tkinter import Frame,Button,Label,Tk,StringVar,N,LEFT,RIGHT,TOP,BOTH,Toplevel,Entry,PhotoImage
import datetime as datetime
from datetime import *
from tkcalendar import Calendar
import pickle

window = Tk()
window.title('Calender')
window.minsize('400','400')
window.maxsize('1000','400')
window.geometry('800x400+300+200')
window.iconbitmap(r'Images\calendar_logo.ico')
window.config(bg = 'Orange')

bgimg = PhotoImage(file = 'Images\space.png')


calframe = Frame(window,bg = 'Blue')
calframe.pack(expand = True,fill = BOTH)


Tirth = 'No Events'

mode = 'day'
Harry_Potter = StringVar()
Tom_Riddle = StringVar()

Eventdict={}

#Funcs

def mode_change():
    global mode
    if mode == 'day':
        mode = 'none'
        btn_SelectMode.config(bg = '#fffd9c')
        cal.config(selectmode = 'none')
    else:
        btn_SelectMode.config(bg = 'Yellow')
        mode = 'day'
        cal.config(selectmode = 'day')
'''
def event_entered():
    global Harry_Potter,Tom_Riddle,Eventdict
    Netflix = cal.get_date().replace('/','-')
    Snitch = Netflix.split('-')
    Hocrux = Snitch[2] +'-'+Snitch[1]+ '-' + Snitch[0]
    date=datetime.strptime(Hocrux,"%Y-%m-%d").date()
    cal.calevent_create(date, Harry_Potter, 'meeting')
    cal.tag_config('meeting', background='Orange', foreground = 'Black')
    Eventdict[Hocrux]=[Harry_Potter.get()],['meeting']
    print(Eventdict)

    
def event_make():
    global Harry_Potter,Tom_Riddle
    root = Toplevel()
    root.geometry('200x110')
    root.iconbitmap(r'Images\calendar_logo.ico')
    rootFrame1 = Frame(root,bg = 'Orange')
    rootFrame1.pack(fill = BOTH)
    rootLabel1 = Label(rootFrame1,text = 'Title',bg = 'Orange')
    rootLabel1.pack(fill = BOTH)
    rootEntry1 = Entry(rootFrame1,textvariable = Harry_Potter,bg = 'Yellow')
    rootEntry1.pack(fill = BOTH)
    rootButton1 = Button(rootFrame1,text = 'Enter',command = event_entered ,bg = 'Orange',)
    rootButton1.pack(fill = BOTH)
    


def see_make():
    global Eventdict
    global Tirth
    think = Toplevel()
    think.iconbitmap(r'Images\calendar_logo.ico')
    Netflix = cal.get_date().replace('/','-')
    Snitch = Netflix.split('-')
    Hocrux = Snitch[2] +'-'+Snitch[1]+ '-' + Snitch[0]
    Tirth = Eventdict[Hocrux][0]
    btn = Button(think,text = Tirth,font = ('Bubble Rainbow', 20))
    btn.pack()
'''

#Month

a = date.today()
monthdict = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
month = StringVar()
year = StringVar()
day = StringVar()
month.set(monthdict[a.month])
year.set(a.year)
day.set(a.day)

#TopFrame

TopFrame = Frame(
    calframe,
    bg = 'Orange'
)
TopFrame.pack(anchor = N,expand = True,fill = 'x')

#Widgets In Top Frame

Title_Label = Label(
    TopFrame,
    text = 'Calender',
    font = ('Cartoon Empire', '40'),
    bg = 'Orange'
)
Title_Label.pack()


#Second top Frame
SecondTopFrame = Frame(TopFrame,bg = 'Yellow')
SecondTopFrame.pack(anchor = N,expand = True,fill = 'x')

txtLabel = Label(SecondTopFrame,)

Daylabel = Label(
    SecondTopFrame,
    textvariable = day,
    bg = 'Yellow',
    font =('Bubble Rainbow', 15)
)
Daylabel.pack(padx = 5,side = LEFT)

Monthlabel = Label(
    SecondTopFrame,
    textvariable = month,
    bg = 'Yellow',
    font =('Bubble Rainbow', 15)
)
Monthlabel.pack(padx = 15,side = LEFT)
Year_label = Label(
    SecondTopFrame,
    textvariable = year,
    bg = 'Yellow',
    font =('Bubble Rainbow', 15)
)
Year_label.pack(side = LEFT)

btn_SelectMode = Button(SecondTopFrame,text = 'Select',bg = 'Yellow',font=('Bubble Rainbow',15),border = 0,command = mode_change)
btn_SelectMode.pack(padx = 20,side = RIGHT)

'''
btn_Make_Event = Button(SecondTopFrame,text = 'Make Event',bg = 'Yellow',font=('Bubble Rainbow',15),border = 0,command = event_make)
btn_Make_Event.pack(padx = 20,side = RIGHT)

btn_See_Event = Button(SecondTopFrame,text = 'See Event',bg = 'Yellow',font=('Bubble Rainbow',15),border = 0,command = see_make)
btn_See_Event.pack(padx = 20,side = RIGHT)
'''


cal = Calendar(calframe,selectmode = 'day',year = a.year,month = a.month ,day = a.day)
cal.pack(expand = True,fill = BOTH)



window.mainloop()