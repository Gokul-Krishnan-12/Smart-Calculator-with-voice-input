from tkinter import *
import speech_recognition as sr

#Function to input voice as text
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            x=('{}'.format(text))
            entry.delete(0, END)
            entry.insert(END, x)

        except:
            print('Sorry I didnt hear you')

# Defining Operations
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1
#convert Fahrenheit to Celsius
def cel(b):
    C=(b-32)*5/9
    return C+'C'
#convert Celsius to Fahrenheit
def far(c):
    F=(c+32)*9/5
    return F +"F"

def Filter_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text1 = text.get()
    for word in text1.split(' '):


        if word.upper() in operations.keys():
            try:
                l =Filter_text(text1)
                r = operations[word.upper()](l[0] , l[1])
                result.delete(0,END)
                result.insert(END,r)
            except:
                result.delete(0,END)
                result.insert(END,'something went wrong ')
            finally:
                break
        elif word.upper() not in operations.keys():
            result.delete(0,END)
            result.insert(END,'something went wrong')

operations={'ADD':add,'PLUS':add,'SUM':add,
            'SUBTRACT':sub,'DIFFERENCE':sub,'MINUS':sub,
            'MULTIPLY':mul,'PRODUCT':mul,
            'DIVIDE':div,
            'FAHRENHEIT':cel,
            'CELSIUS':far ,'LCM':lcm , 'HCF':hcf ,
            'MOD': mod,
            'REMANDER': mod, 'MODULUS': mod}

cal = Tk()

# Adjust size
cal.geometry('570x340')
# Naming title
cal.title('Smart Calculator')

# Add Image File
background = PhotoImage(file='Image.png')
canvass =Canvas(cal,width= 500,height=500,bg='grey')
canvass.pack(fill="both", expand=True)


# Display image
canvass.create_image(0, 0, image=background,anchor="nw")

# Add Text
heading = Label(cal,text='Smart Calculator',font = "Helvetica 20 underline", width=40 ,padx=1,pady=1)
heading.place(x=60,y=10,width=450)

#text_box

text=StringVar()
entry =Entry(cal,width=32,textvariable=text,bg='lightgrey',font= 10)
entry.place(x=55,y=150,height=40)

#speak button
search = Button(cal,text='Speak',command=speak)
search.place(x=420,y=150,height=40)


#search button
search = Button(cal,text='Search',command=calculate)
search.place(x=465,y=150,height=40)

#Result

result = Listbox(cal,width=31,bg='lightgrey',font= ' 10')
result.place(x=60,y=250,height=40)

cal.mainloop()