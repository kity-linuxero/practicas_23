class Pila:
    def __init__(self):
        self.datos=[]

    def apilar(self, elemento):
        self.datos.append(elemento)

    def desapilar(self):
        try:
            return self.datos.pop()
        except:
            print("La pila está vacía")
            return False
    
    def top(self):
        if not self.vacia():
            return self.datos[-1]
        else:
            return False

    def vacia(self):
        return not self.datos
    
    def cant_elementos(self):
        return len(self.datos)
    
    def __str__(self):
        aux=''
        for e in reversed(self.datos):
            aux+=f"|{e}|\n"
        return aux
    
p = Pila()
p.apilar('1')
p.apilar('2')
p.apilar('3')
p.apilar('4')
p.apilar('5')

print(p)
print(p)
