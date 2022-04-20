from tkinter import *

class Colours:
    """Colours class stores methods associated with defining colours"""

    def __init__(self, gui):
        """
        Initialises the gui created in BuilGUI, calls _setup_colour_cmds,
        detects if a colour is set and if not sets the colour label to
        'Pick colour'
        """
        self.gui = gui

        self._setup_colour_cmds()
        if not self.get_colour():
            self.colour_var.set("Pick colour")

    def _setup_colour_cmds(self):
        """
        Assigns methods to their respective buttons, initialises state variables
        """

        self.active_colour = None
        self.colour_var = StringVar()

        self.gui.black_button.config(command=self.black)
        self.gui.white_button.config(command=self.white)
        self.gui.red_button.config(command=self.red)
        self.gui.orange_button.config(command=self.orange)
        self.gui.yellow_button.config(command=self.yellow)
        self.gui.green_button.config(command=self.green)
        self.gui.blue_button.config(command=self.blue)
        self.gui.indigo_button.config(command=self.indigo)
        self.gui.violet_button.config(command=self.violet)
        
        self.gui.curr_colour_label.config(textvariable=self.colour_var)

    def set_colour(self, colour):
        """
        Takes a button class object 'colour',if an active colour exists
        changes button state, sets active colour to new button and updates
        colour label
        """
        if self.active_colour:
            self.active_colour.config(relief=RAISED)

        self.active_colour = colour

        colour.config(relief=SUNKEN)
        self.colour_var.set(self.active_colour.text)

    def get_colour(self):
        """returns the current active colour if it exists"""
        if self.active_colour:
            return self.active_colour.text
    #Red, orange, yellow, green, blue, indigo, violet
    def black(self):
        """calls set_colour method to set black_button as active"""
        self.set_colour(self.gui.black_button)
        return self
    
    def white(self):
        """calls set_colour method to set white_button as active
        NOTE: White with fill function will look the same on a blank canvas as 
        a shape drawn in black with no fill unless width is set to 0"""
        self.set_colour(self.gui.white_button)
        return self

    def red(self):
        """calls set_colour method to set red_button as active"""
        self.set_colour(self.gui.red_button)
        return self

    def orange(self):
        """calls set_colour method to set orange_button as active"""
        self.set_colour(self.gui.orange_button)
        return self

    def yellow(self):
        """calls set_colour method to set yellow_button as active"""
        self.set_colour(self.gui.yellow_button)
        return self

    def green(self):
        """calls set_colour method to set green_button as active"""
        self.set_colour(self.gui.green_button)
        return self
    
    def blue(self):
        """calls set_colour method to set blue_button as active"""
        self.set_colour(self.gui.blue_button)
        return self
    
    def indigo(self):
        """calls set_colour method to set indigo_button as active"""
        self.set_colour(self.gui.indigo_button)
        return self

    def violet(self):
        """calls set_colour method to set violet_button as active"""
        self.set_colour(self.gui.violet_button)
        return self

    colour = property(get_colour, set_colour)
