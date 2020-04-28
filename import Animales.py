import Animales
class Conejos(Animales.Animales):
	"""Creamos la clase conejos y heredamos parte de su comportamiento de la clase Animales"""
	def __reserva(self,reserva):
		
		self.reserva_alimenticia+=reserva
	def Alimentarse(self,tipo_alimento,cantidad_alimento):					
		
		if(tipo_alimento.lower()=="pasto"):
			self.__reserva(cantidad_alimento)
		else:
			print("No debe alimentar a animales herviboros con {0}".format(tipo_alimento))