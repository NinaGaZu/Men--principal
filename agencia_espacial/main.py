import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

def extraer_id(cadena):
    valores = cadena.split(',')
    for valor in valores:
        if "ID" in valor:
            numero_id = int(valor.split(':')[1].strip())
            return numero_id

class AgenciaEspacialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Agencias Espaciales")
        self.root.geometry("800x600")
        
        # Configuración de la conexión a la base de datos
        self.db_config = {
            'user': 'root',
            'password': 'FamGaZu05',
            'host': 'localhost',
            'database': 'semana8'
        }
        
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            self.cursor = self.connection.cursor()
            messagebox.showinfo("Conexión", "Conexión a la base de datos exitosa")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al conectar a la base de datos: {err}")
            self.root.destroy()
            return
        
        # Crear y configurar los elementos de la interfaz gráfica
        self.label_id = tk.Label(root, text="ID:")
        self.entry_id = tk.Entry(root)
        
        self.label_nombre = tk.Label(root, text="Nombre:")
        self.entry_nombre = tk.Entry(root)
        
        self.label_pais = tk.Label(root, text="País:")
        self.entry_pais = tk.Entry(root)
        
        self.label_fecha = tk.Label(root, text="Fecha de Creación (YYYY-MM-DD):")
        self.entry_fecha = tk.Entry(root)
        
        self.btn_agregar = tk.Button(root, text="Agregar Agencia", command=self.agregar_agencia)
        self.btn_mostrar = tk.Button(root, text="Mostrar Agencias", command=self.mostrar_agencias)
        self.btn_borrar = tk.Button(root, text="Borrar Agencia", command=self.borrar_agencia)
        self.btn_actualizar = tk.Button(root, text="Actualizar Agencia", command=self.actualizar_agencia)
        
        # Lista para almacenar información de agencias mostradas
        self.lista_agencias = tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=15)
        self.lista_agencias.bind('<<ListboxSelect>>', self.cargar_datos_seleccionados)
        
        # Ubicar elementos en la interfaz gráfica
        self.label_id.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        self.label_nombre.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        self.label_pais.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_pais.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        self.label_fecha.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_fecha.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        self.lista_agencias.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.btn_agregar.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        self.btn_mostrar.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        self.btn_borrar.grid(row=6, column=0, padx=10, pady=5, sticky="ew")
        self.btn_actualizar.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        
        # Mostrar agencias al iniciar
        self.mostrar_agencias()
    
    def agregar_agencia(self):
        id_agencia = self.entry_id.get()
        nombre = self.entry_nombre.get()
        pais = self.entry_pais.get()
        fecha = self.entry_fecha.get()
        
        if not id_agencia or not nombre or not pais or not fecha:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
            
        try:
            # Validar formato de fecha
            datetime.strptime(fecha, '%Y-%m-%d')
            
            # Insertar datos en la tabla
            query = "INSERT INTO AgenciaEspacial(ID, Nombre, Pais, FechaCreacion) VALUES(%s, %s, %s, %s)"
            values = (id_agencia, nombre, pais, fecha)
            self.cursor.execute(query, values)
            
            # Confirmar la transacción
            self.connection.commit()
            
            messagebox.showinfo("Éxito", "Agencia espacial agregada correctamente")
            self.limpiar_campos()
            self.mostrar_agencias()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use YYYY-MM-DD")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al agregar agencia: {err}")
    
    def mostrar_agencias(self):
        try:
            # Limpiar la lista de agencias antes de mostrarlas
            self.lista_agencias.delete(0, tk.END)
            
            # Realizar una consulta SELECT
            query = "SELECT * FROM AgenciaEspacial"
            self.cursor.execute(query)
            
            # Obtener todos los resultados
            agencias = self.cursor.fetchall()
            
            # Mostrar los resultados en la lista
            for agencia in agencias:
                self.lista_agencias.insert(tk.END, f"ID: {agencia[0]}, Nombre: {agencia[1]}, País: {agencia[2]}, Fecha: {agencia[3]}")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al mostrar agencias: {err}")
    
    def borrar_agencia(self):
        try:
            seleccion = self.lista_agencias.curselection()
            if seleccion:
                agencia_seleccionada = self.lista_agencias.get(seleccion[0])
                agencia_id = extraer_id(agencia_seleccionada)
                
                # Confirmación antes de borrar
                respuesta = messagebox.askyesno("Confirmar", f"¿Está seguro de borrar la agencia con ID {agencia_id}?")
                if respuesta:
                    # Borrar agencia de la base de datos
                    query = "DELETE FROM AgenciaEspacial WHERE ID=%s"
                    self.cursor.execute(query, (agencia_id,))
                    
                    # Confirmar la transacción
                    self.connection.commit()
                    
                    messagebox.showinfo("Éxito", f"Agencia con ID {agencia_id} borrada correctamente")
                    self.mostrar_agencias()
                    self.limpiar_campos()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al borrar agencia: {err}")
    
    def cargar_datos_seleccionados(self, event):
        seleccion = self.lista_agencias.curselection()
        if seleccion:
            agencia_seleccionada = self.lista_agencias.get(seleccion[0])
            agencia_id = extraer_id(agencia_seleccionada)
            
            # Obtener datos de la agencia seleccionada
            query = "SELECT * FROM AgenciaEspacial WHERE ID=%s"
            self.cursor.execute(query, (agencia_id,))
            datos_agencia = self.cursor.fetchone()
            
            # Cargar datos en los campos de entrada
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, datos_agencia[0])
            
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, datos_agencia[1])
            
            self.entry_pais.delete(0, tk.END)
            self.entry_pais.insert(0, datos_agencia[2])
            
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.insert(0, datos_agencia[3])
    
    def actualizar_agencia(self):
        try:
            seleccion = self.lista_agencias.curselection()
            if not seleccion:
                messagebox.showwarning("Advertencia", "Seleccione una agencia para actualizar")
                return
            
            agencia_id = self.entry_id.get()
            nombre = self.entry_nombre.get()
            pais = self.entry_pais.get()
            fecha = self.entry_fecha.get()
            
            if not agencia_id or not nombre or not pais or not fecha:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
                
            try:
                # Validar formato de fecha
                datetime.strptime(fecha, '%Y-%m-%d')
                
                # Actualizar agencia en la base de datos
                query = "UPDATE AgenciaEspacial SET Nombre=%s, Pais=%s, FechaCreacion=%s WHERE ID=%s"
                values = (nombre, pais, fecha, agencia_id)
                self.cursor.execute(query, values)
                
                # Confirmar la transacción
                self.connection.commit()
                
                messagebox.showinfo("Éxito", f"Agencia con ID {agencia_id} actualizada correctamente")
                self.mostrar_agencias()
                self.limpiar_campos()
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha incorrecto. Use YYYY-MM-DD")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al actualizar agencia: {err}")
    
    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_pais.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = AgenciaEspacialApp(root)
    root.mainloop()
    app.cursor.close()
    app.connection.close()

if __name__ == "__main__":
    main()