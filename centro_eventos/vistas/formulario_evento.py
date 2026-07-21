"""
Módulo que contiene el formulario de registro de eventos
"""

import tkinter as tk


class FormularioEvento:
    """Clase que construye el formulario de registro de eventos"""
    
    def __init__(self, parent, controller):
        """
        Inicializa el formulario.
        
        Args:
            parent: Ventana principal de Tkinter
            controller: Controlador del evento
        """
        self.parent = parent
        self.controller = controller
        
        # Variables para Radiobuttons y Checkbuttons
        self.var_categoria = tk.StringVar()
        self.var_estado = tk.StringVar()
        self.var_ubicacion = tk.StringVar()
        self.var_conferencia = tk.IntVar()
        self.var_concierto = tk.IntVar()
        self.var_fiesta = tk.IntVar()
        self.var_taller = tk.IntVar()
        self.var_exposicion = tk.IntVar()
        
        # Lista de ubicaciones
        self.ubicaciones = ["Salón Principal", "Área al Aire Libre", 
                           "Auditorio", "Sala de Conferencias"]
        
        # Widgets de entrada (se inicializan en construir_formulario)
        self.entry_nombre = None
        self.entry_organizador = None
        self.entry_fecha = None
        self.entry_asistentes = None
        self.text_descripcion = None
        
        self.construir_formulario()
    
    def construir_formulario(self):
        """Construye todos los elementos del formulario con scroll"""
        # Crear Canvas y Scrollbar
        canvas = tk.Canvas(self.parent)
        scrollbar = tk.Scrollbar(self.parent, orient="vertical", command=canvas.yview)
        
        # Frame contenedor dentro del canvas
        self.scrollable_frame = tk.Frame(canvas)
        
        # Configurar el scroll
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        # Crear ventana dentro del canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Construir los frames dentro del scrollable_frame
        self._construir_frame_detalles()
        self._construir_frame_categoria()
        self._construir_frame_estado()
        self._construir_frame_asistentes()
        self._construir_frame_descripcion()
        self._construir_frame_ubicacion()
        self._construir_botones()
    
    def _construir_frame_detalles(self):
        """Construye el frame de detalles del evento"""
        frame_detalles = tk.LabelFrame(
            self.scrollable_frame, text="Detalles del Evento",
            font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_detalles.pack(pady=10, padx=10, fill="x")
        
        # Nombre del evento
        label_nombre = tk.Label(frame_detalles, text="Nombre del Evento:")
        label_nombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame_detalles, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        # Organizador
        label_organizador = tk.Label(frame_detalles, text="Organizador:")
        label_organizador.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_organizador = tk.Entry(frame_detalles, width=40)
        self.entry_organizador.grid(row=1, column=1, padx=5, pady=5)
        
        # Fecha
        label_fecha = tk.Label(frame_detalles, text="Fecha del Evento:")
        label_fecha.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_fecha = tk.Entry(frame_detalles, width=40)
        self.entry_fecha.grid(row=2, column=1, padx=5, pady=5)
    
    def _construir_frame_categoria(self):
        """Construye el frame de categoría y tipo de evento"""
        frame_categoria = tk.LabelFrame(
            self.scrollable_frame, text="Categoría y Tipo de Evento",
            font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_categoria.pack(pady=10, padx=10, fill="x")
        
        # Categoría (Radiobuttons)
        label_categoria = tk.Label(frame_categoria, text="Categoría:")
        label_categoria.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        frame_radio_categoria = tk.Frame(frame_categoria)
        frame_radio_categoria.grid(row=0, column=1, sticky="w")
        
        tk.Radiobutton(frame_radio_categoria, text="Cultural",
                       variable=self.var_categoria, value="Cultural"
        ).pack(side="left", padx=5)
        
        tk.Radiobutton(frame_radio_categoria, text="Deportivo",
                       variable=self.var_categoria, value="Deportivo"
        ).pack(side="left", padx=5)
        
        tk.Radiobutton(frame_radio_categoria, text="Social",
                       variable=self.var_categoria, value="Social"
        ).pack(side="left", padx=5)
        
        # Tipo de evento (Checkbuttons)
        label_tipo = tk.Label(frame_categoria, text="Tipo de Evento:")
        label_tipo.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        frame_check_tipo = tk.Frame(frame_categoria)
        frame_check_tipo.grid(row=1, column=1, sticky="w")
        
        tk.Checkbutton(frame_check_tipo, text="Conferencia",
                       variable=self.var_conferencia
        ).pack(side="left", padx=5)
        
        tk.Checkbutton(frame_check_tipo, text="Concierto",
                       variable=self.var_concierto
        ).pack(side="left", padx=5)
        
        tk.Checkbutton(frame_check_tipo, text="Fiesta",
                       variable=self.var_fiesta
        ).pack(side="left", padx=5)
        
        tk.Checkbutton(frame_check_tipo, text="Taller",
                       variable=self.var_taller
        ).pack(side="left", padx=5)
        
        tk.Checkbutton(frame_check_tipo, text="Exposición",
                       variable=self.var_exposicion
        ).pack(side="left", padx=5)
    
    def _construir_frame_estado(self):
        """Construye el frame de estado del evento"""
        frame_estado = tk.LabelFrame(
            self.scrollable_frame, text="Estado del Evento",
            font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_estado.pack(pady=10, padx=10, fill="x")
        
        label_estado = tk.Label(frame_estado, text="Estado:")
        label_estado.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        frame_radio_estado = tk.Frame(frame_estado)
        frame_radio_estado.grid(row=0, column=1, sticky="w")
        
        tk.Radiobutton(frame_radio_estado, text="Programado",
                       variable=self.var_estado, value="Programado"
        ).pack(side="left", padx=5)
        
        tk.Radiobutton(frame_radio_estado, text="Realizado",
                       variable=self.var_estado, value="Realizado"
        ).pack(side="left", padx=5)
    
    def _construir_frame_asistentes(self):
        """Construye el frame de número de asistentes"""
        frame_asistentes = tk.LabelFrame(
            self.scrollable_frame, text="Número de Asistentes",
            font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_asistentes.pack(pady=10, padx=10, fill="x")
        
        label_asistentes = tk.Label(
            frame_asistentes, text="Número de Asistentes Estimados:"
        )
        label_asistentes.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_asistentes = tk.Entry(frame_asistentes, width=40)
        self.entry_asistentes.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    
    def _construir_frame_descripcion(self):
        """Construye el frame de descripción del evento"""
        frame_descripcion = tk.LabelFrame(
            self.scrollable_frame, text="Descripción del Evento",
            font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_descripcion.pack(pady=10, padx=10, fill="x")
        
        label_descripcion = tk.Label(frame_descripcion, text="Descripción:")
        label_descripcion.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        self.text_descripcion = tk.Text(frame_descripcion, height=4, width=40)
        self.text_descripcion.grid(row=0, column=1, padx=5, pady=5)
    
    def _construir_frame_ubicacion(self):
        """Construye el frame de ubicación del evento"""
        frame_ubicacion = tk.LabelFrame(
            self.scrollable_frame, text="Ubicación del Evento",
            font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_ubicacion.pack(pady=10, padx=10, fill="x")
        
        label_ubicacion = tk.Label(frame_ubicacion, text="Ubicación:")
        label_ubicacion.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.var_ubicacion.set(self.ubicaciones[0])
        menu_ubicacion = tk.OptionMenu(
            frame_ubicacion, self.var_ubicacion, *self.ubicaciones
        )
        menu_ubicacion.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    
    def _construir_botones(self):
        """Construye los botones de acción"""
        frame_botones = tk.Frame(self.scrollable_frame)
        frame_botones.pack(pady=20)
        
        btn_registrar = tk.Button(
            frame_botones, text="Registrar Evento",
            command=self.controller.registrar_evento,
            bg="#4CAF50", fg="white",
            font=("Arial", 10, "bold"),
            padx=20, pady=10
        )
        btn_registrar.pack(side="left", padx=10)
        
        btn_limpiar = tk.Button(
            frame_botones, text="Limpiar",
            command=self.controller.limpiar_formulario,
            bg="#f44336", fg="white",
            font=("Arial", 10, "bold"),
            padx=20, pady=10
        )
        btn_limpiar.pack(side="left", padx=10)
    
    def obtener_datos(self):
        """
        Obtiene todos los datos del formulario.
        
        Returns:
            dict: Diccionario con los datos del formulario
        """
        # Obtener tipos de evento seleccionados
        tipos_evento = []
        if self.var_conferencia.get():
            tipos_evento.append("Conferencia")
        if self.var_concierto.get():
            tipos_evento.append("Concierto")
        if self.var_fiesta.get():
            tipos_evento.append("Fiesta")
        if self.var_taller.get():
            tipos_evento.append("Taller")
        if self.var_exposicion.get():
            tipos_evento.append("Exposición")
        
        return {
            'nombre': self.entry_nombre.get(),
            'organizador': self.entry_organizador.get(),
            'fecha': self.entry_fecha.get(),
            'categoria': self.var_categoria.get(),
            'tipos_evento': tipos_evento,
            'estado': self.var_estado.get(),
            'asistentes': self.entry_asistentes.get(),
            'ubicacion': self.var_ubicacion.get(),
            'descripcion': self.text_descripcion.get("1.0", tk.END).strip()
        }
    
    def limpiar(self):
        """Limpia todos los campos del formulario"""
        # Limpiar Entry
        self.entry_nombre.delete(0, tk.END)
        self.entry_organizador.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_asistentes.delete(0, tk.END)
        
        # Limpiar Text
        self.text_descripcion.delete("1.0", tk.END)
        
        # Resetear Radiobuttons
        self.var_categoria.set(None)
        self.var_estado.set(None)
        
        # Resetear Checkbuttons
        self.var_conferencia.set(0)
        self.var_concierto.set(0)
        self.var_fiesta.set(0)
        self.var_taller.set(0)
        self.var_exposicion.set(0)
        
        # Resetear Menú
        self.var_ubicacion.set(self.ubicaciones[0])