from tkinter import *
from tkinter import ttk
import smootwin

class VerticalScrolledFrame(Frame):
    
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        
        style =ttk.Style()
        style.theme_use("clam")
        style.configure("Vertical.TScrollbar",gripcount =0,activebackground=smootwin.DGRAY,background=smootwin.BGRAY,troughcolor=smootwin.DGRAY,arrowsize=10,borderwidth=1,bordercolor=smootwin.DGRAY,lightcolor=smootwin.BGRAY,darkcolor=smootwin.BGRAY)
        style.map('Vertical.TScrollbar', background=[('active', smootwin.BGRAY)])
        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,yscrollcommand=vscrollbar.set,bg=smootwin.DGRAY)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = Frame(canvas,bg=smootwin.DGRAY,highlightthickness=0,bd=0)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
