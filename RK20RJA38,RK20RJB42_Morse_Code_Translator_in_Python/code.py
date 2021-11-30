''' Dictionary '''

# strings containing alphabets and numbers
s_alpha = 'a.01 b.1000 c.1010 d.100 e.0 f.0010 g.110 h.0000 i.00 j.0111 k.101 l.0100 m.11 n.10 o.111 p.0110 q.1101 r.010 s.000 t.1 u.001 v.0001 w.011 x.1001 y.1011 z.1100 '
s_num = '1.01111 2.00111 3.00011 4.00001 5.00000 6.10000 7.11000 8.11100 9.11110 0.11111 '

# concatination of two strings
s_alphanum = s_alpha + s_num

# conversion of string to list
l_alphanum = s_alphanum.split()

# conversion of list to dictionary
d_eng_morse = {}
for i in range(len(l_alphanum)):
    d_eng_morse[l_alphanum[i].split('.')[0]] = l_alphanum[i].split('.')[1]

# swapping keys and values of dictionary
d_morse_eng = {}
for i in d_eng_morse:
    d_morse_eng[d_eng_morse[i]] = i



''' English to Morse and Morse to Englich translator function '''

# Input format: (string to be converted), (short sign symbol), (long sign symbol), (spacing scheme), (eng to morse or vice-versa)
# Output: translated string
def translator(string, l, u, compact, em):

    # spacing in compact form
    if compact:
        part_same_letter='' # 0
        btw_letter=' '      # 1 
        btw_word='   '      # 3
    
    # spacing in International morse code form
    else:
        part_same_letter=' ' # 1
        btw_letter='   '     # 3
        btw_word='       '   # 7
 
    #string to be returned
    output=''
    
    #english to morse
    if em==1:

        # redifining spacing formats for english to morse
        if compact:
            part_same_letter='' # 0
            btw_letter=' '      # 1-0 (space between letters - space between parts of same letter)
            btw_word='  '       # 3-1 (space between words - space between letters)
        else:
            part_same_letter=' ' # 1
            btw_letter='  '      # 3-1
            btw_word='    '      # 7-3

        # converting uppercase letters to lowercase
        stringl = string.lower()
                
        #reading english letters one by one
        for i in stringl:

            # converting spacing in english to spacing in morse
            if i.isspace():
                output=output+btw_word
                continue

            # converting alphabets and numbers to morse symbols
            elif i.islower() or i.isdigit():

                # converting short and long sign according to user customized symbols
                for j in d_eng_morse[i]:
                    if j=='1':
                        output=output+u+part_same_letter
                    else:
                        output=output+l+part_same_letter

            # assigning 'X' to unrecognized symbols
            else:
                output=output+'X'+part_same_letter

            # after conversion of one English letters, adding space between letter
            output=output+btw_letter

        output=output[0:-len(btw_letter)-len(part_same_letter)]
            
    # morse to english
    else:
    
        # creating list containing code for english words
        l_word = string.split(btw_word)
        print(l_word)

        # traversing each word
        for i in l_word:

            # creating list containing code for english letters
            l_letter = i.split(btw_letter)
            print(l_letter)
            
            # traversing each letter
            for j in l_letter:

                # creating temporary storage for an English letter
                temp=''

                # traversign parts of same letter
                for k in j:

                    # converting user selected symbols to 0's and 1's
                    if k==u:
                        temp=temp+'1'
                    elif k==l:
                        temp=temp+'0'
                        
                # concatinating letters and 'X' if unrecognized
                output=output+d_morse_eng.get(temp, 'X')

            # concatinating spaces after each word
            output=output+' '

        output=output[0:-1]
            
        
    return output


''' Filter to check whether the string is direct, or contained in a file '''

def filter(string, l, u, compact, em, file):

    # accessing text if present in file
    if file:

        # exception handling
        # defining Python user-defined exceptions
        class error(Exception):
            pass

        class empty(error):
            pass
       
        try:
            f=open(string, 'r')
            if f.read()=='':
                raise empty

        # if file is empty
        except empty:
            output='(empty file)'

        # if file not found
        except IOError:
            output='(Cant find the file)'

        # if no exceptions found
        else:
            f=open(string, 'r')
            output=translator(f.read(), l, u, compact, em)

    # calling translator function as it is 
    else:
        output=translator(string, l, u, compact, em)

    return output
        

'''--------------------------------------------------------------------------------------------------------------'''

from tkinter import *
import tkinter.messagebox as tmsg

def deletetext():
    textbox.delete("1.0", "end")



def submit():
    deletetext()
    string1=StringVar()
    string1=input.get()
    print(string1)
    global answer
    answer=filter(input.get(), shortsign.get(), longsign.get(), var2.get(), var1.get(), var3.get())
    print(answer)
    textbox.insert('end',answer)
    
   
 
   

