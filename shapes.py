from tkinter import *

class Shapes:
    """
    Shapes class stores methods associated with building shapes
    """

    def __init__(self, gui):
        """
        Initialises the gui created in BuilGUI, calls _setup_shape_cmds,
        detects if a shape is set and if not sets the shape label to 'Pick Shape'
        """
        self.gui = gui

        self._setup_shape_cmds()
        if not self.get_shape():
            self.shape_var.set("Pick shape")

    def _setup_shape_cmds(self):
        """
        Assigns methods to their respective buttons, initialises state and watcher
        variables
        """
        self.gui.rect_button.config(command=self.rect)
        self.gui.line_button.config(command=self.line)
        self.gui.oval_button.config(command=self.oval)

        self.active_shape = None
        self.shape_var = StringVar()

        self.gui.curr_shape_label.config(textvariable=self.shape_var)

        self.butt_watch = 0

    def rect(self):
        """calls set_shape method to set rect_button as active"""
        self.set_shape(self.gui.rect_button)
        return self

    def oval(self):
        """calls set_shape method to set oval_button as active"""
        self.set_shape(self.gui.oval_button)
        return self

    def line(self):
        """calls set_shape method to set line_button as active"""
        self.set_shape(self.gui.line_button)
        return self

    def set_shape(self, shape):
        """
        Takes a button class object 'shape', Sets the button watcher to 0,
        if an active shape exists changes button state, sets active shape
        to new button and updates shape label
        """
        self.butt_watch = 0
        if self.active_shape:
            self.active_shape.config(relief=RAISED)

        self.active_shape = shape
        shape.config(relief=SUNKEN)
        self.shape_var.set(self.active_shape.text)
        return self

    def get_shape(self):
        """returns the current active shape if it exists"""
        if self.active_shape:
            return self.active_shape.text

    shape = property(get_shape, set_shape)