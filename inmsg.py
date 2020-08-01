import tkinter as tk

def insert():
    
    head = tk.Tk()
    head.title("Secret Message")
    head.geometry("300x130")

    msg = tk.Text(head, height=5, width=10)
    msg.pack(side=tk.TOP, fill = tk.X)

    
    def retrieve():
        
        global string
        string = msg.get(1.0, tk.END).strip()
        
        head.destroy()
        
    button = tk.Button(head, text="OK", command = retrieve).pack(side=tk.TOP)

    
    head.mainloop()
    return string

def displaymsg(sec_msg):
    head = tk.Tk()
    head.title("Secret Message")
    head.geometry("300x50")

    text = tk.Label(head, text=sec_msg)
    text.pack(fill = tk.BOTH, anchor="w")
