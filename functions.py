from tkinter import ACTIVE, END, simpledialog, Label, IntVar, Checkbutton, Frame, Button, ttk
from embroidery_app import Embroidery


class Functions(Embroidery):
    def list_selected_item(self, size, var):

        # The item selected from the list either by clicking with the mouse or with the keyboard arrows, activating the ACTIVE constant
        selected_item = self.tk_list.get(ACTIVE)

        if var.get() == 1:

            qty = simpledialog.askinteger(
                'Quantidade', 'Digite a quantidade: ', minvalue=1)
            try:
                chosen_price = uniforms[selected_item][size]
            except:
                chosen_price = uniforms[selected_item][0]

            if self.price_silk_embroidery:
                new_value = float(
                    (chosen_price + self.price_silk_embroidery) * qty)
                new_item = selected_item + ' - ' + \
                    size + '(personalizado)'
            else:
                new_value = chosen_price * qty
                new_item = selected_item + ' - ' + size

            self.add_or_update(qty, new_item, new_value)

            self.show_qty_value()

    def calculator(self, event):

        # Remove label_sizes if exists when pressing Enter
        if hasattr(self, 'label_sizes'):
            self.label_sizes.destroy()

        self.label_sizes = Label(
            self.frame_white_bottom, bg='white', width=150, height=80)
        self.label_sizes.place(relx=0.755, rely=0.0062)

        # After 60s the label is destroyed after showing up the sizes
        self.label_sizes.after(60000, lambda: self.label_sizes.destroy())

        # 1 - Get your list selected item
        selected_item = self.tk_list.get(ACTIVE)

        # 2 - Getting the size to create variables
        size = len(uniforms[selected_item])

        self.price_silk_embroidery = simpledialog.askinteger(
            'Quantidade', 'Digite o valor do silk/bordado: ', minvalue=4)

        self.var1 = IntVar(self.label_sizes, 550)
        self.var2 = IntVar(self.label_sizes, 550)
        self.var3 = IntVar(self.label_sizes, 550)

        if size == 1:
            checkbutton1 = Checkbutton(
                self.label_sizes, text='Tamanho único', variable=self.var1, command=lambda: self.list_selected_item('Tamanho único', self.var1)).pack()

        if size == 2:
            if 'Pacote C/ 25' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Pacote C/ 25', variable=self.var1, command=lambda: self.list_selected_item('Pacote C/ 25', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='Pacote C/ 50', variable=self.var2, command=lambda: self.list_selected_item('Pacote C/ 50', self.var2)).pack()

            elif 'Pacote C/ 100' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Unidade', variable=self.var1, command=lambda: self.list_selected_item('Unidade', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='Pacote C/ 100', variable=self.var2, command=lambda: self.list_selected_item('Pacote C/ 100', self.var2)).pack()

            elif 'Pacote C/ 10' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Unidade', variable=self.var1, command=lambda: self.list_selected_item('Unidade', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='Pacote C/ 10', variable=self.var2, command=lambda: self.list_selected_item('Pacote C/ 10', self.var2)).pack()

            elif 'Pacote C/ 3' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Par', variable=self.var1, command=lambda: self.list_selected_item('Par', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='Pacote C/ 3', variable=self.var2, command=lambda: self.list_selected_item('Pacote C/ 3', self.var2)).pack()

        if size == 3:
            if 'Acima do nº 54' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Até nº 50', variable=self.var1, command=lambda: self.list_selected_item('Até nº 50', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='52 e 54', variable=self.var2, command=lambda: self.list_selected_item('52 e 54', self.var2)).pack()

            elif 'Acima do XG' in uniforms[selected_item].keys() and '+20%' in uniforms[selected_item].values():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='P ao GG', variable=self.var1, command=lambda: self.list_selected_item('P ao GG', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='XG', variable=self.var2, command=lambda: self.list_selected_item('XG', self.var2)).pack()

            elif 'Consultar' in uniforms[selected_item].values():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='P ao GG', variable=self.var1, command=lambda: self.list_selected_item('P ao GG', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='XG', variable=self.var2, command=lambda: self.list_selected_item('XG', self.var2)).pack()

            elif 'P ao GG' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='P ao GG', variable=self.var1, command=lambda: self.list_selected_item('P ao GG', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='XG', variable=self.var2, command=lambda: self.list_selected_item('XG', self.var2)).pack()
                checkbutton3 = Checkbutton(
                    self.label_sizes, text='XGG', variable=self.var3, command=lambda: self.list_selected_item('XGG', self.var3)).pack()

            elif 'Acima do XG' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='P ao GG', variable=self.var1, command=lambda: self.list_selected_item('P ao GG', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='XG', variable=self.var2, command=lambda: self.list_selected_item('XG', self.var2)).pack()
                checkbutton3 = Checkbutton(
                    self.label_sizes, text='Acima do XG', variable=self.var3, command=lambda: self.list_selected_item('Acima do XG', self.var3)).pack()

            elif 'Até nº 50' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Até nº 50', variable=self.var1, command=lambda: self.list_selected_item('Até nº 50', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='52 e 54', variable=self.var2, command=lambda: self.list_selected_item('52 e 54', self.var2)).pack()
                checkbutton3 = Checkbutton(
                    self.label_sizes, text='Acima do nº 54', variable=self.var3, command=lambda: self.list_selected_item('Acima do nº 54', self.var3)).pack()

            elif '10 unidades' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Par', variable=self.var1, command=lambda: self.list_selected_item('Par', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='10 unidades', variable=self.var2, command=lambda: self.list_selected_item('10 unidades', self.var2)).pack()
                checkbutton3 = Checkbutton(
                    self.label_sizes, text='50 unidades', variable=self.var3, command=lambda: self.list_selected_item('50 unidades', self.var3)).pack()

            elif 'Caixa C/ 10' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Unidade', variable=self.var1, command=lambda: self.list_selected_item('Unidade', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='Caixa C/ 10', variable=self.var2, command=lambda: self.list_selected_item('Caixa C/ 10', self.var2)).pack()
                checkbutton3 = Checkbutton(
                    self.label_sizes, text='Caixa C/ 50', variable=self.var3, command=lambda: self.list_selected_item('Caixa C/ 50', self.var3)).pack()

            elif 'Até nº 5(GG)' in uniforms[selected_item].keys():
                checkbutton1 = Checkbutton(
                    self.label_sizes, text='Até nº 5(GG)', variable=self.var1, command=lambda: self.list_selected_item('Até nº 5(GG)', self.var1)).pack()
                checkbutton2 = Checkbutton(
                    self.label_sizes, text='Nº 6(XG)', variable=self.var2, command=lambda: self.list_selected_item('Nº 6(XG)', self.var2)).pack()
                checkbutton3 = Checkbutton(
                    self.label_sizes, text='Nº 7(XGG)', variable=self.var3, command=lambda: self.list_selected_item('Nº 7(XGG)', self.var3)).pack()

    def show_qty_value(self):

        # Calculate total quantity and price
        self.new_total = 0
        self.new_qty = 0

        for child in self.listClick.get_children():
            total = float(self.listClick.item(child, 'values')[2])  # Preço
            qtty = int(self.listClick.item(child, 'values')[0])  # Qtd

            self.new_total += total
            self.new_qty += qtty

        if hasattr(self, 'label_value'):
            self.label_value.destroy()

        if hasattr(self, 'label_qty'):
            self.label_qty.destroy()

        self.label_value = Label(self.frame_white_bottom,
                                 text=f'Total: R${self.new_total:.2f}', fg='white', bg='#b82323', font=('Helvetica', 13, 'bold'))
        self.label_value.place(relx=0.017, rely=0.15)

        self.label_qty = Label(self.frame_white_bottom,
                               text=f'Itens: {self.new_qty}', fg='white', bg='#b82323', font=('Helvetica', 13, 'bold'))
        self.label_qty.place(relx=0.017, rely=0.55)

        self.btn_clear = Button(self.frame_new_top_white_bar, text='Limpar', bg='#b82323', fg='white', relief='flat', font=(
            'Futura', 10, 'bold'), command=self.delete_values)
        self.btn_clear.place(relx=0.935, rely=0.53, anchor='center')

    def add_or_update(self, qty, new_item, new_value):
        updated_item = False

        for child in self.listClick.get_children():
            item_treeview = self.listClick.item(child, 'values')[1]

            # If you have the same item chosen
            if item_treeview == new_item:

                # Updates Qtd and Valor
                current_qty = int(self.listClick.item(child, 'values')[0])
                current_price = float(self.listClick.item(child, 'values')[2])

                nova_qty = current_qty + qty
                novo_preco = current_price + new_value

                self.listClick.item(child, values=(
                    nova_qty, new_item, f"{novo_preco:.2f}"))

                updated_item = True
                break

        if not updated_item:
            # Insert the item if it doesn't not already exist in the Treeview
            self.listClick.insert('', END, values=(
                qty, new_item, f"{new_value:.2f}"))

    def delete_value_from_list(self, event=None):

        selected_item_list = self.listClick.selection()
        selected_qty = int(self.listClick.item(
            selected_item_list, 'values')[0])
        selected_price = float(self.listClick.item(
            selected_item_list, 'values')[2])

        for child in selected_item_list:
            self.listClick.delete(child)

        self.new_qty = self.new_qty - selected_qty
        self.new_total = self.new_total - selected_price

        self.label_qty.configure(text=f'Itens: {self.new_qty}')
        self.label_value.configure(text=f'Total: R${self.new_total:.2f} ')

    def delete_values(self):
        for child in self.listClick.get_children():
            self.listClick.delete(child)
            self.label_value.configure(text='Total: R$0.00')
            self.label_qty.configure(text='Item: 0')

    def embroidery_screen(self):
        if self.var_embroidery_calculator.get() == 1:
            Embroidery.embroidery_calculator(self)
        else:
            self.window.destroy()

    def update(self, dictionary):

        # Clear List
        self.tk_list.delete(0, END)

        for key in dictionary:
            self.tk_list.insert(END, key)

    def fillout(self, event=None):

        if hasattr(self, 'tk_label_price'):
            self.tk_label_price.destroy()

        self.tk_entry.delete(0, END)

        self.tk_entry.insert(0, self.tk_list.get(ACTIVE))

        selected_item = self.tk_list.get(ACTIVE)

        prices = uniforms.get(selected_item, [])

        # If the price's value is a dictionary or a list we can handle that
        if isinstance(prices, dict):
            try:
                # For the dictionary formats as "Key: Value"
                formatted_prices = "\n".join(
                    [f"{key}: R$ {value:.2f}" for key, value in prices.items()])
            except:
                formatted_prices = "\n".join(
                    [f"{key}: R$ {value}" for key, value in prices.items()])

        else:
            # To unique values
            formatted_prices = f'R$ {uniforms[selected_item][0]:.2f}'

        self.tk_label_price = Label(
            self.frame_white_bottom_bar, font=('Verdana', 12, 'bold'), text=f'{formatted_prices}', bg='#dcdfe3', fg='#b82323', border=5)
        self.tk_label_price.place(relx=0.011, rely=0.093)

        self.tk_label_price.after(
            120000, lambda: self.tk_label_price.configure(text='', bg='white'))

    def check(self, event):
        self.typed = self.tk_entry.get()
        if self.typed == '':
            self.data = uniforms
        else:
            self.data = []
            for key in uniforms.keys():
                if self.typed.lower() in key.lower():
                    self.data.append(key)

        self.update(self.data)

    def show_calculator(self):

        if self.var.get() == 1:

            self.label_infos.configure(width=620)
            self.frame_white_bottom_bar.configure(width=600)
            self.tk_list.configure(width=53)
            self.frame_red_outline.configure(width=600)

            self.frame_white_bottom = Frame(bg='white', width=546, height=80)
            self.frame_white_bottom.place(relx=0.525, rely=0.843)

            self.label_sizes = Label(self.frame_white_bottom, bg='white',
                                     width=150, height=180, font=('Helvetica', 20))
            self.label_sizes.place(relx=0.755, rely=0.0062)

            self.frame_outline = Frame(bg='#871010', width=546, height=460)
            self.frame_outline.place(relx=0.525, rely=0.135)

            self.frame_black_top_bar.configure(width=600)
            self.frame_new_top_white_bar = Frame(
                bg='white', width=546, height=40)
            self.frame_new_top_white_bar.place(relx=0.525, rely=0.135)

            self.label_new_calculator = Label(
                self.frame_new_top_white_bar, text='Calculadora', bg='white', fg='#b82323', font=('Futura', 20, 'bold'))
            self.label_new_calculator.place(relx=0.525, rely=0.5, anchor='c')

            self.style = ttk.Style()
            self.style.configure('Treeview', font=('Helvetica', 12))
            self.listClick = ttk.Treeview(
                self.frame_outline, height=3, column=('col1', 'col2', 'col3'), show='headings')
            self.listClick.heading("#1", text='Qtd')
            self.listClick.heading("#2", text='Produto')
            self.listClick.heading("#3", text='Preço')

            self.listClick.column("#1", width=1, anchor='center')
            self.listClick.column("#2", width=360, anchor='center')
            self.listClick.column("#3", width=20, anchor='center')
            self.listClick.place(relx=0.015, rely=0.107,
                                 relwidth=0.966, relheight=0.871)

            # Double-clicking on the list deletes the selected item automatically
            self.listClick.bind('<Double-Button-1>',
                                self.delete_value_from_list)

        else:
            self.frame_outline.destroy()
            self.frame_new_top_white_bar.destroy()
            self.frame_white_bottom.destroy()

            self.label_infos.configure(width=1152)
            self.frame_white_bottom_bar.configure(width=1152)
            self.tk_list.configure(width=103)
            self.frame_red_outline.configure(width=1152)
            self.frame_black_top_bar.configure(width=1152)


