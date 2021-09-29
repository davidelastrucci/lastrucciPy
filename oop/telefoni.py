class telefoni:

   def __init__(self, modello, marca, sistema_operativo, anno_di_produzione, colore):
     self.modello = modello
     self.marca = marca
     self.sistema_operativo = sistema_operativo
     self.anno_di_produzione = anno_di_produzione
     self.colore = colore 
   def scheda(self):
        return f'\nModello {self.modello}\nMarca: {self.marca}\nSistema_operativo:{self.sistema_operativo}\nAnno_di_produzione:{self.anno_di_produzione}\nColore:{self.colore}'

iPhone= telefoni("iPhone","Apple","Ios 15","2018","nero")

print(iPhone.scheda())