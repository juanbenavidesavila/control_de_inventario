from django.db import models


# Create your models here.
class Vehiculo(models.Model):
    marcas = [["Abarth", "Abarth"], ["BMW", "BMW"], ["Dacia", "Dacia"], ["Infiniti", "Infiniti"], ["Kia", "Kia"], ["Land Rover", "Land Rover"], ["Mercedes-Benz", "Mercedes-Benz"], ["Opel", "Opel"], ["Rolls-Royce", "Rolls-Royce"], ["Subaru", "Subaru"], ["Volkswagen", "Volkswagen"], ["Alfa Romeo", "TAlfa Romeo"], ["Cadillac", "Cadillac"], ["Ferrari", "Ferrari"], ["Isuzu", "Isuzu"], ["KTM", "KTM"], ["Lexus", "Lexus"], ["Mini", "Mini"], ["Peugeot", "Peugeot"], ["Seat", "Seat"], ["Suzuki", "Suzuki"], ["Volvo", "Volvo"], ["Aston Martin", "Aston Martin"], ["Toyota", "Toyota"], ["Caterham", "Caterham"], ["Iveco", "Iveco"], ["Lada", "Lada"], ["Lotus", "Lotus"], ["Fiat", "Fiat"], ["Mitsubishi", "Mitsubishi"], ["Piaggio", "Piaggio"], ["Skoda", "Skoda"], ["Tata", "Tata"], ["Audi", "Audi"], ["Jaguar", "Jaguar"], ["Lamborghini", "Lamborghini"], ["Maserati", "Maserati"], ["Chevrolet", "Chevrolet"], ["Ford", "Ford"], ["Morgan", "Morgan"], ["Porsche", "Porsche"], ["Smart", "Smart"], ["Tesla", "Tesla"], ["Bentley", "Bentley"], ["Citroen", "Citroen"], ["Honda", "Honda"], ["Jeep", "Jeep"], ["Lancia", "Lancia"], ["Mazda", "Mazda"], ["Nissan", "Nissan"], ["Renault", "Renault"], ["SsangYong", "SsangYong"], ["Toyota", "Toyota"]]
    marca = models.CharField(max_length=20, choices=marcas, default="Ford")
    modelo = models.CharField(max_length=20)
    condiciones = [["Nuevo", "Nuevo"], ["Seminuevo", "Seminuevo"], ["Usado", "Usado"]]
    condicion = models.CharField(max_length=20, 
                                 choices=condiciones, 
                                 default="Nuevo")
    año = models.CharField(max_length=5, default="2024")
    categorias = [["Particular", "Particular"], ["Transporte", "Transporte"],
                  ["Carga", "Carga"]]
    categoria = models.CharField(max_length=20,
                                 choices=categorias,
                                 default="Particular")

    precio = models.DecimalField(max_digits=20,
                                 decimal_places=0,
                                 blank=False,
                                 null=False)
    #auto_now_add Se anade una sola vez, cuando se crea el registro
    creacion = models.DateTimeField(auto_now_add=True)
    #auto_now Se modifica con cada cambio que se realize en el registro
    modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [("visualizar_catalogo", "Visualizar catalogos")]
      
#function para determinar la condicion de precio seguna su valor.
    #def condicion_precio(self):

      
      #if self.precio >= 0 and self.precio <= 10000:
        #return "Bajo"
      
      #return "Alto"


# medio: 10001 30000
# alto: 30001 a mas
