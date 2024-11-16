import tkinter as tk
from tkinter import ttk, messagebox
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
from tkcalendar import Calendar

fake = Faker()

# Lista de los campos disponibles en el generador
fields = [
    "first_name", "last_name", "email", "address", "ssn", "date_of_birth", "gender", "street_address", "city", "state", 
    "postcode", "country", "latitude", "longitude", "phone_number", "job", "date", "time", "user_name", "password"
]

# Funciones para generar datos
def generate_number(range_):
    return random.randint(*range_)

def generate_string(pattern):
    if pattern == "first_name":
        return fake.first_name()
    elif pattern == "last_name":
        return fake.last_name()
    elif pattern == "email":
        return fake.email()
    elif pattern == "address":
        return fake.address()
    elif pattern == "ssn":
        return fake.ssn()
    elif pattern == "date_of_birth":
        return fake.date_of_birth().strftime("%Y-%m-%d")
    elif pattern == "gender":
        return fake.gender()
    elif pattern == "street_address":
        return fake.street_address()
    elif pattern == "city":
        return fake.city()
    elif pattern == "state":
        return fake.state()
    elif pattern == "postcode":
        return fake.postcode()
    elif pattern == "country":
        return fake.country()
    elif pattern == "latitude":
        return fake.latitude()
    elif pattern == "longitude":
        return fake.longitude()
    elif pattern == "phone_number":
        return fake.phone_number()
    elif pattern == "job":
        return fake.job()
    elif pattern == "date":
        return fake.date()
    elif pattern == "time":
        return fake.time()
    elif pattern == "user_name":
        return fake.user_name()
    elif pattern == "password":
        return fake.password()
    return fake.text()

# Función para generar fechas aleatorias dentro de un rango
def generate_date(range_):
    start, end = [datetime.strptime(date, "%Y-%m-%d") for date in range_]
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Función para generar datos según configuración del usuario
def generate_data(config, num_records):
    data = []
    for _ in range(num_records):
        row = {}
        for col in config:
            if col["type"] == "number":
                row[col["name"]] = generate_number(col["range"])
            elif col["type"] == "string":
                row[col["name"]] = generate_string(col["pattern"])
            elif col["type"] == "date":
                row[col["name"]] = generate_date(col["range"]).strftime("%Y-%m-%d")
        data.append(row)
    return data