def save():
    tmsg.showinfo("Successfully Saved","The file is successfully saved!")
def instruction():
    tmsg.showinfo("Instructions","1) Select the converstion type\n2) Enter the symbols\n3) Select display format\n4) Enter text\n5) Click on submit")
def credit():
    tmsg.showinfo("Credits","1) Backend: Sudip Kumar Madal\n2) Frontend: Rohan Saraswat")    


root = Tk() 

root.geometry("1000x650")
root.minsize(900,600)
root.wm_iconbitmap("1.ico")

mainmenu=Menu(root)
menu1=Menu(mainmenu,tearoff=0)
menu1.add_command(label="New")
menu1.add_command(label="Open")
menu1.add_separator()
menu1.add_command(label="Save", command=save)
menu1.add_command(label="Save As")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=menu1)
menu2=Menu(mainmenu,tearoff=0)
menu2.add_command(label="Instructions", command=instruction)
menu2.add_command(label="Credits",command=credit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=menu2)
menu3=Menu(mainmenu,tearoff=0)
menu3.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Quit", menu=menu3)


root.title("Morse code Translator")

frame=Frame(root,bg="#FFBF86")
Label(frame, text="Welcome to Morse Code Encoder-Decoder",font= "comicsansms 25 bold",borderwidth=5,bg="#88E0EF", relief=SUNKEN,padx=10,pady=5).grid(row=0,column=0,columnspan=4)

var1=IntVar()
var1.set(1)
radio1=Radiobutton(frame, text="English to Morse Code",font= "comicsansms 20 bold",variable=var1,value="1",border=3, relief="solid").grid(row=1, column=0,columnspan=2,padx=15,pady=15)
radio1=Radiobutton(frame, text="Morse Code to English",font= "comicsansms 20 bold",variable=var1,value="0",border=3, relief="solid").grid(row=1, column=2,padx=15,pady=15)

Label(frame, text="Enter Symbol for: ",font= "comicsansms 25 underline",bg="#CEE5D0").grid(row=2,column=0,columnspan=2,sticky=W,pady=10,padx=15)
Label(frame, text="Choose Display format: ",font= "comicsansms 25 underline",bg="#CEE5D0").grid(row=2,column=2,sticky=W,pady=10,padx=15)
Label(frame, text="Choose String Type: ",font= "comicsansms 25 underline",bg="#CEE5D0").grid(row=2,column=3,sticky=W,pady=10,padx=15)

Label(frame, text="Short Sign: ",font= "comicsansms 20 ",bg="#FFBF86").grid(row=3,column=0,sticky=W)
Label(frame, text="Long Sign: ",font= "comicsansms 20 ",bg="#FFBF86").grid(row=4,column=0,sticky=W)

shortsign=StringVar()
longsign=StringVar()
shortsign.set('.')
longsign.set('-')
Entry(frame, width=5,textvariable=shortsign,font= "comicsansms 15 ",bg="#F3F0D7").grid(row=3,column=1,sticky=W)
Entry(frame, width=5,textvariable=longsign,font= "comicsansms 15 ",bg="#F3F0D7").grid(row=4,column=1,sticky=W)

var2=IntVar()
var2.set(0)
radio1=Radiobutton(frame, text="International Format",font= "comicsansms 20",bg="#FFBF86",variable=var2,value="0").grid(row=3, column=2,sticky=W)
radio1=Radiobutton(frame, text="Compact Format",font= "comicsansms 20",bg="#FFBF86",variable=var2,value="1").grid(row=4, column=2,sticky=W)

var3=IntVar()
var3.set(0)
radio1=Radiobutton(frame, text="Enter string",font= "comicsansms 20",bg="#FFBF86",variable=var3,value="0").grid(row=3, column=3,sticky=W)
radio1=Radiobutton(frame, text="Select file",font= "comicsansms 20",bg="#FFBF86",variable=var3,value="1").grid(row=4, column=3,sticky=W)

Label(frame, text="Enter Text: ",font= "comicsansms 20 ",bg="#FFBF86").grid(row=5,column=0,sticky=W)

input=StringVar()
input.set('sample text')
Entry(frame, width=35,textvariable=input,font= "comicsansms 25 ",bg="#F3F0D7").grid(row=5,column=1,columnspan=3,sticky="w",pady=10)

Button(frame, text="Submit",font= "comicsansms 20 bold",bg="#EC0101",command=submit, ).grid(row=6,column=2,pady=10)

Label(frame, text="Output: ",font= "comicsansms 20 bold underline " ,bg="#FFBF86").grid(row=7,column=0,sticky=W)



# output=StringVar()
# output=answer
textbox=Text(frame, width=50,height=4,font="consolas 18 bold")
textbox.grid(row=8,column=0,columnspan=4)
# textbox.insert('end',output)
# textbox.config(state="disabled")

root.configure(bg="#FFBF86")

frame.pack()
root.mainloop()
