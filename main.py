from tkinter import *
import evaluate as e
import matplotlib
import numpy as np

matplotlib.use("TkAgg")
from PIL import ImageTk, Image
import sys
import matplotlib.pyplot as plt
import threading


# D:\projects\BE-project\UCSD_Anomaly_Dataset\UCSD_Anomaly_Dataset\UCSD_Anomaly_Dataset.v1p2\UCSDped1\Test\Test001

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry('500x500')
        self.frames = {}
        self.dir = ""
        self.result = []

        for F in (start_page, evaluate, graph):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(start_page)

    def star_again(self):
        self.show_frame(start_page)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

    def entry_prepare_data(self, entry):
        data = entry.get()
        print(data)
        if data == "":
            print("please enter data..")
        elif "\\" in data:
            print("got data..")
            self.dir = data
            print("dir:" + self.dir)
            self.show_frame(evaluate)
        else:
            print("please enter a valid directory")

    def evaluate_data(self):
        print("running")
        # plotting graph for anomaly
        self.result = e.evaluate(self.dir.strip())
 #        self.result = [0.97208325, 0.97186781, 0.97216473, 0.97264416, 0.97313312, 0.97362102,
 # 0.97436067, 0.97489139,  0.97551999,  0.97630008, 0.97691266, 0.97776316,
 # 0.97861419, 0.97911279, 0.97938322, 0.97954717, 0.97965145, 0.97975583,
 # 0.97950545, 0.97911937, 0.97911528, 0.97904505, 0.97881034, 0.9784554,
 # 0.97809645, 0.97807034, 0.97807497, 0.97801105, 0.97825991, 0.97850634,
 # 0.97860092, 0.97903891, 0.97961945, 0.98015189, 0.98062937, 0.98103181,
 # 0.98119179, 0.98123962, 0.98126953, 0.9813519 , 0.98142848, 0.98154733,
 # 0.98166371, 0.98179394, 0.98201557, 0.98252599, 0.98358192 ,0.98467764,
 # 0.98544791, 0.98630212, 0.98695096, 0.98754363, 0.9881527 , 0.98872384,
 # 0.98918685, 0.98953235, 0.99001748, 0.9909016 , 0.99144911, 0.99192734,
 # 0.99219452, 0.99251509, 0.99249208, 0.9924972 , 0.99088381, 0.99110301,
 # 0.99112514, 0.99295506, 0.99334355, 0.99386621 ,0.99451988, 0.99490478,
 # 0.99519075, 0.9952766,  0.99506748, 0.99530484 ,0.99551346, 0.99585813,
 # 0.99654921, 0.99698153, 0.99719344, 0.9976173  ,0.99828752, 0.99909148,
 # 0.99920925, 0.99917878, 0.99937483, 0.9995657  ,0.99986687, 1.,
 # 0.99988167, 0.99933666, 0.99865033, 0.99821598, 0.99822506, 0.99805254,
 # 0.99792003, 0.99810143, 0.99843877, 0.99861836, 0.99898629, 0.99932002,
 # 0.99934463, 0.99911537, 0.99878715, 0.99846427, 0.99773232, 0.99671189,
 # 0.99593439, 0.99562102, 0.99525956, 0.99486467, 0.99471617, 0.99455584,
 # 0.99416377, 0.99370208, 0.99297733 ,0.99207202, 0.99118084, 0.99045647,
 # 0.99030036, 0.98975482, 0.98926017 ,0.98893135, 0.98890591, 0.98883525,
 # 0.98891546, 0.98907888, 0.98928375, 0.98943386, 0.98964357, 0.98957221,
 # 0.98954637, 0.98958443, 0.98926896, 0.98885486, 0.98808103, 0.98709229,
 # 0.98647659, 0.98569472, 0.98447042, 0.98317579, 0.98188043, 0.98061403,
 # 0.97960978, 0.97850054, 0.97786053, 0.97731187, 0.97686621, 0.97663245,
 # 0.9765723 , 0.9764841,  0.97616367, 0.97551581, 0.97501577, 0.97441943,
 # 0.97379898, 0.97320874, 0.97287497, 0.97262534, 0.97247176, 0.97218061,
 # 0.9721251 , 0.97211252, 0.97197943, 0.9718449 , 0.97146511, 0.97128475,
 # 0.97116814, 0.97114654, 0.97113061, 0.97075631, 0.97013294, 0.96991337,
 # 0.96945721, 0.96890057, 0.96870558, 0.96854589, 0.96840883, 0.96839813,
 # 0.96856409, 0.96917963, 0.96947422, 0.9692904,  0.96919638, 0.96951261,
 # 0.96973157, 0.96958439, 0.96909264, 0.96856127]
        self.show_frame(graph)

        plt.plot(self.result)
        plt.ylabel('regularity score Sr(t)')
        plt.xlabel('frame t')
        plt.show()




class start_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        space = Label(self, text="")
        label = Label(self, text="Enter directory path")
        label.pack()
        space.pack()

        space2 = Label(self, text="")
        entry = Entry(self, width=50)
        entry.pack()
        space2.pack()

        space3 = Label(self, text="")
        button = Button(self, text="Next", command=lambda: controller.entry_prepare_data(entry))
        button.pack()
        # pass the entry data( dir location to prepare_data)


class evaluate(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="click evaluate and wait")
        label.pack()

        space = Label(self, text="")
        space.pack()

        button = Button(self, text="evaluate", command=lambda: controller.evaluate_data())
        button.pack()


class graph(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        load = Image.open("example.PNG")
        resized = load.resize((500, 350), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resized)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=30)

        button = Button(self, text="Retest", command=lambda: controller.star_again())
        button.place(x=100, y=400)

        exit = Button(self, text="exit", command=lambda: sys.exit())
        exit.place(x=350, y=400)


app = App()
app.mainloop()
