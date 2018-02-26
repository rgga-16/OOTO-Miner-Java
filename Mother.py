#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Feb 26, 2018 11:23:01 AM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Mother_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    Mother_support.set_Tk_var()
    top = OOTO_Miner (root)
    Mother_support.init(root, top)
    root.mainloop()

w = None
def create_OOTO_Miner(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    Mother_support.set_Tk_var()
    top = OOTO_Miner (w)
    Mother_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_OOTO_Miner():
    global w
    w.destroy()
    w = None


class OOTO_Miner:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1000x600+522+139")
        top.title("OOTO Miner")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.buttonTest = Button(top)
        self.buttonTest.place(relx=0.51, rely=0.93, height=33, width=486)
        self.buttonTest.configure(activebackground="#d9d9d9")
        self.buttonTest.configure(activeforeground="#000000")
        self.buttonTest.configure(background="#d9d9d9")
        self.buttonTest.configure(disabledforeground="#a3a3a3")
        self.buttonTest.configure(foreground="#000000")
        self.buttonTest.configure(highlightbackground="#d9d9d9")
        self.buttonTest.configure(highlightcolor="black")
        self.buttonTest.configure(pady="0")
        self.buttonTest.configure(text='''Test''')


        testTypeValues = ["Chi-Test", "Z-score test of independence of pooled proportions", "Standard Error of Population"]
        self.comboBoxTestType = ttk.Combobox(top)
        self.comboBoxTestType.place(relx=0.01, rely=0.02, relheight=0.04
                , relwidth=0.49)
        self.comboBoxTestType.configure(exportselection="0")
        self.comboBoxTestType.configure(textvariable=Mother_support.combobox)
        self.comboBoxTestType.configure(takefocus="")
        self.comboBoxTestType.configure(values=testTypeValues)

        self.buttonTestType = Button(top)
        self.buttonTestType.place(relx=0.01, rely=0.07, height=23, width=486)
        self.buttonTestType.configure(activebackground="#d9d9d9")
        self.buttonTestType.configure(activeforeground="#000000")
        self.buttonTestType.configure(background="#d9d9d9")
        self.buttonTestType.configure(disabledforeground="#a3a3a3")
        self.buttonTestType.configure(foreground="#000000")
        self.buttonTestType.configure(highlightbackground="#d9d9d9")
        self.buttonTestType.configure(highlightcolor="black")
        self.buttonTestType.configure(pady="0")
        self.buttonTestType.configure(text='''Select Test''')

        self.entryPopulation = Entry(top)
        self.entryPopulation.place(relx=0.01, rely=0.12, relheight=0.04
                , relwidth=0.48)
        self.entryPopulation.configure(background="white")
        self.entryPopulation.configure(disabledforeground="#a3a3a3")
        self.entryPopulation.configure(font="TkFixedFont")
        self.entryPopulation.configure(foreground="#000000")
        self.entryPopulation.configure(highlightbackground="#d9d9d9")
        self.entryPopulation.configure(highlightcolor="black")
        self.entryPopulation.configure(insertbackground="black")
        self.entryPopulation.configure(selectbackground="#c4c4c4")
        self.entryPopulation.configure(selectforeground="black")

        self.buttonPopulation = Button(top)
        self.buttonPopulation.place(relx=0.01, rely=0.17, height=23, width=486)
        self.buttonPopulation.configure(activebackground="#d9d9d9")
        self.buttonPopulation.configure(activeforeground="#000000")
        self.buttonPopulation.configure(background="#d9d9d9")
        self.buttonPopulation.configure(disabledforeground="#a3a3a3")
        self.buttonPopulation.configure(foreground="#000000")
        self.buttonPopulation.configure(highlightbackground="#d9d9d9")
        self.buttonPopulation.configure(highlightcolor="black")
        self.buttonPopulation.configure(pady="0")
        self.buttonPopulation.configure(text='''Upload Population''')

        self.labelFrameZTest = LabelFrame(top)
        self.labelFrameZTest.place(relx=0.51, rely=0.0, relheight=0.93
                , relwidth=0.48)
        self.labelFrameZTest.configure(relief=GROOVE)
        self.labelFrameZTest.configure(foreground="black")
        self.labelFrameZTest.configure(text='''Z -Test''')
        self.labelFrameZTest.configure(background="#d9d9d9")
        self.labelFrameZTest.configure(highlightbackground="#d9d9d9")
        self.labelFrameZTest.configure(highlightcolor="black")
        self.labelFrameZTest.configure(width=480)

        self.labelZCriticalValue = Label(self.labelFrameZTest)
        self.labelZCriticalValue.place(relx=0.02, rely=0.06, height=26
                , width=108)
        self.labelZCriticalValue.configure(activebackground="#f9f9f9")
        self.labelZCriticalValue.configure(activeforeground="black")
        self.labelZCriticalValue.configure(background="#d9d9d9")
        self.labelZCriticalValue.configure(disabledforeground="#a3a3a3")
        self.labelZCriticalValue.configure(foreground="#000000")
        self.labelZCriticalValue.configure(highlightbackground="#d9d9d9")
        self.labelZCriticalValue.configure(highlightcolor="black")
        self.labelZCriticalValue.configure(text='''Z-Critical Value''')

        self.labelFeature = Label(self.labelFrameZTest)
        self.labelFeature.place(relx=0.02, rely=0.11, height=26, width=55)
        self.labelFeature.configure(activebackground="#f9f9f9")
        self.labelFeature.configure(activeforeground="black")
        self.labelFeature.configure(background="#d9d9d9")
        self.labelFeature.configure(disabledforeground="#a3a3a3")
        self.labelFeature.configure(foreground="#000000")
        self.labelFeature.configure(highlightbackground="#d9d9d9")
        self.labelFeature.configure(highlightcolor="black")
        self.labelFeature.configure(text='''Feature''')

        self.textFeature = Text(self.labelFrameZTest)
        self.textFeature.place(relx=0.02, rely=0.17, relheight=0.1
                , relwidth=0.95)
        self.textFeature.configure(background="white")
        self.textFeature.configure(exportselection="0")
        self.textFeature.configure(font="TkTextFont")
        self.textFeature.configure(foreground="black")
        self.textFeature.configure(highlightbackground="#d9d9d9")
        self.textFeature.configure(highlightcolor="black")
        self.textFeature.configure(insertbackground="black")
        self.textFeature.configure(selectbackground="#c4c4c4")
        self.textFeature.configure(selectforeground="black")
        self.textFeature.configure(width=454)
        self.textFeature.configure(wrap=WORD)

        self.listAttributes = Listbox(self.labelFrameZTest)
        self.listAttributes.place(relx=0.02, rely=0.27, relheight=0.72
                , relwidth=0.95)
        self.listAttributes.configure(background="white")
        self.listAttributes.configure(disabledforeground="#a3a3a3")
        self.listAttributes.configure(exportselection="0")
        self.listAttributes.configure(font="TkFixedFont")
        self.listAttributes.configure(foreground="#000000")
        self.listAttributes.configure(highlightbackground="#d9d9d9")
        self.listAttributes.configure(highlightcolor="black")
        self.listAttributes.configure(selectbackground="#c4c4c4")
        self.listAttributes.configure(selectforeground="black")
        self.listAttributes.configure(width=454)

        self.entryCriticalValue = Entry(self.labelFrameZTest)
        self.entryCriticalValue.place(relx=0.25, rely=0.05, relheight=0.04
                , relwidth=0.72)
        self.entryCriticalValue.configure(background="white")
        self.entryCriticalValue.configure(disabledforeground="#a3a3a3")
        self.entryCriticalValue.configure(font="TkFixedFont")
        self.entryCriticalValue.configure(foreground="#000000")
        self.entryCriticalValue.configure(insertbackground="black")
        self.entryCriticalValue.configure(width=344)

        self.labelFrameGenerateSamples = LabelFrame(top)
        self.labelFrameGenerateSamples.place(relx=0.01, rely=0.22, relheight=0.78
                , relwidth=0.49)
        self.labelFrameGenerateSamples.configure(relief=GROOVE)
        self.labelFrameGenerateSamples.configure(foreground="black")
        self.labelFrameGenerateSamples.configure(text='''Generate Samples''')
        self.labelFrameGenerateSamples.configure(background="#d9d9d9")
        self.labelFrameGenerateSamples.configure(highlightbackground="#d9d9d9")
        self.labelFrameGenerateSamples.configure(highlightcolor="black")
        self.labelFrameGenerateSamples.configure(width=490)

        self.entrySample = Entry(self.labelFrameGenerateSamples)
        self.entrySample.place(relx=0.02, rely=0.05, relheight=0.05
                , relwidth=0.46)
        self.entrySample.configure(background="white")
        self.entrySample.configure(disabledforeground="#a3a3a3")
        self.entrySample.configure(font="TkFixedFont")
        self.entrySample.configure(foreground="#000000")
        self.entrySample.configure(highlightbackground="#d9d9d9")
        self.entrySample.configure(highlightcolor="black")
        self.entrySample.configure(insertbackground="black")
        self.entrySample.configure(selectbackground="#c4c4c4")
        self.entrySample.configure(selectforeground="black")

        self.entryFocus = Entry(self.labelFrameGenerateSamples)
        self.entryFocus.place(relx=0.51, rely=0.05, relheight=0.05
                , relwidth=0.46)
        self.entryFocus.configure(background="white")
        self.entryFocus.configure(disabledforeground="#a3a3a3")
        self.entryFocus.configure(font="TkFixedFont")
        self.entryFocus.configure(foreground="#000000")
        self.entryFocus.configure(highlightbackground="#d9d9d9")
        self.entryFocus.configure(highlightcolor="black")
        self.entryFocus.configure(insertbackground="black")
        self.entryFocus.configure(selectbackground="#c4c4c4")
        self.entryFocus.configure(selectforeground="black")

        self.buttonSample = Button(self.labelFrameGenerateSamples)
        self.buttonSample.place(relx=0.02, rely=0.11, height=23, width=226)
        self.buttonSample.configure(activebackground="#d9d9d9")
        self.buttonSample.configure(activeforeground="#000000")
        self.buttonSample.configure(background="#d9d9d9")
        self.buttonSample.configure(disabledforeground="#a3a3a3")
        self.buttonSample.configure(foreground="#000000")
        self.buttonSample.configure(highlightbackground="#d9d9d9")
        self.buttonSample.configure(highlightcolor="black")
        self.buttonSample.configure(pady="0")
        self.buttonSample.configure(text='''Enter Sample Feature''')

        self.buttonFocus = Button(self.labelFrameGenerateSamples)
        self.buttonFocus.place(relx=0.51, rely=0.11, height=23, width=226)
        self.buttonFocus.configure(activebackground="#d9d9d9")
        self.buttonFocus.configure(activeforeground="#000000")
        self.buttonFocus.configure(background="#d9d9d9")
        self.buttonFocus.configure(disabledforeground="#a3a3a3")
        self.buttonFocus.configure(foreground="#000000")
        self.buttonFocus.configure(highlightbackground="#d9d9d9")
        self.buttonFocus.configure(highlightcolor="black")
        self.buttonFocus.configure(pady="0")
        self.buttonFocus.configure(text='''Enter Focus Feature''')

        self.buttonShowA = Button(self.labelFrameGenerateSamples)
        self.buttonShowA.place(relx=0.02, rely=0.24, height=23, width=226)
        self.buttonShowA.configure(activebackground="#d9d9d9")
        self.buttonShowA.configure(activeforeground="#000000")
        self.buttonShowA.configure(background="#d9d9d9")
        self.buttonShowA.configure(disabledforeground="#a3a3a3")
        self.buttonShowA.configure(foreground="#000000")
        self.buttonShowA.configure(highlightbackground="#d9d9d9")
        self.buttonShowA.configure(highlightcolor="black")
        self.buttonShowA.configure(pady="0")
        self.buttonShowA.configure(text='''Show Features A''')

        self.buttonShowB = Button(self.labelFrameGenerateSamples)
        self.buttonShowB.place(relx=0.51, rely=0.24, height=23, width=226)
        self.buttonShowB.configure(activebackground="#d9d9d9")
        self.buttonShowB.configure(activeforeground="#000000")
        self.buttonShowB.configure(background="#d9d9d9")
        self.buttonShowB.configure(disabledforeground="#a3a3a3")
        self.buttonShowB.configure(foreground="#000000")
        self.buttonShowB.configure(highlightbackground="#d9d9d9")
        self.buttonShowB.configure(highlightcolor="black")
        self.buttonShowB.configure(pady="0")
        self.buttonShowB.configure(text='''Show Features B''')

        self.listFeatA = Listbox(self.labelFrameGenerateSamples)
        self.listFeatA.place(relx=0.02, rely=0.31, relheight=0.58, relwidth=0.46)

        self.listFeatA.configure(background="white")
        self.listFeatA.configure(disabledforeground="#a3a3a3")
        self.listFeatA.configure(exportselection="0")
        self.listFeatA.configure(font="TkFixedFont")
        self.listFeatA.configure(foreground="#000000")
        self.listFeatA.configure(highlightbackground="#d9d9d9")
        self.listFeatA.configure(highlightcolor="black")
        self.listFeatA.configure(selectbackground="#c4c4c4")
        self.listFeatA.configure(selectforeground="black")
        self.listFeatA.configure(width=224)

        self.listFeatB = Listbox(self.labelFrameGenerateSamples)
        self.listFeatB.place(relx=0.51, rely=0.31, relheight=0.58, relwidth=0.46)

        self.listFeatB.configure(background="white")
        self.listFeatB.configure(disabledforeground="#a3a3a3")
        self.listFeatB.configure(exportselection="0")
        self.listFeatB.configure(font="TkFixedFont")
        self.listFeatB.configure(foreground="#000000")
        self.listFeatB.configure(highlightbackground="#d9d9d9")
        self.listFeatB.configure(highlightcolor="black")
        self.listFeatB.configure(selectbackground="#c4c4c4")
        self.listFeatB.configure(selectforeground="black")
        self.listFeatB.configure(width=224)

        self.buttonSaveDatasets = Button(self.labelFrameGenerateSamples)
        self.buttonSaveDatasets.place(relx=0.02, rely=0.91, height=33, width=466)

        self.buttonSaveDatasets.configure(activebackground="#d9d9d9")
        self.buttonSaveDatasets.configure(activeforeground="#000000")
        self.buttonSaveDatasets.configure(background="#d9d9d9")
        self.buttonSaveDatasets.configure(disabledforeground="#a3a3a3")
        self.buttonSaveDatasets.configure(foreground="#000000")
        self.buttonSaveDatasets.configure(highlightbackground="#d9d9d9")
        self.buttonSaveDatasets.configure(highlightcolor="black")
        self.buttonSaveDatasets.configure(pady="0")
        self.buttonSaveDatasets.configure(text='''Save Datasets''')

        self.entryFeatA = Entry(self.labelFrameGenerateSamples)
        self.entryFeatA.place(relx=0.02, rely=0.17, relheight=0.05
                , relwidth=0.46)
        self.entryFeatA.configure(background="white")
        self.entryFeatA.configure(disabledforeground="#a3a3a3")
        self.entryFeatA.configure(font="TkFixedFont")
        self.entryFeatA.configure(foreground="#000000")
        self.entryFeatA.configure(insertbackground="black")
        self.entryFeatA.configure(width=224)

        self.entryFeatB = Entry(self.labelFrameGenerateSamples)
        self.entryFeatB.place(relx=0.51, rely=0.17, relheight=0.05
                , relwidth=0.46)
        self.entryFeatB.configure(background="white")
        self.entryFeatB.configure(disabledforeground="#a3a3a3")
        self.entryFeatB.configure(font="TkFixedFont")
        self.entryFeatB.configure(foreground="#000000")
        self.entryFeatB.configure(insertbackground="black")
        self.entryFeatB.configure(width=224)

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event):
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#d9d9d9")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(font="{Segoe UI} 9")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()