# Guardar datos en archivo CSV
def save_to_csv(data, filename="data"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    messagebox.showinfo("Éxito", f"Datos guardados en {filename}")

# Crear la interfaz gráfica
class DataGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Datos Dummy")
        self.root.geometry("500x500")  # Aumentar el tamaño de la ventana
        self.root.resizable(True, True)  # Hacer la ventana redimensionable

        # Configuración general
        self.columns = []
        self.num_records = tk.IntVar(value=100)
        self.filename = tk.StringVar(value="data")  # Variable para el nombre del archivo

        # Interfaz principal
        self.setup_ui()

    def setup_ui(self):
        # Título de la aplicación
        tk.Label(self.root, text="Generador de Datos Dummy", font=("Arial", 16), pady=20).grid(row=0, column=0, columnspan=2)

        # Número de registros
        tk.Label(self.root, text="Número de registros:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        tk.Entry(self.root, textvariable=self.num_records, width=15, font=("Arial", 12)).grid(row=1, column=1, sticky="w", padx=20)

        # Nombre del archivo
        tk.Label(self.root, text="Nombre del archivo:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=20, pady=10)
        tk.Entry(self.root, textvariable=self.filename, width=20, font=("Arial", 12)).grid(row=2, column=1, sticky="w", padx=20)

        # Botón para agregar columnas
        tk.Button(self.root, text="Agregar Columna", font=("Arial", 12), command=self.add_column, width=20, height=2).grid(row=3, column=0, pady=20, padx=20, columnspan=2)

        # Listado de columnas
        self.columns_frame = tk.Frame(self.root)
        self.columns_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

        # Botón para generar
        tk.Button(self.root, text="Generar Datos", font=("Arial", 14), command=self.generate_file, width=20, height=2, bg="#4CAF50", fg="white").grid(row=5, column=0, pady=20, columnspan=2)

    def add_column(self):
        def save_column():
            column_name = column_name_var.get()
            column_type = column_type_var.get()

            if not column_name or not column_type:
                messagebox.showerror("Error", "Debe completar todos los campos")
                return

            column_config = {"name": column_name, "type": column_type}

            # Configuración específica por tipo
            if column_type == "number":
                column_config["range"] = [int(min_value.get()), int(max_value.get())]
            elif column_type == "date":
                column_config["range"] = [start_date_var.get(), end_date_var.get()]
            elif column_type == "string":
                column_config["pattern"] = string_pattern_var.get()

            self.columns.append(column_config)
            column_window.destroy()
            self.update_columns_view()

        # Ventana para configuración de columnas
        column_window = tk.Toplevel(self.root)
        column_window.title("Nueva Columna")
        column_window.geometry("500x500")

        tk.Label(column_window, text="Nombre de la Columna:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        column_name_var = tk.StringVar()
        tk.Entry(column_window, textvariable=column_name_var, font=("Arial", 12), width=20).grid(row=0, column=1)

        tk.Label(column_window, text="Tipo de Dato:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=10)
        column_type_var = tk.StringVar()
        column_type_combo = ttk.Combobox(column_window, textvariable=column_type_var, state="readonly", font=("Arial", 12))
        column_type_combo["values"] = ("number", "string", "date")
        column_type_combo.grid(row=1, column=1, padx=20)

        # Configuraciones adicionales
        config_frame = tk.Frame(column_window)
        config_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

        # Campos adicionales para "number"
        min_value = tk.Entry(config_frame, font=("Arial", 12))
        max_value = tk.Entry(config_frame, font=("Arial", 12))

        # Campos adicionales para "date"
        start_date_var = tk.StringVar()
        end_date_var = tk.StringVar()

        # Campos adicionales para "string"
        string_pattern_var = tk.StringVar()

        # Función para actualizar los campos visibles según el tipo de dato seleccionado
        def update_fields():
            # Limpiar los campos
            for widget in config_frame.winfo_children():
                widget.grid_forget()

            if column_type_var.get() == "number":
                # Mostrar campos numéricos
                tk.Label(config_frame, text="Mínimo:", font=("Arial", 12)).grid(row=0, column=0)
                min_value.grid(row=0, column=1)
                tk.Label(config_frame, text="Máximo:", font=("Arial", 12)).grid(row=1, column=0)
                max_value.grid(row=1, column=1)
            elif column_type_var.get() == "date":
                # Mostrar campos de fecha
                tk.Label(config_frame, text="Fecha Inicio:", font=("Arial", 12)).grid(row=0, column=0)
                tk.Entry(config_frame, textvariable=start_date_var, font=("Arial", 12), width=10).grid(row=0, column=1)
                tk.Label(config_frame, text="Fecha Fin", font=("Arial", 12)).grid(row=1, column=0)
                tk.Entry(config_frame, textvariable=end_date_var, font=("Arial", 12), width=10).grid(row=1, column=1)
            elif column_type_var.get() == "string":
                # Mostrar selector de patrones de cadena
                tk.Label(config_frame, text="Patrón de cadena:", font=("Arial", 12)).grid(row=0, column=0)
                string_pattern_combo = ttk.Combobox(config_frame, textvariable=string_pattern_var, state="readonly", font=("Arial", 12))
                string_pattern_combo["values"] = fields  # Aquí le asignas los patrones disponibles
                string_pattern_combo.grid(row=0, column=1)

        # Actualizar los campos cuando cambie el tipo de dato
        column_type_combo.bind("<<ComboboxSelected>>", lambda event: update_fields())

        # Botón para guardar la columna
        tk.Button(column_window, text="Guardar", font=("Arial", 12), command=save_column).grid(row=5, column=0, columnspan=2, pady=20)

    def update_columns_view(self):
        for widget in self.columns_frame.winfo_children():
            widget.destroy()

        for idx, col in enumerate(self.columns):
            col_label = tk.Label(self.columns_frame, text=f"{col['name']} ({col['type']})", font=("Arial", 10))
            col_label.grid(row=idx, column=0, sticky="w")

    def generate_file(self):
        if not self.columns:
            messagebox.showerror("Error", "Debe agregar al menos una columna.")
            return

        num_records = self.num_records.get()
        data = generate_data(self.columns, num_records)
        save_to_csv(data, self.filename.get() + ".csv")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = DataGeneratorApp(root)
    root.mainloop()
