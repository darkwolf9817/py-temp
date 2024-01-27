import tkinter as tk

# The function to run the conversion
def convert():
    try:
        in_temp = float(in_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                out_temp = (in_temp * 9/5) + 32
            elif to_unit == "Kelvin":
                out_temp = in_temp + 273.15
            else: # A default case for if the user for some reason has Celsius for both the from and to temps
                out_temp = in_temp
        elif from_unit =="Fahrenheit":
            if to_unit == "Celsius":
                out_temp = (in_temp - 32) * 5/9
            elif to_unit == "Kelvin":
                out_temp = (in_temp - 32) * 5/9 +273.15
            else: # Once again, to handle same unit inputs
                out_temp = in_temp
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                out_temp = in_temp - 273.15
            elif to_unit == "Fahrenheit":
                out_temp = (in_temp - 273.15) * 9/5 + 32
            else: # You get the drill
                out_temp = in_temp
        out_label.config(text=f"{out_temp:.2f} {to_unit}")
    except ValueError:
        out_label.config(text="Invalid input")
        
# Creating the window
root = tk.Tk()
root.title("Temp Converter")
root.geometry("480 x 640")

# Input temperature
in_label = tk.Label(root, text="Enter Temperature: ").pack()
in_entry = tk.Entry(root).pack()

# From unit combobox
from_unit_var = tk.StringVar(root)
from_unit_var.set("Celsius") # Default value
from_unit_ops = ["Celsius", "Fahrenheit", "Kelvin"]
from_menu = tk.OptionMenu(root, from_unit_var, *from_unit_ops).pack()

# To unit combobox
to_unit_var = tk.StringVar(root)
to_unit_var.set("Celsius") # Default value
to_unit_ops = ["Celsius", "Fahrenheit", "Kelvin"]
tomenu = tk.OptionMenu(root, to_unit_var, *to_unit_ops).pack()

# Convert button
convert_btn = tk.Button(root, text="Convert", command=convert).pack()

# Output
out_label = tk.Label(root, text="").pack()

root.mainloop()