uniforms = {
    'Jaleco Oxford Manga Longa': {'P ao GG': 76.00, 'XG': 86.00, 'XGG': 129.00},

    'Jaleco Brim Fechado Manga Curta Branco ': {'P ao GG': 60.00, 'XG': 65.00, 'XGG': 95.00},

    'Jaleco Fechado Brim Manga Curta Cor ': {'P ao GG': 65.00, 'XG': 70.00, 'XGG': 104.00},

    'Jaleco G. Padre/Esporte Brim Manga Curta Branco ': {'P ao GG': 70.00, 'XG': 75.00, 'XGG': 115.00},

    'Jaleco G. Padre/Esporte Manga Curta Cor Brim': {'P ao GG': 75.00, 'XG': 80.00, 'XGG': 115.00},

    'Jaleco Feminino C/Viés ou Renda Manga Curta Oxford': {'P ao GG': 80.00, 'XG': 86.00, 'XGG': 135.00},

    'Jaleco Longo Gabardine Zíper Manga Longa': {'P ao GG': 110.00, 'XG': 120.00, 'XGG': 140.00},

    'Camisa Malha Branco Algodão/PV/Poliéster': {'P ao GG': 30.00, 'XG': 35.00, 'XGG': 50.00},

    'Camisa Malha Cor Algodão/PV/Poliéster': {'P ao GG': 35.00, 'XG': 39.00, 'XGG': 50.00},

    'Camisa Malha Branco Premium Algodão': {'P ao GG': 40.00, 'XG': 45.00, 'XGG': 55.00},

    'Camisa Malha Cor Premium Algodão': {'P ao GG': 45.00, 'XG': 50.00, 'XGG': 60.00},

    'Camisa Polo Branco/Mescla Algodão/Dryfit': {'P ao GG': 50.00, 'XG': 55.00, 'XGG': 68.00},

    'Camisa Polo Cor Algodão/Dryfit': {'P ao GG': 55.00, 'XG': 60.00, 'XGG': 78.00},

    'Camisa UV Manga Longa': {'P ao GG': 60.00, 'XG': 65.00, 'XGG': 'Consultar'},

    'Camisa Social Manga Curta ou Manga Longa Masculino': {'Até nº 5(GG)': 110.00, 'Nº 6(XG)': 120.00, 'Nº 7(XGG)': 180.00},

    'Camisa Social Manga Curta/Manga Longa/Manga 3/4 Feminino': {'P ao GG': 110.00, 'XG': 120.00, 'XGG': 180.00},

    'Camisa social Manga Longa Branco Microfibra': {'Até nº 5(GG)': 90.00, 'Nº 6(XG)': 100.00, 'Nº 7(XGG)': 150.00},

    'Bermuda Brim Branco Elástico': {'P ao GG': 60.00, 'XG': 65.00, 'XGG': 95.00},

    'Bermuda Cor Elástico Brim': {'P ao GG': 65.00, 'XG': 70.00, 'XGG': 110.00},

    'Bermuda Elástico Oxford': {'P ao GG': 50.00, 'XG': 54.00, 'XGG': 85.00},

    'Calça Elástico Brim Branco': {'P ao GG': 70.00, 'XG': 75.00, 'XGG': 115.00},

    'Calça Brim Elástico Carijó ou Cor': {'P ao GG': 80.00, 'XG': 87.00, 'XGG': 135.00},

    'Calça Legging Plástico Branco ou Preta': {'P ao GG': 85.00, 'XG': 89.00, 'XGG': 141.00},

    'Calça Meio Cós Oxford': {'P ao GG': 75.00, 'XG': 78.00, 'XGG': 116.00},

    'Calça Elástico Oxford': {'P ao GG': 54.00, 'XG': 61.00, 'XGG': 92.00},

    'Calça Jeans Masculino ou Feminino': {'Até nº 50': 90.00, '52 e 54': 95.00, 'Acima do nº 54':  'Consultar'},

    'Calça Social Feminina Oxford': {'Até nº 50': 85.00, '52 e 54': 95.00, 'Acima do nº 54':  'Consultar'},

    'Calça Social Masculino Oxford': {'Até nº 50': 83.00, '52 e 54': 87.00, 'Acima do nº 54':  'Consultar'},

    'Jaqueta Chef Oxford Manga Curta/Longa': {'P ao GG': 100.00, 'XG': 110.00, 'XGG': 170.00},

    'Jaqueta Brim Branco Manga Curta': {'P ao GG': 100.00, 'XG': 110.00, 'XGG': 170.00},

    'Jaqueta Brim Branco Manga Longa': {'P ao GG': 110.00, 'XG': 120.00, 'XGG': 180.00},

    'Jaqueta Brim Cor Manga Curta': {'P ao GG': 120.00, 'XG': 130.00, 'XGG': 150.00},

    'Jaqueta Brim Cor Manga Longa': {'P ao GG': 130.00, 'XG': 140.00, 'XGG': 200.00},

    'Jaqueta Oxford Manga curta/ Manga longa': {'P ao GG': 100.00, 'XG': 110.00, 'XGG': 170.00},

    'Jaqueta Brim Bot Pressão/Embutido Manga Curta Sutache': {'P ao GG': 150.00, 'XG': 160.00, 'XGG': 250.00},

    'Jaqueta Brim Bot Pressão/Embutido Manga Longa Sutache': {'P ao GG': 170.00, 'XG': 180.00, 'XGG': 260.00},

    'Jaqueta Jeans Botão Pressão Manga Curta': {'P ao GG': 170.00, 'XG': 175.00, 'XGG': 250.00},

    'Jaqueta Jeans Botão Pressão Manga Longa': {'P ao GG': 180.00, 'XG': 185.00, 'XGG': 260.00},

    'Blazer Feminino/Masculino': {'P ao GG': 220.00, 'XG': 230.00, 'XGG': 'Consultar'},

    'Conjunto Blazer Feminino/Masculino': {'P ao GG': 290.00, 'XG': 300.00, 'XGG': 'Consultar'},

    'Casaco Forrado Oxford Preto': {'P ao GG': 190.00, 'XG': 210.00, 'XGG': 'Consultar'},

    'Casaco Moletom(Preto e Cinza Mescla)': {'P ao GG': 100.00, 'XG': 110.00, 'XGG': 'Consultar'},

    'Jaqueta Frigorífica Azul Marinho(G/GG)': [250.00],

    'Avental Peito Napa Branco/Cor 100cm x 70cm Curto': [25.00],

    'Avental Peito Napa Branco/Cor 120cm x 70cm Longo': [28.00],

    'Avental Peito Napa Branco/Cor 100cm x 70cm Curto Verniz': [30.00],

    'Avental Peito Napa Branco/Cor 120cm x 70cm Longo Verniz': [35.00],

    'Avental Peito Retardante a Chamas C/ Bolso': [45.00],

    'Avental Peito Repelente a Água e Óleo C/ Bolso': [45.00],

    'Avental Peito/Cintura Brim Branco': [30.00],

    'Avental Peito de Lona Artesanal': [150.00],

    'Avental Peito Courino C/ Det Ouro Velho': [80.00],

    'Avental Peito/Cintura Transpassado Brim Branco com ou sem Pala': [45.00],

    'Avental Peito/Cintura Carijó/Cor Brim': [35.00],

    'Avental Peito/Cintura Carijó/Cor Transpassado Brim': [50.00],

    'Avental Peito/Cintura Jeans C/ Det Couro C/ Bolso': [61.00],

    'Avental Peito/Cintura Couro C/ Det Couro C/ Bolso': [80.00],

    'Avental Peito/Cintura Jeans ou Lona': [50.00],

    'Avental Peito/Cintura Oxford': [30.00],

    'Avental Peito/Cintura Transpassado Oxford': [35.00],

    'Avental Peito Lona C/ Det Couro': [70.00],

    'Avental Peito Silicone 120cm x 70cm': [25.00],

    'Avental Peito Descartável': [20.00],

    'Avental Camareira': [25.00],

    'Avental Camareira C/ Renda': [40.00],

    'Avental Colete Oxford': [40.00],

    'Avental Colete Oxford Transpassado': [50.00],

    'Pochete': [30.00],

    'Pochete Jeans': [32.00],

    'Colete Garçom Brim/Oxford': {
        'P ao GG': 60.00,
        'XG': 54.00,
        'Acima do XG': '+20%'
    },

    'Bota Branco/Preto Cano Curto(18cm)': [65.00],

    'Bota Branco/Preto Cano Longo(28cm)': [75.00],

    'Bota C/ Cadarço Nobuck': [140.00],

    'Botina Elástico Solado de Borracha Mondensidade': [85.00],

    'Botina Elástico Solado de PU Bidensidade': [95.00],

    'Sapato/Tênis Antiderrapante Preto/Branco': [110.00],

    'Sapato Social Feminino': [90.00],

    'Sapato Social Masculino': [110.00],

    'Bandana fechada': [25.00],

    'Bandana Lenço': [20.00],

    'Bibico Brim': [15.00],

    'Boné Americano': [35.00],

    'Boné Árabe': [35.00],

    'Boné Brim': [25.00],

    'Boina Lona': [60.00],

    'Chapelão Brim Branco ou C/ Det Xadrez': [30.00],

    'Faixa Estilizada Cabelo': [60.00],

    'Luva Chefe Preta': {
        'Par': 5.00,
        '10 unidades': 20.00,
        '50 unidades': 60.00
    },

    'Gorro Preto': [25.00],

    'Chapelão Descartável (M/G)': {
        'Pacote C/ 25': 130.00,
        'Pacote C/ 50': 230.00
    },

    'Coque C/ Laço': [20.00],

    'Rede para Cabelo Branca ou Preta': {
        'Unidade': 6.00,
        'Pacote C/ 100': 384.00
    },

    'Touca Brim Amarrar': [30.00],

    'Touca Descartável': [45.00],

    'Bata Oxford': [50.00],

    'Capa de Chuva Forrada Amarela': [50.00],

    'Capa de Chuva Forrada Transparente': [50.00],

    'Cinto preto': [30.00],

    'Fundo de Copo': {
        'Unidade': 3.00,
        'Pacote C/ 10': 25.00
    },

    'Gravata Borboleta': [15.00],

    'Gravata Laço Feminino': [25.00],

    'Gravata Laço Pronto': [30.00],

    'Happi': [80.00],

    'Lenço Feminino': [26.00],

    'Luva Alta Temperatura': [70.00],

    'Luva do Chef Latex Reutilizável M ou G': {
        'Unidade': 5.00,
        'Caixa C/ 10': 20.00,
        'Caixa C/ 50': 60.00
    },

    'Luva Latex Silver(Par)': [7.00],

    'Meias Sociais Pretas': {
        'Par': 25.00,
        'Pacote C/ 3': 68.00
    },

    'Meias Algodão Branca': {
        'Par': 25.00,
        'Pacote C/ 3': 68.00
    },

    'Pano P/ Vinho 50cm x 50cm Branco/Vinho': [15.00],

    'Toalha Jaqcard 1.40x1.40': [49.00],

    'Toalha Jaqcard 2.80x2.80': [190.00],

    'Toalha de Juta 1.50x1.50': [66.00],

    'Toalha Oxford 1.30x1.30(Xadrez/Estampado)': [45.00],

    'Toalha Oxford 1.50x1.50(Xadrez/Estampado)': [52.00],

    'Toalha Oxford 1.50x2.00(Xadrez/Estampado)': [70.00],

    'Toalha Brim 1.30x1.30': [57.00],

    'Toalha Brim 1.50x1.50': [66.00],

    'Toalho Brim 1.60x1.60': [70.00],

    'Toalha Brim 1.60x2.00': [88.00],

    'Toalha Oxford 1.30x1.30': [32.00],

    'Toalha Oxford 1.50x1.50': [37.00],

    'Toalha Oxford 2.00x2.00': [80.00],

    'Toalha Oxford 3.00x3.00': [120.00],

    'Toalha Panamá Gold 1.30x1.30': [42.00],

    'Toalha Panamá Gold 1.50x1.50': [49.00],

    'Toalha Panamá Gold 2.00x2.00': [130.00],

    'Toalha Panamá Gold 3.00x3.00': [195.00],

    'Cobremancha Oxford 0.75x0.75(Xadrez/Estampado)': [13.00],

    'Cobremancha Oxford 1.00x1.00(Xadrez/Estampado)': [30.00],

    'Cobremancha Oxford 1.00x1.20(Xadrez/Estampado)': [40.00],

    'Cobremancha Brim 0.80x0.80': [18.00],

    'Cobremancha Brim 1.00x1.00': [40.00],

    'Cobremancha Brim 1.00x1.20': [50.00],

    'Cobremancha Oxford 0.75x0.75': [10.00],

    'Cobremancha Oxford 1.00x1.00': [20.00],

    'Cobremancha Oxford 0.75x1.20': [15.00],

    'Cobremancha Panamá Gold 0.75x0.75': [15.00],

    'Cobremancha Panamá Gold 1.00x1.00': [29.00],

    'Cobremancha 1.00x1.20': [35.00],

    'Guardanapo Jacquard Bainha Envelope 0.45x0.45': [11.00],

    'Guardanapo Oxford 0.50x0.50(Xadrez/Estampado)': [6.50],

    'Guardanapo Brim 0.40x0.40': [8.00],

    'Guardanapo Brim 0.50x0.50(ACABADO)': [13.00],

    'Guardanapo Brim Ponto Aju 0.45x0.45(ACABADO)': [18.00],

    'Guardanapo Brim Sarja Branco 0.40x0.40': [5.00],

    'Guardanapo Brim Sarja Branco 0.50x0.50': [6.00],

    'Guardanapo Oxford 0.40x0.40': [5.00],

    'Guardanapo Oxford 0.50x0.50': [6.00],

    'Guardanapo Panamá Gold 0.40x0.40': [9.00],

    'Guardanapo Panamá Gold 0.50x0.50': [11.00],

    'Guardanapo Panamá Gold 0.50x0.50(ACABADO)': [12.00],



}
