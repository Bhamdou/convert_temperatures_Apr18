import tkinter as tk

class TemperatureConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Temperature Converter")
        self.geometry("350x200")

        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self, text="Enter temperature:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.temperature_entry = tk.Entry(self)
        self.temperature_entry.grid(row=0, column=1, padx=10, pady=10)

        self.convert_to_celsius_button = tk.Button(self, text="Convert to Celsius", command=self.convert_to_celsius)
        self.convert_to_celsius_button.grid(row=1, column=0, padx=10, pady=10)

        self.convert_to_fahrenheit_button = tk.Button(self, text="Convert to Fahrenheit", command=self.convert_to_fahrenheit)
        self.convert_to_fahrenheit_button.grid(row=1, column=1, padx=10, pady=10)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=2, column=0, padx=10, pady=10)

        self.result_value = tk.StringVar()
        self.result_value.set("0.0")

        self.result_display = tk.Label(self, textvariable=self.result_value)
        self.result_display.grid(row=2, column=1, padx=10, pady=10)

    def convert_to_celsius(self):
        try:
            fahrenheit = float(self.temperature_entry.get())
            celsius = (fahrenheit - 32) * 5 / 9
            self.result_value.set(round(celsius, 2))
        except ValueError:
            self.result_value.set("Invalid input")

    def convert_to_fahrenheit(self):
        try:
            celsius = float(self.temperature_entry.get())
            fahrenheit = (celsius * 9 / 5) + 32
            self.result_value.set(round(fahrenheit, 2))
        except ValueError:
            self.result_value.set("Invalid input")

if __name__ == "__main__":
    app = TemperatureConverter()
    app.mainloop()
