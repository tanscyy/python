from tkinter import *
import _sqlite3
from rich.console import Console

root = Tk()
root.title('CompuServ Belize')
root.geometry("400x300")
root.configure(background='Grey')

console = Console()
conn = _sqlite3.connect('Compdata.db')
c = conn.cursor()
C = c.execute("""CREATE TABLE IF NOT EXISTS users( Computers TEXT, Accessories Text, Cables TEXT, Memory TEXT, Storage TEXT, Printerandsupplies TEXT, Quantity NUMERIC, Price NUMERIC )""")
conn.commit()
conn.close()

Computers = Entry(root, width=30)
Computers.grid(row=1, column=1)


Accessories = Entry(root, width=30)
Accessories.grid(row=2, column=1)
