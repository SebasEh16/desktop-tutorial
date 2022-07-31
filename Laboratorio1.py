"""El siguiente programa esta basado en un proceso químico, el cual es el preparar soluciones por medio de Disolucines,
 por medio de la formula C1*V1=C2*V2 se puede averiguar la concentración o volumen que la solucion necesita"""
#Creando clase 
class solucionnes:
    def __init__(self):
        self.c_1= int (input("Ingresar la priemra concentracion:"))
        self.c_2= int (input("Ingresar la segunda concentracion:"))
        self.v_1= int (input("Ingresar el pirmer volumen:")) 
        self.v_2= int (input("Ingresar el segundo volumen:")) 
 #El dato que se calculara sera el que al moemento de ingresar los valores sea meno o igual a 0   
    def concenuno(self):
            concen_1= (self.c_2*self.v_2)/self.v_1
            print("La concentracion molar 1 es:",round(concen_1,2),"M")
    def concendos(self):
            concen_2= (self.c_1*self.v_1)/self.v_2
            return print("La concentracion molar 2 es:",round(concen_2,2),"M")
    def volumuno(self):
            volum_1= (self.c_2*self.v_2)/self.c_1
            return print("El volumen 1 es:",round(volum_1,2), "Ml")
    def volumdos(self):
            volum_2= (self.c_1*self.v_1)/self.c_2 
            return print("El volumen 2 es:",round(volum_2,2),"Ml")

solu=solucionnes()
print("\n")
solu.concenuno()
solu.concendos()
solu.volumuno()
solu.volumdos()

    



