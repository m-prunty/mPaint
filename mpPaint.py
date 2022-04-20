from tkinter import *

from gui import BuildGUI
from shapes import Shapes
from colours import Colours

class Main(object):
    """The Main body of mpPaint"""

    def __init__(self):
        """
        Initialises the root tkinter and calls _setup() for config and
         _reset()for coordinate variables
        """
        self.root = Tk()
        self._reset()
        self._setup()

    def _setup(self):
        """
        Instantiates the classes used, configures various butttons and labels,
        binds the main click function for drawing shapes and motion function,
        initialises id variable and id list for shapes
        """
        self.id = 0
        self.id_list = []

        self.gui = BuildGUI(self.root)
        self.shapes = Shapes(self.gui)
        self.colours = Colours(self.gui)
        
        self.gui.canvas.bind("<1>", self._click)

        self.shape_pos_var = StringVar()
        self.gui.shape_pos_label.configure(textvariable=self.shape_pos_var)
        self.gui.canvas.bind("<Motion>", self._motion)

        self.curr_pos_var = StringVar()
        self.gui.curr_pos_label.configure(textvariable=self.curr_pos_var)

        self.gui.fill_button.config(command=self.fill)
        self.active_fill = False

        self.gui.undo_button.config(command=self.undo)
        
        self.gui.clear_button.config(command=self.clear)

        

    def _reset(self):
        """Resets all variables associated with coords"""
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.coords = []

    def _click(self, event):
        """
        Main click function; If a shape and colour are selected takes a click event on the
        canvas area or else produces popup request.

        On first click stores x,y to x0,y0, second click will store as x1,y1 build coords variable,
        call _create_shape(), _corners() and finally reset the coords

        NOTE: Nested 'if' uses butt_watch (initialied in Shapes) to determine if a shape button was
        clicked in between the 1st and 2nd click and whether there are values stored for x0,y0 already

        """
        if self.shapes.get_shape() and self.colours.get_colour():
            if self.shapes.butt_watch and self.x0 and self.y0:

                self.x1 = event.x
                self.y1 = event.y

                self.coords = [
                    self.x0,
                    self.y0,
                    self.x1,
                    self.y1,
                ]

                self._create_shape()

                self.second = [self.x1, self.y1]
                self._corners()
                self._reset()
                return self.coords

            self.x0 = event.x
            self.y0 = event.y
            self.first = [self.x0, self.y0]
            self.shapes.butt_watch = 1

        else:
            self.gui.popup()

    def _create_shape(self):
        """
        determines which shape is selected and calls _create(cmd) with respective shape function
        """

        def _create(cmd):
            """
            A helper function that takes a tk.create command (cmd) determines whether fill has been
            selected or shape is a Line, then builds the shape from corrds, active colour and size
            """
            if self.active_fill or self.shapes.get_shape() == "Line":
                self.id = cmd(
                    self.coords,
                    fill=self.colours.get_colour(),
                    width=self.gui.size.get(),
                )
            else:
                self.id = cmd(
                    self.coords,
                    outline=self.colours.get_colour(),
                    width=self.gui.size.get(),
                )

            self.id_list.append(self.id)

        if self.shapes.get_shape() == "Rectangle":
            _create(self.gui.canvas.create_rectangle)

        if self.shapes.get_shape() == "Circle":
            _create(self.gui.canvas.create_oval)

        if self.shapes.get_shape() == "Line":
            _create(self.gui.canvas.create_line)

    

    def _motion(self, event):
        """
        Detects the xy coordinates of the mouse on the canvas and reports it to
        the respective label
        """
        x, y = event.x, event.y
        self.curr_pos_var.set(f"{x},{y}")

    def _corners(self):
        """
        Reports the top left and bottom right coordinates for any shape or the
        start and end points of a line
        """
        if self.shapes.get_shape() == "Line":
            self.shape_pos_var.set(
                f"Start Line: \n {self.first}\n End line:\n {self.second} "
            )

        else:
            if self.first[0] < self.second[0]:
                if self.first[1] < self.second[1]:
                    self.corn_coords = (
                        [self.first[0], self.first[1]],
                        [self.second[0], self.second[1]],
                    )
                else:
                    self.corn_coords = (
                        [self.first[0], self.second[1]],
                        [self.second[0], self.first[1]],
                    )
            else:
                if self.first[1] < self.second[1]:
                    self.corn_coords = (
                        [self.second[0], self.first[1]],
                        [self.first[0], self.second[1]],
                    )
                else:
                    self.corn_coords = (
                        [self.second[0], self.second[1]],
                        [self.first[0], self.first[1]],
                    )

            self.shape_pos_var.set(
                f"Top left:\n {self.corn_coords[0]}\n Low right:\n {self.corn_coords[1]}"
            )

    def _switch(self, button, var_):
        """
        A helper function to switch a buttons state between active and inactive
        Takes a button type object and a state variable. Returns altered state,
        implement as var = switch(button, var)

        """
        self._button = button
        self._var = var_
        if not self._var:
            self._button.config(relief=SUNKEN)
            self._var = True

        else:
            self._button.config(relief=RAISED)
            self._var = False

        return self._var

    def fill(self):
        """Toggles shape fill option"""
        self.active_fill = self._switch(self.gui.fill_button, self.active_fill)

    def clear(self):
        """deletes all shapes on canvas and clears id list"""
        self.gui.canvas.delete("all")
        self.id_list = []

    def undo(self):
        """Undos last shape created, pops last item added to id list and deletes respective 
        shape. Current implemntation cannot undo delete """
        if self.id_list:
            self.gui.canvas.delete(f"{self.id_list.pop()}")

Main().root.mainloop()
