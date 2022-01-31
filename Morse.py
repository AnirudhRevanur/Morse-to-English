import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import*
import pyttsx3

LARGE_FONT= ("Verdana", 12)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,daytheme, nighttheme):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(pady=10,padx=10)

        button = tk.Button(self, text="day theme",
                            command=lambda: controller.show_frame(daytheme))
        button.grid()

        button2 = tk.Button(self, text="night theme",
                            command=lambda: controller.show_frame(nighttheme))
        button2.grid()


class daytheme(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        variable1 = StringVar(self)
        variable2 = StringVar(self)
   

        variable1.set("lang-code")
        variable2.set("lang-code")
   


        ENGLISH_TO_MORSE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':'/'}
        MORSE_TO_ENGLISH = {}
        for key, value in ENGLISH_TO_MORSE.items():
            MORSE_TO_ENGLISH[value] = key


        def clearAll() :
            language1_field.delete(1.0, END)
            language2_field.delete(1.0, END)
    
        engine=pyttsx3.init()

        def speaknow():
           engine.say(self.textv.get())
           engine.runAndWait()
           engine.stop()


        def convert() :
 
    
            message = language1_field.get("1.0", "end")[:-1]
 
    
            if variable1.get() == variable2.get():
                messagebox.showerror("Can't Be same Language")
                return
 
            elif variable1.get() == "Eng" and variable2.get() == "Morse" :
        
        
               rslt = encrypt(message)
 
            elif variable1.get() == "Morse" and variable2.get() == "Eng" :
 
       
                rslt = decrypt(message)
 
            else :
         
       
                messagebox.showerror("please choose valid language code..")
                return
     
   
            language2_field.insert('end -1 chars', rslt)
     
         

        def encrypt(message):
            morse = []  
            for char in message:
              if char in ENGLISH_TO_MORSE:
                 morse.append(ENGLISH_TO_MORSE[char])
            return " ".join(morse)
    

        def decrypt(message):
            message = message.split(" ")
            english = []  
            for code in message:
               if code in MORSE_TO_ENGLISH:
                   english.append(MORSE_TO_ENGLISH[code])
            return " ".join(english)

        if __name__ == "__main__" :
            self.configure(background = 'goldenrod1') 
     
     
            headlabel = Label(self, text = 'Morse Code Translator', fg = 'black', bg = "red")
            Font_tuple = ("tekstil", 15, "bold")
            headlabel.configure(font = Font_tuple)
   
    
            label1 = Label(self, text = "chosen Language ",
                        fg = 'black', bg = 'coral1')
            Font_tuple = ("Kartika", 10, "bold")
            label1.configure(font = Font_tuple)
       
     
            label2 = Label(self, text = "From Language", 
                         fg = 'black', bg = 'deeppink2')
            Font_tuple = ("Comic Sans MS", 10, "bold")
            label2.configure(font = Font_tuple)
     
   
            label3 = Label(self, text = "To Language ", 
                             fg = 'black', bg = 'deeppink2')
            Font_tuple = ("Comic Sans MS", 10, "bold")
            label3.configure(font = Font_tuple)
     
   
    
            label4 = Label(self, text = "Converted Language ", 
                                  fg = 'black', bg = 'coral1')
            Font_tuple = ("Kartika", 10, "bold")
            label4.configure(font = Font_tuple)
    
   
     
            headlabel.grid(row = 0, column = 2) 
            label1.grid(row = 2, column = 0) 
            label2.grid(row = 2, column = 1)
            label3.grid(row = 2, column = 3)
            label4.grid(row = 2, column = 4)
        
            self.textv=tk.StringVar()

            language1_field = Text(self, height = 8, width = 25,
                               font = "lucida 13")

        
            language2_field = Text(self, height = 8, width = 25,
                               font = "lucida 13")
            voice= Entry(self,textvariable=self.textv, font=30, width=25,bd=5)
        
            language1_field.grid(row = 1, column = 0, padx = 10) 
            language2_field.grid(row = 1, column = 4, padx = 10)
            voice.grid(row = 1, column = 2, padx = 10)      
   
    
            languageCode_list = ["Eng", "Morse"]
   
    
            FromLanguage_option = OptionMenu(self,variable1, *languageCode_list)
            ToLanguage_option = OptionMenu(self,variable2, *languageCode_list)
       
            FromLanguage_option.grid(row =1, column = 1, ipadx = 10)
            ToLanguage_option.grid(row = 1, column = 3, ipadx = 10)
       
     
            button1 = tk.Button(self, text = "Convert", bg = "red", fg = "black",
                                command = convert)
       
            button1.grid(row = 3, column = 2)
   
            button2 = tk.Button(self, text = "Clear", bg = "red", 
                     fg = "black", command = clearAll)
     
            button2.grid(row = 4, column = 2)

            button3 = tk.Button(self, text = "voice", bg = "red", fg = "black",
                                command = speaknow)
            button3.grid(row = 5, column=2)

            button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
            button4.grid(row=6,column=2)

            button5 = tk.Button(self, text="night theme",
                            command=lambda: controller.show_frame(nighttheme))
            button5.grid(row=7,column=2)


class nighttheme(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from tkinter import messagebox
        
 
 
        variable1 = StringVar(self)
        variable2 = StringVar(self)
   

        variable1.set("lang-code")
        variable2.set("lang-code")
   


        ENGLISH_TO_MORSE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':'/'}
        MORSE_TO_ENGLISH = {}
        for key, value in ENGLISH_TO_MORSE.items():
            MORSE_TO_ENGLISH[value] = key


        def clearAll() :
            language1_field.delete(1.0, END)
            language2_field.delete(1.0, END)
    
        engine=pyttsx3.init()

        def speaknow():
           engine.say(textv.get())
           engine.runAndWait()
           engine.stop()


        def convert() :
 
    
            message = language1_field.get("1.0", "end")[:-1]
 
    
            if variable1.get() == variable2.get() :
                messagebox.showerror("Can't Be same Language")
                return
 
            elif variable1.get() == "Eng" and variable2.get() == "Morse" :
        
        
               rslt = encrypt(message)
 
            elif variable1.get() == "Morse" and variable2.get() == "Eng" :
 
       
                rslt = decrypt(message)
 
            else :
         
       
                messagebox.showerror("please choose valid language code..")
                return
     
   
            language2_field.insert('end -1 chars', rslt)
     
         

        def encrypt(message):
            morse = []  
            for char in message:
              if char in ENGLISH_TO_MORSE:
                 morse.append(ENGLISH_TO_MORSE[char])
            return " ".join(morse)
    

        def decrypt(message):
            message = message.split(" ")
            english = []  
            for code in message:
               if code in MORSE_TO_ENGLISH:
                   english.append(MORSE_TO_ENGLISH[code])
            return " ".join(english)

        if __name__ == "__main__" :
            self.configure(background = 'black') 
     
     
            headlabel = Label(self, text = 'Morse Code Translator', fg = 'black', bg = "red")
            Font_tuple = ("tekstil", 15, "bold")
            headlabel.configure(font = Font_tuple)
   
    
            label1 = Label(self, text = "chosen Language ",
                        fg = 'black', bg = 'coral1')
            Font_tuple = ("Kartika", 10, "bold")
            label1.configure(font = Font_tuple)
       
     
            label2 = Label(self, text = "From Language", 
                         fg = 'black', bg = 'deeppink2')
            Font_tuple = ("Comic Sans MS", 10, "bold")
            label2.configure(font = Font_tuple)
     
   
            label3 = Label(self, text = "To Language ", 
                             fg = 'black', bg = 'deeppink2')
            Font_tuple = ("Comic Sans MS", 10, "bold")
            label3.configure(font = Font_tuple)
     
   
    
            label4 = Label(self, text = "Converted Language ", 
                                  fg = 'black', bg = 'coral1')
            Font_tuple = ("Kartika", 10, "bold")
            label4.configure(font = Font_tuple)
    
   
     
            headlabel.grid(row = 0, column = 2) 
            label1.grid(row = 2, column = 0) 
            label2.grid(row = 2, column = 1)
            label3.grid(row = 2, column = 3)
            label4.grid(row = 2, column = 4)
        
            textv=StringVar()

            language1_field = Text(self, height = 8, width = 25,
                               font = "lucida 13")
        
            language2_field = Text(self, height = 8, width = 25,
                               font = "lucida 13")
            voice= Entry(self,textvariable=textv, font=30, width=25,bd=5)
        
            language1_field.grid(row = 1, column = 0, padx = 10) 
            language2_field.grid(row = 1, column = 4, padx = 10)
            voice.grid(row = 1, column = 2, padx = 10)      
   
    
            languageCode_list = ["Eng", "Morse"]
   
    
            FromLanguage_option = OptionMenu(self, variable1, *languageCode_list)
            ToLanguage_option = OptionMenu(self, variable2, *languageCode_list)
       
            FromLanguage_option.grid(row =1, column = 1, ipadx = 10)
            ToLanguage_option.grid(row = 1, column = 3, ipadx = 10)
       
     
            button1 = tk.Button(self, text = "Convert", bg = "red", fg = "black",
                                command = convert)
       
            button1.grid(row = 3, column = 2)
   
            button2 = tk.Button(self, text = "Clear", bg = "red", 
                     fg = "black", command = clearAll)
     
            button2.grid(row = 4, column = 2)

            button3 = tk.Button(self, text = "voice", bg = "red", fg = "black",
                                command = speaknow)
            button3.grid(row = 5, column=2)

            button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
            button4.grid(row=6,column=2)
            button5 = tk.Button(self, text="day theme",
                            command=lambda: controller.show_frame(daytheme))
            button5.grid(row=7,column=2)



app = SeaofBTCapp()
app.mainloop()