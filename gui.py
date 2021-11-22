import tkinter as tk


window = tk.Tk()
window.geometry("700x600")
window.title("Done Interface")
font_specs = ('ubuntu', 13)

def setting():
    window_setting = tk.Tk()
    window_setting.geometry("500x500")
    window_setting.title("Setting")
    window_setting.resizable(False, False)

def flame_sensor():
    window_sensor = tk.Tk()
    window_sensor.geometry("700x600")
    window_sensor.title("Flame Sensor")

def temperature_humidity_sensor():
    window_sensor = tk.Tk()
    window_sensor.geometry("700x600")
    window_sensor.title("Temperature and Humidity Sensor")

def connection():
    text = "Connection Successful"
    text_output = tk.Label(window, text = text)
    text_output.grid(row=0, column=1)

def gas_sensor():
    window_sensor = tk.Tk()
    window_sensor.geometry("700x600")
    window_sensor.title("Gas Sensor")

def vibration_sensor():
    window_sensor = tk.Tk()
    window_sensor.geometry("700x600")
    window_sensor.title("Vibration Sensor")

def pressure_temperature_sensor():
    window_sensor = tk.Tk()
    window_sensor.geometry("700x600")
    window_sensor.title("Pressure and Temperature Sensor")

menubar = tk.Menu(window, font=font_specs, bd=1, bg="grey")
window.config(menu=menubar)

file_save = tk.Menu(menubar, font=font_specs, tearoff=0)
file_save.add_command(label="Save")
file_save.add_command(label="New window")
file_save.add_command(label="Close window")
file_save.add_command(label="Setting", command=setting)
sensor_set = tk.Menu(menubar, font=font_specs, tearoff=0)
sensor_set.add_command(label="flame sensor")
sensor_set.add_command(label="Temperature and Humidity senor")
sensor_set.add_command(label="Gas sensor")
sensor_set.add_command(label="Vibration sensor")
sensor_set.add_command(label="Pressure and temperature sensor")


menubar.add_cascade(label="File", menu=file_save)
menubar.add_cascade(label="Sensor", menu=sensor_set)


if __name__ == "__main__":
    window.mainloop()
