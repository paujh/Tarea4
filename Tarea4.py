#Jorge Hinostrosa Paula
#paulajhinostrosa@ciencias.unam.mx
import random as r
class Smartphone:
  
  def __init__(self,marca,pantalla,imei,codBloqueo,bloqueado,bateria):
    self.marca=marca
    self.pantalla=pantalla
    self.imei=imei
    self.codBloqueo=codBloqueo
    self.bloqueado=bloqueado
    self.bateria=bateria
  
  def __str__(self):
    return "Marca:"+str(self.marca)+"\nPantalla: "+str(self.pantalla)+"\nIMEI: "+str(self.imei)+"\nCódigo de bloqueo: "+str(self.codBloqueo)+"\nBloqueado: "+str(self.bloqueado)+"\nCarga de bateria: "+str(self.bateria)+"%"

  def getCodBloqueo(self):
    return self.codBloqueo
  
  def getBateria(self):
    return self.bateria

  def setCodBloqueo(self,nCodigo):
    self.codBloqueo=nCodigo

  def setBateria(self,nBateria):
    self.bateria=nBateria

  def cargaBateria(self):
    if self.bateria<=99:
      self.bateria=self.bateria+1
    else:
      self.bateria=self.bateria

  def descargaBateria(self):
    if self.bateria>0:
      self.bateria=self.bateria-1
    else:
      self.bateria=self.bateria

  def bloquear(self):
    self.bloqueado=True
  
  def desbloquear(self,cod):
    if self.codBloqueo==cod:
      self.bloqueado=False
    else:
      self.bloqueado=True
      print("El código de desbloqueo es incorrecto.")

  def smartphonePseudoaleatorio():
    n=len(listaM)
    marca=listaM[r.randint(0,n-1)]
    l1=[]
    a=r.uniform(320,3840)
    b=r.uniform(320,a)
    num="0123456789"
    cadena=""
    for i in range(15):
      cadena=cadena+num[r.randint(0,9)]
    l=[]
    for i in range(0,10000):
      l.append(i)
    n=len(l)
    codigo=l[r.randint(0,n-1)]
    bloqueado=listaN[r.randint(0,1)]
    l2=[]
    for i in range(0,101):
      l2.append(i)
    n=len(l2)
    bateria=l2[r.randint(0,n-1)]
    return Smartphone(marca,[a,b],cadena,codigo,bloqueado,bateria)
  

listaM=["Samsung","Apple","Huawei","Xiaomi","Sony","LG"]
listaN=[True,False]
s1=Smartphone("Huawei",[1920,1080],123456789012345,1567,False,66)
print(s1)
s1.setCodBloqueo(8665)
print(s1.getCodBloqueo())
s1.setBateria(75)
print(s1)
s1.cargaBateria()
print(s1.getBateria())
s1.setBateria(54)
s1.descargaBateria()
print(s1.getBateria())
s1.bloquear()
print(s1)
s1.desbloquear(1597)
s1.desbloquear(8665)
print(s1)
s2=Smartphone.smartphonePseudoaleatorio()
print(s2)
