import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

flame_connection = False
temperature_humidity_connection = False
gas_connection = False
vibration_connection = False
pressure_temperature_connection = False


window = tk.Tk()
window.geometry("700x600")
window.title("Done Interface")
font_specs = ('ubuntu', 11)

def setting():
    window_setting = tk.Tk()
    window_setting.geometry("500x500")
    window_setting.title("Setting")
    window_setting.resizable(False, False)

def flame_sensor():
    if  flame_connection == True:
        window_sensor = tk.Tk()
        window_sensor.geometry("700x600")
        window_sensor.title("Flame Sensor")
    else:
        messagebox.showerror("Connection error", "Try to verify that the sensor is mounted correctly" )
         


def temperature_humidity_sensor():
    if temperature_humidity_connection == True:
        window_sensor = tk.Tk()
        window_sensor.geometry("700x600")
        window_sensor.title("Temperature and Humidity Sensor")
    else:
        messagebox.showerror("Connection error", "Try to verify that the sensor is mounted correctly" )


def connection():
    text = "Connection Successful"
    text_output = tk.Label(window, text = text)
    text_output.grid(row=0, column=1)

def gas_sensor():
    if gas_connection == True:
        window_sensor = tk.Tk()
        window_sensor.geometry("700x600")
        window_sensor.title("Gas Sensor")
    else:
        messagebox.showerror("Connection error", "Try to verify that the sensor is mounted correctly" )

def vibration_sensor():
    if vibration_connection == True:
        window_sensor = tk.Tk()
        window_sensor.geometry("700x600")
        window_sensor.title("Vibration Sensor")
    else:
        messagebox.showerror("Connection error", "Try to verify that the sensor is mounted correctly" )

def pressure_temperature_sensor():
    if pressure_temperature_connection == True:
        window_sensor = tk.Tk()
        window_sensor.geometry("700x600")
        window_sensor.title("Pressure and Temperature Sensor")
    else:
        messagebox.showerror("Connection error", "Try to verify that the sensor is mounted correctly" )

def onSave():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))

menubar = tk.Menu(window, font=font_specs, bd=1, bg="grey")
window.config(menu=menubar)

file_save = tk.Menu(menubar, font=font_specs, tearoff=0)
file_save.add_command(label="Save", command=onSave)
file_save.add_command(label="New window")
file_save.add_command(label="Close window", command=window.quit)
file_save.add_command(label="Setting", command=setting)
sensor_set = tk.Menu(menubar, font=font_specs, tearoff=0)
sensor_set.add_command(label="flame sensor", command=flame_sensor)
sensor_set.add_command(label="Temperature and Humidity senor", command= temperature_humidity_sensor)
sensor_set.add_command(label="Gas sensor", command=gas_sensor)
sensor_set.add_command(label="Vibration sensor", command=vibration_sensor)
sensor_set.add_command(label="Pressure and temperature sensor", command=pressure_temperature_sensor)


menubar.add_cascade(label="File", menu=file_save)
menubar.add_cascade(label="Sensor", menu=sensor_set)

statusbar=tk.Label(window, text="Connection: online" , bd=1, relief=tk.SUNKEN, anchor=tk.W)

statusbar.pack(side=tk.BOTTOM, fill=tk.X)

if __name__ == "__main__":
    window.mainloop()
