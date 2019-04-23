from tkinter import*
import webbrowser
def show():
    name=star.get()
    name1=star1.get()
    if name =="holland"and name1=="USA":
        print("country")
        webbrowser.open("http://www.yahoo.com")
    else:
           print("not a country")
      
k=Tk()
k.title("ebe")
k.geometry("900x900")
k.configure(background='light pink')
Label(k,text="ebe",font=200,fg="black",bg="yellow").grid(row=1,column=2)
Label(k,text="hello",font=650,fg="blue",bg="red").grid(row=2,column=2)
Label(k,text="me",font=150,fg="yellow",bg="black").grid(row=2,column=1)
star=Entry(k,width=95,bg="purple")
star.grid(row=4,column=2)
star1=Entry(k,width=95,bg="purple")
star1.grid(row=5,column=2)
e=Button(k,width=10,text="submit",bg="black",fg="white",font=20,command=show)   
e.grid(row=6,column=2)         
