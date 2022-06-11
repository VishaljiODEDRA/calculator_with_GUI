import tkinter


class calculate:
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.title("Modern Calculator")

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.mid_frame2 = tkinter.Frame(self.mw)
        self.mid_frame3 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)
        self.bottom_frame1 = tkinter.Frame(self.mw)

        self.equation = tkinter.StringVar()
        self.result = tkinter.IntVar()
        self.ask_input_label = tkinter.Label(self.top_frame,
                                             textvariable=self.equation,
                                             background="black",
                                             foreground="white")
        self.total_label = tkinter.Label(self.top_frame, text=" = ")
        self.cal_total_label = tkinter.Label(self.top_frame,
                                             textvariable=self.result,
                                             background="blue",
                                             foreground="white")

        self.ask_input_label.pack(side="left")
        self.total_label.pack(side="left")
        self.cal_total_label.pack(side="left")

        self.input1 = tkinter.Button(
            self.mid_frame1,
            text="1",
            command=lambda event="1": self.button_click(event))
        self.input2 = tkinter.Button(
            self.mid_frame1,
            text="2",
            command=lambda event="2": self.button_click(event))
        self.input3 = tkinter.Button(
            self.mid_frame1,
            text="3",
            command=lambda event="3": self.button_click(event))

        self.input_add = tkinter.Button(
            self.mid_frame1,
            text="+",
            command=lambda event="+": self.button_click(event))

        self.input4 = tkinter.Button(
            self.mid_frame2,
            text="4",
            command=lambda event="4": self.button_click(event))
        self.input5 = tkinter.Button(
            self.mid_frame2,
            text="5",
            command=lambda event="5": self.button_click(event))
        self.input6 = tkinter.Button(
            self.mid_frame2,
            text="6",
            command=lambda event="6": self.button_click(event))

        self.input_minus = tkinter.Button(
            self.mid_frame2,
            text="-",
            command=lambda event="-": self.button_click(event))

        self.input7 = tkinter.Button(
            self.mid_frame3,
            text="7",
            command=lambda event="7": self.button_click(event))
        self.input8 = tkinter.Button(
            self.mid_frame3,
            text="8",
            command=lambda event="8": self.button_click(event))
        self.input9 = tkinter.Button(
            self.mid_frame3,
            text="9",
            command=lambda event="9": self.button_click(event))

        self.input_multi = tkinter.Button(
            self.mid_frame3,
            text="*",
            command=lambda event="*": self.button_click(event))

        self.input_point = tkinter.Button(
            self.bottom_frame,
            text=".",
            command=lambda event=".": self.button_click(event))
        self.input_zero = tkinter.Button(
            self.bottom_frame,
            text="0",
            command=lambda event="0": self.button_click(event))
        self.input_equal = tkinter.Button(self.bottom_frame,
                                          text="=",
                                          command=self.equals)

        self.input_div = tkinter.Button(
            self.bottom_frame,
            text="/",
            command=lambda event="/": self.button_click(event))

        self.clear_button = tkinter.Button(self.bottom_frame1,
                                           text="Clear",
                                           command=self.clear)

        self.input1.pack(side="left")
        self.input2.pack(side="left")
        self.input3.pack(side="left")
        self.input_add.pack(side="left")
        self.input4.pack(side="left")
        self.input5.pack(side="left")
        self.input6.pack(side="left")
        self.input_minus.pack(side="left")
        self.input7.pack(side="left")
        self.input8.pack(side="left")
        self.input9.pack(side="left")
        self.input_multi.pack(side="left")
        self.input_point.pack(side="left")
        self.input_zero.pack(side="left")
        self.input_equal.pack(side="left")
        self.input_div.pack(side="left")
        self.clear_button.pack(side="left")

        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.mid_frame3.pack()
        self.bottom_frame.pack()
        self.bottom_frame1.pack()

        tkinter.mainloop()

    def button_click(self, button_pressed):
        equation_string = self.equation.get() + button_pressed
        self.equation.set(equation_string)

    def equals(self):
        if "/0" in self.equation.get():
            self.result.set("Division by 0 is Impossible.")
        else:
            self.result.set(eval(self.equation.get()))

    def clear(self):
        self.equation.set("")
        self.result.set("")


calculate()