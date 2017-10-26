"""
A program to find all of the anagrams in a dictionary
in which there are at least 4 letters in the word
and at least as many anagrams as there are letters.
word must be greater than 4 letters (not characters?)

author: altipple@gmail.com 20171026
"""

from tkinter import *

class Anagrams(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # input file label
        self.filelab = Label(self)
        self.filelab.grid(column=0,row=0,columnspan=1,sticky='W')
        self.filelab["text"] = "Input file"

        # input file space
        self.fileentry = Entry(self,width=55)
        self.fileentry.grid(column=1,row=0,columnspan=1,sticky='EW')

        # browse to input file
        self.browsebutton = Button(self)
        self.browsebutton["text"] = "Browse"
        self.browsebutton["command"] = self.browsecsv
        self.browsebutton.grid(column=2,row=0,columnspan=1,sticky='EW')

        # update space for filename with file name typed in or browsed to
        self.filecontents = StringVar()
        self.fileentry["textvariable"] = self.filecontents
        self.fileentry.update_idletasks() 
 
        # run button
        self.runit = Button(self)
        self.runit["text"] = "Run"
        self.runit["command"] = self.write_anagrams
        self.runit.grid(column=1,row=2,columnspan=1,sticky='EW')
        
        # quit program
        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(column=0,row=2, columnspan=1,sticky='EW')

    def browsecsv(self):
        # browse to file
        self.filenm = filedialog.askopenfilename()
        self.filecontents.set(self.filenm)
        return self.filenm   
    
    def write_anagrams(self):
        # run program
        infile = self.filecontents.get()
        outfile = infile.split(".")[0] + "_output.txt"
        self.group_words(self.index_words(infile),outfile)
        return messagebox.showinfo("Result" , "Anagrams program complete\nSee input file location\nfor results file '_output.txt'")
        
    def index_words(self,filepath):
        # return dict of words longer than 4 letters
        # and sorted word as index
        words_dict = {}
        with open(filepath, 'r') as fp_in:
            for word in fp_in:
                w = list(word.strip())
                if "'" in w:
                    ww = w.pop(w.index("'"))
                    if len(ww) > 3:
                        words_dict.update({word.strip():"".join(sorted(ww))})
                else:
                    ww = w
                    if len(ww) > 3:
                        words_dict.update({word.strip():"".join(sorted(ww))})
        return words_dict

    def group_words(self,new_words_dict,outfile):
        # group anagrams by like index
        groups = {}
        with open(outfile,'w') as fp_out:
            for k,v in new_words_dict.items():
                if v not in groups:
                    groups[v] = [k]
                else:
                    groups[v].append(k)
            for a,b in groups.items():
                if len(list(b)) >= len(list(a)):
                    fp_out.write(",".join(list(b)) + "\n")
        return fp_out
    
        
root = Tk()
root.geometry("580x80+200+200")
root.title("Anagram program")
app = Anagrams(master=root)
app.mainloop()
root.destroy()

