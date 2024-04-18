# импорт модулей
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import sqlite3

def init_db():
    # Создать БД
    conn = sqlite3.connect('business_orders.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS orders (
     id INTEGER PRIMARY KEY, customer_name TEXT NOT NULL,
     order_details TEXT NOT NULL, status TEXT NOT NULL)''')

    conn.commit()
    conn.close()

def view_orders():
    # Отобразить данные из таблицы БД в таблице на экране
    for i in tree.get_children():
        tree.delete(i)
    conn = sqlite3.connect('business_orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def add_order():
    # Добавление заказа. Со статусом Новый.
    conn = sqlite3.connect('business_orders.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (customer_name, order_details, status) VALUES (?, ?, 'Новый')",
                (customer_name_entry.get(), order_details_entry.get()))
    conn.commit()
    conn.close()
    customer_name_entry.delete(0, tk.END)
    order_details_entry.delete(0, tk.END)
    view_orders()

def complete_order():
    selected_item = tree.selection()
    if selected_item:
        #order_id = tree.item()

        order_id = tree.item(selected_item[0])['values'][0]
        conn = sqlite3.connect('business_orders.db')
        cur = conn.cursor()
        cur.execute("UPDATE orders SET status='Завершен' WHERE id=?", (order_id,))
        conn.commit()
        conn.close()
        view_orders()
    else:
        messagebox.showwarning("Предупреждение", "Выберите заказ для завершения!")


# окно интерфейса
app = tk.Tk()
app.title("Система управления заказами")

# Надпись
tk.Label(app, text="Имя клиента").pack()

# Поле для ввода имени клиента
customer_name_entry = tk.Entry(app)
customer_name_entry.pack()

# Поля для деталей заказа
tk.Label(app, text="Детали заказа").pack()
order_details_entry = tk.Entry(app)
order_details_entry.pack()

# Кнопка для добавления данных в таблицу
add_button = tk.Button(app, text="Добавить заказ", command=add_order)
add_button.pack()

# Кнопка для завершения заказа
complete_button = tk.Button(app, text="Завершить заказ", command=complete_order)
complete_button.pack()

# Создать таблицу из колонок
columns = ("id", "customer_name", "order_details", "status")
tree = ttk.Treeview(app, columns=columns, show="headings")

# Вывод шапки таблицы
for column in columns:
    tree.heading(column, text=column)
    tree.pack()

app.mainloop()
init_db()
view_orders()
