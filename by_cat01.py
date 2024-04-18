import tkinter as tk
from tkinter import ttk

def show_children():
    children = tree.get_children()
    for child in children:
        print("Child:", child, "with text:", tree.item(child)["text"])

root = tk.Tk()

tree = ttk.Treeview(root)
tree.pack()

# Добавление узлов
tree.insert('', 'end', 'item1', text='Элемент 1')
tree.insert('', 'end', 'item2', text='Элемент 2')
tree.insert('item1', 'end', 'subitem1', text='Дочерний элемент 1.1')

button = tk.Button(root, text="Показать детей корневого уровня", command=show_children)
button.pack()

root.mainloop()