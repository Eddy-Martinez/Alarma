global bandera
class contraseña:
        def __init__(self,contaseña):
                self.contraseña=contraseña

        def pregunta(self):
                global bandera
                bandera = 1
                contraseña=1234
                real=0
                while (real != contraseña):
                        real=int(input("Ingrese contraseña\t"))
                        if(real==contraseña):
                                print ("Alarma desactivada\n")
                                bandera = 0
                        else:
                                print("Contraseña incorrecta\n")
class activa:
        def __init__(self,activa):
                self.activa=activa

        def pregunta(self):
                global bandera
                respuesta='N'
                while (respuesta != 'S'):
                        respuesta=input("¿Activar alarma?\n")
                print("Alarma activada\n")
                bandera = 1
                
activa.pregunta('S')
while (bandera == 1):
        contraseña.pregunta(1234)
        while (bandera == 0):
                activa.pregunta('S')       
