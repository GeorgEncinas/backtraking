import math

class Sensor_Velocidad:

    def __init__(self, radio_, sensor_, nro_secciones):
        self.radio = radio_
        self.sensor = sensor_
        self.nro_seccion = nro_secciones

    def get_desplazamiento(self):
        #obtener el perimetro de la rueda, el radio debe estar en metros
        perimetro = 2*math.pi*self.radio
        distandia_seccion_recorrido = perimetro/self.nro_seccion
        return distandia_seccion_recorrido

    def get_angulo_seccion(self):
        return (2*math.pi)/self.nro_seccion

    def get_distancia(self, contador):
        return contador*self.get_desplazamiento()
