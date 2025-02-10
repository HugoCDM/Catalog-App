from tkinter import Tk, Frame, Label, Entry, ttk, Button, Event, END


class Embroidery:
    def embroidery_calculator(self):
        self.window = Tk()
        self.window.geometry('400x300')
        self.window.resizable(False, False)
        self.window.title('Calculadora')

        # Frames
        self.frame_main = Frame(self.window, bg='#b82323')
        self.frame_main.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Labels
        self.label_calculator = Label(self.window, text='Calculadora Bordado', font=(
            'Helvetica', 20, 'bold'), width=450, bg='#871010', height=2, fg="white")
        self.label_calculator.place(relx=0.5, rely=0.1, anchor='c')

        self.label_qty = Label(self.frame_main, text='Quantidade',
                               fg='white', bg='#b82323', font=('Arial', 15, 'bold'))
        self.label_qty.place(relx=0.2, rely=0.35, relheight=0.1)

        self.embroidery_value = Label(self.frame_main, text='Personalização',
                                      fg='white', bg='#b82323', font=('Arial', 15, 'bold'))
        self.embroidery_value.place(relx=0.125, rely=0.45, relheight=0.1)

        self.label_result_text_area = Label(
            self.frame_main, text='', fg='white', bg='#b82323', font=('Arial', 12, 'bold'))
        self.label_result_text_area.place(relx=0.08, rely=0.74,
                                          relheight=0.2, relwidth=0.83)

        # Entrys
        self.entry_qty = Entry(self.frame_main, relief='flat')
        self.entry_qty.place(relx=0.52, rely=0.377,
                             relheight=0.06, relwidth=0.385)

        # Buttons
        self.btn_send = Button(self.frame_main, relief='flat',
                               text='Enviar', command=self.send)
        self.btn_send.place(relx=0.757, rely=0.57,
                            relheight=0.07, relwidth=0.15)

        # Combobox
        self.combo = ttk.Combobox(self.frame_main, width=22, values=['Somente letras até 8cm',
                                                                     'Somente letras até 16cm', 'Logo sem fundo até 8cm', 'Logo sem fundo até 16cm',
                                                                     'Logo com fundo até 8cm', 'Logo com fundo até 16cm'])
        self.combo.place(relx=0.52, rely=0.47)
        self.combo_get = self.combo.bind("<<ComboboxSelected>>", self.combos)

        self.window.mainloop()

    def combos(self, eventObject):

        self.combo_get = self.combo.get()
        return self.combo_get

    def send(self):

        self.get_qty = self.entry_qty.get()
        self.combos(Event)

        if int(self.get_qty) == 1 and self.combo_get == 'Somente letras até 8cm':
            corresponding_value = 72.00
            description = 'Personalizando 1 item,\nadiciona:'

        elif 2 <= int(self.get_qty) <= 3 and self.combo_get == 'Somente letras até 8cm':
            corresponding_value = 24.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 4 <= int(self.get_qty) <= 7 and self.combo_get == 'Somente letras até 8cm':
            corresponding_value = 10.29
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 8 <= int(self.get_qty) <= 11 and self.combo_get == 'Somente letras até 8cm':
            corresponding_value = 6.55
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) >= 12 and self.combo_get == 'Somente letras até 8cm':
            corresponding_value = 6.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) == 1 and self.combo_get == 'Somente letras até 16cm':
            corresponding_value = 96.00
            description = 'Personalizando 1 item,\nadiciona:'

        elif 2 <= int(self.get_qty) <= 3 and self.combo_get == 'Somente letras até 16cm':
            corresponding_value = 32.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 4 <= int(self.get_qty) <= 7 and self.combo_get == 'Somente letras até 16cm':
            corresponding_value = 13.71
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 8 <= int(self.get_qty) <= 11 and self.combo_get == 'Somente letras até 16cm':
            corresponding_value = 8.73
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) >= 12 and self.combo_get == 'Somente letras até 16cm':
            corresponding_value = 8.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) == 1 and self.combo_get == 'Logo sem fundo até 8cm':
            corresponding_value = 108.00
            description = 'Personalizando 1 item,\nadiciona:'

        elif 2 <= int(self.get_qty) <= 3 and self.combo_get == 'Logo sem fundo até 8cm':
            corresponding_value = 36.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 4 <= int(self.get_qty) <= 7 and self.combo_get == 'Logo sem fundo até 8cm':
            corresponding_value = 15.43
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 8 <= int(self.get_qty) <= 11 and self.combo_get == 'Logo sem fundo até 8cm':
            corresponding_value = 9.82
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) >= 12 and self.combo_get == 'Logo sem fundo até 8cm':
            corresponding_value = 9.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) == 1 and self.combo_get == 'Logo sem fundo até 16cm':
            corresponding_value = 156.00
            description = 'Personalizando 1 item,\nadiciona:'

        elif 2 <= int(self.get_qty) <= 3 and self.combo_get == 'Logo sem fundo até 16cm':
            corresponding_value = 52.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 4 <= int(self.get_qty) <= 7 and self.combo_get == 'Logo sem fundo até 16cm':
            corresponding_value = 22.29
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 8 <= int(self.get_qty) <= 11 and self.combo_get == 'Logo sem fundo até 16cm':
            corresponding_value = 14.18
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) >= 12 and self.combo_get == 'Logo sem fundo até 16cm':
            corresponding_value = 13.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) == 1 and self.combo_get == 'Logo com fundo até 8cm':
            corresponding_value = 180.00
            description = 'Personalizando 1 item,\nadiciona:'

        elif 2 <= int(self.get_qty) <= 3 and self.combo_get == 'Logo com fundo até 8cm':
            corresponding_value = 60.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 4 <= int(self.get_qty) <= 7 and self.combo_get == 'Logo com fundo até 8cm':
            corresponding_value = 25.71
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 8 <= int(self.get_qty) <= 11 and self.combo_get == 'Logo com fundo até 8cm':
            corresponding_value = 16.36
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) >= 12 and self.combo_get == 'Logo com fundo até 8cm':
            corresponding_value = 15.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) == 1 and self.combo_get == 'Logo com fundo até 16cm':
            corresponding_value = 240.00
            description = 'Personalizando 1 item,\nadiciona:'

        elif 2 <= int(self.get_qty) <= 3 and self.combo_get == 'Logo com fundo até 16cm':
            corresponding_value = 80.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 4 <= int(self.get_qty) <= 7 and self.combo_get == 'Logo com fundo até 16cm':
            corresponding_value = 34.29
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif 8 <= int(self.get_qty) <= 11 and self.combo_get == 'Logo com fundo até 16cm':
            corresponding_value = 21.82
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        elif int(self.get_qty) >= 12 and self.combo_get == 'Logo com fundo até 16cm':
            corresponding_value = 20.00
            description = f'Personalizando {self.get_qty} itens,\nadiciona:'

        self.label_result_text_area.configure(
            text=f'{description} R${corresponding_value:.2f}\nalém do valor da peça.', bg='#b82323')

        self.clear()
        self.entry_qty.focus()

    def clear(self):
        self.entry_qty.delete(0, END)


if __name__ == '__main__':
    Embroidery().embroidery_calculator()
