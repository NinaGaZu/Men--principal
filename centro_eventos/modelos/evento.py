"""
Módulo que define la clase Evento
"""


class Evento:
    """Clase que representa un evento del CentroEventosArenasX"""
    
    def __init__(self, nombre, organizador, fecha, categoria, tipos_evento,
                 estado, asistentes, ubicacion, descripcion):
        """
        Inicializa un nuevo evento.
        
        Args:
            nombre (str): Nombre del evento
            organizador (str): Nombre del organizador
            fecha (str): Fecha del evento
            categoria (str): Categoría (Cultural, Deportivo, Social)
            tipos_evento (list): Lista de tipos de evento
            estado (str): Estado (Programado, Realizado)
            asistentes (str): Número de asistentes estimados
            ubicacion (str): Ubicación del evento
            descripcion (str): Descripción del evento
        """
        self.nombre = nombre
        self.organizador = organizador
        self.fecha = fecha
        self.categoria = categoria
        self.tipos_evento = tipos_evento
        self.estado = estado
        self.asistentes = asistentes
        self.ubicacion = ubicacion
        self.descripcion = descripcion
    
    def to_dict(self):
        """Convierte el evento a diccionario"""
        return {
            'nombre': self.nombre,
            'organizador': self.organizador,
            'fecha': self.fecha,
            'categoria': self.categoria,
            'tipos_evento': self.tipos_evento,
            'estado': self.estado,
            'asistentes': self.asistentes,
            'ubicacion': self.ubicacion,
            'descripcion': self.descripcion
        }
    
    def mostrar_info(self):
        """Muestra la información del evento en terminal"""
        print("\n" + "="*60)
        print("EVENTO REGISTRADO - CENTROEVENTOSARENASX")
        print("="*60)
        print(f"Nombre del Evento: {self.nombre}")
        print(f"Organizador: {self.organizador}")
        print(f"Fecha: {self.fecha}")
        print(f"Categoría: {self.categoria}")
        print(f"Tipo de Evento: {', '.join(self.tipos_evento)}")
        print(f"Estado: {self.estado}")
        print(f"Número de Asistentes: {self.asistentes}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Descripción: {self.descripcion}")
        print("="*60 + "\n")
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria} - {self.estado}"