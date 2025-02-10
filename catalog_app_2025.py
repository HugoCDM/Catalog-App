from tkinter import Tk, Frame, Label, Entry, Listbox
from tkinter import ttk
from functions import *


class CatalogApp(Functions):
    def __init__(self):

        # First a Tkinter window will open
        self.tk = Tk()
        self.tk.geometry('1200x650')
        self.tk.title('Catálogo 2025')
        self.tk.resizable(False, False)
        self.tk.configure(bg='#b82323')

        # Some functions will load from the beginning such as frames and labels which make the window
        self.frames()

        self.labels()

        # It's necessary that self.update loads the dictionary uniforms otherwise an empty list is shown
        self.update(uniforms)

        # A bind that ensures all windows are closed when clicking on X at the main window
        self.tk.protocol('WM_DELETE_WINDOW', self.close_windows)

        # Starts the program
        self.tk.mainloop()

    def frames(self):

        self.frame_1 = Frame(bg='#dcdfe3', width=1250, height=650)
        self.frame_1.place(x=0, y=0)

        self.tk_entry = Entry(self.frame_1, width=104, font=('Verdana', 13))
        self.tk_entry.place(relx=0.02, rely=0.075)

        # A bind for searched text in the bar
        self.tk_entry.bind('<KeyRelease>', self.check)

        self.frame_red_outline = Frame(bg='#b82323', width=1152, height=460)
        self.frame_red_outline.place(relx=0.02, rely=0.135)

        self.frame_white_bottom_bar = Frame(
            bg='white', width=1152, height=80, border=1)
        self.frame_white_bottom_bar.place(relx=0.02, rely=0.843)

        self.frame_black_top_bar = Frame(bg='white', width=1152, height=40)
        self.frame_black_top_bar.place(relx=0.02, rely=0.135)

        # List Box
        self.tk_list = Listbox(
            self.frame_red_outline, width=103, height=19, font=('Verdana', 13))
        self.tk_list.place(relx=0.007, rely=0.105)

        # Clicking on a item on the list calls the function fillout
        self.tk_list.bind('<<ListboxSelect>>', self.fillout)

        # Clicking Enter on a item on the list calls the function calculator
        self.tk_list.bind('<Return>', self.calculator)

    def labels(self):

        self.label_products = Label(self.tk, text='Produto', font=(
            'Helvetica', 15, ' bold'), bg='#dcdfe3', fg='#b82323')
        self.label_products.place(relx=0.015, rely=0.0285)

        self.label_infos = Label(self.frame_black_top_bar, text='Informações',
                                 bg='white', fg='#b82323', font=('Futura', 20, 'bold'))
        self.label_infos.place(relx=0.5, rely=0.5, anchor='c')

        self.var = IntVar()
        self.checkbox = Checkbutton(self.frame_1, text='Calculadora ', bg='#dcdfe3', font=(
            'Helvetica', 12), variable=self.var, command=self.show_calculator)
        self.checkbox.place(relx=0.85, rely=0.02)
        print(self.var.get())

        self.var_embroidery_calculator = IntVar()

        self.checkbox = Checkbutton(self.frame_1, text='Calculadora Bordado', bg='#dcdfe3', font=(
            'Helvetica', 12), variable=self.var_embroidery_calculator, command=self.embroidery_screen)
        self.checkbox.place(relx=0.7, rely=0.02)
        print(self.var.get())

    def close_windows(self):
        try:
            self.window.destroy()
            self.tk.destroy()
        except:
            self.tk.destroy()


if __name__ == '__main__':
    CatalogApp()
