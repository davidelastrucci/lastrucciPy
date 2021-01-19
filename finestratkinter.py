import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("tkinter")
window.configure(background="black")

def first_print():
    text = "ciao"
    text_output = tk.Label(window, text=text, fg="green", font=("Merriweather"))
    text_output.grid(row=0, column=1)


def second_function():
    text = "ciao 2.0"
    text_output = tk.Label(window, text=text, fg="purple", font=("Merriweather"))
    text_output.grid(row=1, column=1)


first_button = tk.Button(text="prima funzione", command= first_print)
first_button.grid(row=0, column=0)

second_button = tk.Button(text="seconda funzione", command= second_function)
second_button.grid(row=1, column=0, pady="20")

window.mainloop()