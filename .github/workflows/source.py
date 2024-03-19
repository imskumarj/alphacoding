from tkinter import *
root = Tk()
root.title("Fibonacci Generator")
root.state("zoomed")
root.config(bg="skyblue")


def fib():
    elements = []
    if EntryType.get() == 1:
        elements.append(0)
        return elements
    if EntryType.get() == 2:
        elements.extend([0,1])
        return elements
    if EntryType.get() >2:
        elements.extend([0,1])
        for i in range(2,EntryType.get()):
            elements.append(elements[i-2]+elements[i-1])
        return elements


def start():
    text.destroy()
    EntryBox.destroy()
    Submit.destroy()
    Label(text="Obtained Fibonacci series is:",font=("Poppins", 30, "bold"),bg="skyblue").place(x=250,y=150)
    if EntryType.get() == 0:
        Label(root, text = "EMPTY!", font=("Poppins", 30, "bold"),bg="skyblue").place(x=700,y=350)
    if EntryType.get() == 1:
        elements = fib()
        Label(root, text = elements, font=("Poppins", 30, "bold"),bg="skyblue").place(x=700,y=350)
    if EntryType.get() > 1:
        elements = fib()
        print(elements)
        result = ''
        for i in range(0,len(elements)):
            if i%6==0 and i!=0:
                result += str(elements[i]) + "\n"
            else:
                result += str(elements[i])+'  '
        Label(root, text = result, font=("Poppins", 30, "bold"),bg="skyblue").place(x=600,y=350)


text = Label(root, text="Enter the number of elements required in Fibonacci series", font=("Poppins", 30, "bold"),bg="skyblue")
text.place(x=250,y=150)
EntryType = IntVar()
EntryBox = Entry(root, textvariable=EntryType)
EntryBox.place(x=700,y=350)
Submit = Button(text="Enter", command=start)
Submit.place(x=742,y=380)
root.mainloop()
