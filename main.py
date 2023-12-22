import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())

    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        result_label.config(text=f"Vücut Kitle Endeksi: {bmi:.2f}")
    else:
        result_label.config(text="Geçersiz değerler")


window = tk.Tk()
window.title("BMI CALCULATOR")

height_label = tk.Label(window, text="Enter your height (cm):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Enter your weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
