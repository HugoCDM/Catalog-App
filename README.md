# Catalog App 2025
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p> A Tkinter-based application developed for a uniform company that displays its catalog and make it available for getting a quote by calculating the items.</p>




## 📥 Installation
1. Clone the repository and navigate into the directory
   ```bash
   git clone https://github.com/HugoCDM/Catalog-App.git
   cd Catalog-App
   ```
2. Create and activate a virtual environment(optional)
   ```bash
   python -m venv venv 
   .\venv\Scripts\activate 
   ```
   
If you have trouble with .\venv\Scripts\activate, run Windows PowerShell on your search bar as an administrator and write:
```bash
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser # Then type Y and press Enter. Go to step 2
```
## 🖱 Usage
### 1. Produto's entry
- A entry where you can search for a uniform available in its catalog.
- Whevener you type, the corresponding uniforms with these words are displayed.

### 2. Checkboxes
- Calculadora Bordado: Opens an embroidery calculator app embedded in its catalog.
- Calculadora: Once you click on the checkbox, the frame is split and a calculator is displayed.
- Sizes: It just shows when you check Calculadora checkbox and choose an item by pressing Enter.

### 3. Simpledialog Section
- Silk or Embroidery: If you want to customize your uniforms(optional) you can enter the cost of each. Otherwise, just close the window.
- Quantity: Enter the quantity of items.

### 4. Keyboard keys and mouse
- ⌨️ Arrows: Navigate through the list 
- 🖰 Left-Mouse: Navigate through the list 
- ↵  Enter: Select an item
- ![icons8-computer-mouse-20](https://github.com/user-attachments/assets/ca356564-807a-40a4-9acd-4ab099b16935) Double-click: Delete an item on the Treeview


## ƒ Functions
### list_selected_item(size, var)
- 2 parameters:
    - <b>size</b>: the item corresponding description(e.g. Pack of 25 units)
    - <b>var</b>: a variable where the item descriptions are shown
- The item selected from the list either by clicking with the mouse or with the keyboard arrows, activates the ACTIVE constant.

### calculator(event)
- Get your list selected item.
- Get the size to create variables
- Checkbuttons are created depending on the item size description

### show_qty_value()
- Displays quantity and value on labels
- A clear button is displayed on top for deleting all items

### add_or_update()
- Add an item if not exists in the list(Treeview)
- Update the item, quantity and value if already exists in the list(Treeview)

### update()
- Fills the Treeview with the items from the catalog

### fillout()
- Fills the tk_label_price with the selected item description of the list

### check()
- Displays the corresponding items with the words you type
- Updates the Treeview calling the update() function

### show_calculator()
- Splits the screen to show the calculator
- The Treeview is built
- Double-clicking on the selected item of the list deletes it automatically

### close_windows()
- Ensure all windows are closed when clicking the X on the main window



## 🌅 Image section
![catalog](https://github.com/user-attachments/assets/82d8d556-dd37-4d38-b163-2463612a9375)
![catalog_calculator](https://github.com/user-attachments/assets/f67da28c-f19d-4518-9319-c738613ad353)
![catalog_embroidery](https://github.com/user-attachments/assets/798bacf7-8c7e-4b39-9136-0bbba379f56e)
![catalog_camisa](https://github.com/user-attachments/assets/3c2b05c9-0fc8-48f4-8a55-b7650244b130)
![catalog_camisa_silkorembroidery](https://github.com/user-attachments/assets/3b3b9049-ecb4-4d9e-8097-1856e7eab9f7)
![catalog_camisa_qty](https://github.com/user-attachments/assets/b4c51f88-de41-475b-93e9-584acd434527)
![catalog_selected_camisa_calculator](https://github.com/user-attachments/assets/640bb1c8-735b-4dc0-ad95-a656d4d736ab)
![catalog_selected_camisa_colete_calculator](https://github.com/user-attachments/assets/a3563564-d9d8-4071-97a3-e946a530a4fd)



### *Made by [Hugo Mello](https://github.com/HugoCDM)*








