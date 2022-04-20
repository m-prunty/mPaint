from tkinter import *

from pathlib import Path

class BuildGUI(Frame):
    """Builds the main GUI"""

    def __init__(self, root):
        """Initialises the frames for locating buttons and labels and
        the canvas, calls the build_buttons,build_labels and pack functions"""
        self.root = root
        self.root.title("mpPaint")
        self.dummy_frame = Frame(self.root)
        self.shape_frame = Frame(
            self.dummy_frame,
            highlightbackground="black",
            highlightthickness=2,
            )

        self.col_frame = Frame(
	        self.dummy_frame,
            highlightbackground="black",
            highlightthickness=2,
        )

        self.misc_frame = Frame(
            self.dummy_frame,
            highlightbackground="black",
            highlightthickness=2,
        )

        self.label_frame = Frame(self.dummy_frame)

        self.canvas = Canvas(self.root, bg="white", width=600, height=500)

        self._build_buttons()
        self._build_labels()
        self._pack_frames()

    def _pack_frames(self):
        """
        Packs the canvas and frames to there respective locations
        """
        self.label_frame.pack(side=BOTTOM, anchor=N)
        self.dummy_frame.pack(side=LEFT, anchor=NW)
        self.col_frame.pack(side=LEFT, anchor=NW)
        
        self.misc_frame.pack(side=BOTTOM, anchor=NE)
        self.shape_frame.pack(side=LEFT, anchor=NE)

        self.canvas.pack(side=RIGHT, anchor=NW, fill=BOTH, expand=YES)

        return self

    def _imgs(self):
        """
        Imports, scales and stores the images for the different buttons
        NOTE: If ANY file image cannot be found the current implementaion
        will set all images to None
        """
        self.loc = Path("imgs/" )
        try:
            self.circle_img = PhotoImage(file=self.loc / "circle.png").subsample(3)
            self.rect_img = PhotoImage(file=self.loc / "square.png").subsample(3)
            self.line_img = PhotoImage(file=self.loc / "line.png").subsample(3)

            self.fill_img = PhotoImage(file=self.loc / "fill.png").subsample(3)
            self.undo_img = PhotoImage(file=self.loc / "undo.png").subsample(3)
            self.clear_img = PhotoImage(file=self.loc / "clear.png").subsample(3)

            self.frame_img = PhotoImage(file=self.loc / "frame.png").subsample(3)

        except:
            print("Shape images not found: check location")

            self.circle_img = None
            self.rect_img = None
            self.line_img = None

            self.fill_img = None
            self.undo_img = None
            self.clear_img = None

            self.frame_img = None

        return self

    def _build_buttons(self):
        """
        calls the _imgs() function and sets each button to its required button class.
        Introduces a slider object for setting line width.
        NOTE: Command functions are set in respective Colours, Shapes and Main classes
        """

        self._imgs()

        self.size = Scale(
            self.shape_frame, 
            from_=0, to=20, 
            orient=VERTICAL, 
            length=112 if self.frame_img else 118
            )
        self.size.set(5)
        self.size.pack(side=BOTTOM, anchor=W)

        self.line_button = self.PicButton(self.shape_frame, "Line", self.line_img)
        self.oval_button = self.PicButton(self.shape_frame, "Circle", self.circle_img)
        self.rect_button = self.PicButton(self.shape_frame, "Rectangle", self.rect_img)

        self.fill_button = self.PicButton(self.misc_frame, "Fill", self.fill_img)
        self.undo_button = self.PicButton(self.misc_frame, "Undo", self.undo_img)
        self.clear_button = self.PicButton(self.misc_frame, "Clear", self.clear_img)

        self.black_button = self.ColourButton(self.col_frame, "Black", self.frame_img)
        self.red_button = self.ColourButton(self.col_frame, "Red", self.frame_img)
        self.orange_button = self.ColourButton(self.col_frame, "Orange", self.frame_img)
        self.yellow_button = self.ColourButton(self.col_frame, "Yellow", self.frame_img)
        self.green_button = self.ColourButton(self.col_frame, "Green", self.frame_img)
        self.blue_button = self.ColourButton(self.col_frame, "Blue", self.frame_img)
        self.indigo_button = self.ColourButton(self.col_frame, "Indigo", self.frame_img)
        self.violet_button = self.ColourButton(self.col_frame, "Violet", self.frame_img)
        self.white_button = self.ColourButton(self.col_frame, "White", self.frame_img)
        
        return self

    def _build_labels(self):
        """
        Initialises the labels for reporting various features
        """
        self.shape_pos_label = self.CustLabels(self.label_frame)
        self.curr_pos_label = self.CustLabels(self.label_frame)
        self.curr_shape_label = self.CustLabels(self.label_frame)
        self.curr_colour_label = self.CustLabels(self.label_frame)
        return self

    def popup(self):
        """Defines a popup box"""
        self.pop = Toplevel()
        self.pop.title("Error!!")

        self.pop_label = Label(
            self.pop, text="Choose a shape AND\n colour to get started"
        )
        self.pop_label.pack()

        self.pop_button = Button(self.pop, text="Okay", command=self.pop.destroy)
        self.pop_button.pack()

    class CustLabels(Label):
        """Metaclass that inherits from tk.Label"""

        def __init__(self, master):
            """
            Takes a labels master(associated frame) and packs in positon
            """
            super().__init__(master=master)
            self.pack(side=BOTTOM, anchor=S)

    class ColourButton(Button):
        """Metaclass that inherits from tk.Button"""

        def __init__(self, master, text, img=None, command=None):
            """
            Takes a colour buttons master(associated frame), name('text')
            assigns bg and fg colours based on 'text'. Takes an image if
            given, packs in positon
            """
            self.master = master
            self.text = text
            self.command = command
            self.frame = img
            print(self.text)
            super().__init__(
                master=self.master,
                text=self.text,
                command=self.command,
                image=self.frame,
                bg=self.text,
                fg=self.text,
                width=3 if not self.frame else 0,
                height=2 if not self.frame else 0,
                pady=3 if not self.frame else 0
            )

            self.pack(side=BOTTOM, anchor=W)

    class PicButton(Button):
        """Metaclass that inherits from tk.Button"""

        def __init__(self, master, text, img=None, command=None):
            """
            Takes a buttons master(associated frame), name('text'), image(if given)
            and packs in positon
            """
            self.master = master
            self.text = text
            self.command = command
            self.img = img

            super().__init__(
                master=self.master,
                text=self.text,
                
                command=self.command, 
                image=self.img, 
                width=5 if not self.img else 0,
                height=2 if not self.img else 0,
                pady=1 if not self.img else 0,
            )

            self.pack(side=BOTTOM, anchor=NW)
