from tkinter import *


class TrafficLight:
    def __init__(self):
        self.__color = (('red', 'yellow', 'green'), ('#440000', '#444400', '#004400'))
        self.lights = [(Frame(root, width=200, height=200), 7000),
                       (Frame(root, width=200, height=200), 2000),
                       (Frame(root, width=200, height=200), 7000)]

    def running(self, counter=0):
        for i, a in enumerate(self.lights):
            a[0]['bg'] = self.__color[i != counter % 3][i]
        root.after(self.lights[counter % 3][1], self.running, counter + 1)


root = Tk()
trafficLight = TrafficLight()
for a in trafficLight.lights:
    a[0].pack()
trafficLight.running()
root.mainloop()
