from RenePy.Utiles import *
print(SQL.insertar("Articulo","asd"))
# print(SQL.eliminarColumna("asd","zxc"))

# from operator import attrgetter,itemgetter
# import re
#
# import uuid
# print(str(uuid.uuid1()))
# print(str(uuid.uuid1()))
# print(str(uuid.uuid1()))



# def asd(ff):
#     def zz(*args,**keywords):
#         print("a")
#         ff(*args,**keywords)
#         print("b")
#     return zz

# def ggg(ff):
#     def zz(*args,**keywords):
#         print("************")
#         ff(*args,**keywords)
#         print("************")
#     return zz

# @ggg
# @asd
# def xx(r):
#     print(r,"  --")


# xx("ww")
# class TipoDeValidacion:
#     NO_NULL=None
#     STR_NO_EMPTY=None
#     STR_CON_ALFANUMERICOS=None
#     SOLO_INT_POSITIVO_STR=None
#     PATRON_SOLO_FLOAT_POSITIVO_STR=None
#     STR_CORREO=None
#     STR_SOLO_LETRAS=None
#     STR_SOLO_LETRAS_Y_NUMEROS=None
#     STR_SOLO_ALFANUMERICOS=None
#     STR_SEGURIDAD_MINIMA_CONTRASEÑA=None
#     def __init__(self,esValido,getMensaje):
#         self.esValido=esValido
#         self.getMensaje=getMensaje
#     def setMensaje(self,texto):
#         self.getMensaje=lambda :texto
#
# __MEDIO_PATRON_LETRAS="(?:\\w|[ÑñáéíóúÁÉÍÓÚÀÈÌÒÙàèìòù])"
# #PATRON_CONTIENE_LETRAS=re.compile("(?:\\d*)((?![\\d_])\\w+(?<![\\d_]))(?:\\d*)")
# PATRON_CONTIENE_LETRAS=re.compile("(?:\\d*)((?![\\d_])"+__MEDIO_PATRON_LETRAS+"+(?<![\\d_]))(?:\\d*)")
#
# def hayMatch(patron,texto):
#     return len(re.findall(patron, texto)) > 0
# TipoDeValidacion.NO_NULL=TipoDeValidacion(lambda v:v is not None,lambda :"No puede estar vacío ")
# TipoDeValidacion.STR_NO_EMPTY=TipoDeValidacion(lambda v:TipoDeValidacion.NO_NULL.esValido(v) and isinstance(v,str) and len(v.strip())>0
#                                                ,lambda :"No puede estar vacío ")
#
# def evaluar(v):
#     print(TipoDeValidacion.NO_NULL.esValido(v))
#     print(isinstance(v,str))
#     #print(v is str)
#     print(len(v.strip())>0)
#
# evaluar("alberto ")
# print(TipoDeValidacion.STR_NO_EMPTY.esValido("alberto "))

#
# def separadorDePalabrasEnTextoUnido(palabra:str):
#     listaDePalabras=[]
#     #palabraActual = ""
#     p=[""]
#     def appenC(c):
#         p[0]+=c
#
#
#     def agregarPalabra():
#         if len(p[0])>0:
#             listaDePalabras.append(p[0])
#             p[0]=""
#
#     elAnteriorFueNumero=False
#     for c in palabra:
#         if c.isnumeric():
#             if not elAnteriorFueNumero:
#                 agregarPalabra()
#             appenC(c)
#             elAnteriorFueNumero=True
#             continue
#         else:
#             elAnteriorFueNumero=False
#         if c.isupper():
#             agregarPalabra()
#             appenC(c)
#         elif c=="_" or c.isspace():
#             agregarPalabra()
#         elif c.isalpha():
#             appenC(c)
#     agregarPalabra()
#     return  listaDePalabras
#
# lista=separadorDePalabrasEnTextoUnido("contraseñaConfirmar")
# lista=[p.title() for p in lista]
#
# verLista(" ".join(lista))


#
# class asd:
#     def __init__(self,a,b):
#         self.a=a
#         self.b = b
#     def __str__(self):
#         return strg("{a=",self.a," b=",self.b,"}")
#
#
#
# la=[asd(a,b) for a,b in [(4,7),(8,3),(1,9)]]
# verLista(la)
#
# la=sorted(la, key=attrgetter('b'))
# verLista(la)


#
# def crearMatrizDeConfusionBidimencionalDeUnaClase(matrizDeConfusionMulticlase,indiceDeClase):
#     """
#     [[Negativos Reales TN,Falsos Positivos FP],[ Falsos Negativos FN , Positivos Reales TP ]]
#     :param matrizDeConfusionMulticlase:
#     :param indiceDeClase:
#     :return:
#     """
#     FP=0
#     TP=0
#     FN=0
#     TN=0
#     for f in range(len(matrizDeConfusionMulticlase)):
#         fila=matrizDeConfusionMulticlase[f]
#         for c in range(len(fila)):
#             valor=fila[c]
#             if c==indiceDeClase and f ==indiceDeClase:
#                 TP+=valor
#             elif c==indiceDeClase and f!=indiceDeClase:
#                 FP+=valor
#             elif f==indiceDeClase and c!=indiceDeClase:
#                 FN+=valor
#             else:
#                 TN+=valor
#     return [[TN,FP],[FN,TP]]
#
# m=[[5,2,1],[3,4,4],[5,6,3]]
# #print(crearMatrizDeConfusionBidimencionalDeUnaClase(m,1))
#
#
# class MetricasDeClase:
#     def __init__(self):
#         self.precision=0
#         self.especificidad=0
#         self.sensibilidad=0
#
#         self.exactitud=0
#     def __str__(self):
#         def ft(n):
#             return "%.2f"%(n*100)
#         return " precision="+ft(self.precision)+" especificidad="+ft(self.especificidad)+" sensibilidad="+ft(self.sensibilidad)+" exactitud="+ft(self.exactitud)
#
# def getMetricasDeClase(matrizDeConfusionMulticlase):
#     metricas=[]
#     for i in range(len(matrizDeConfusionMulticlase)):
#         matrizBinaria=crearMatrizDeConfusionBidimencionalDeUnaClase(matrizDeConfusionMulticlase,i)
#         # print("--------------------------------")
#         # print(i)
#         # print(matrizBinaria)
#         #[[TN a, FP b], [FN c, TP d]]
#         TN=matrizBinaria[0][0]
#         FP=matrizBinaria[0][1]
#         FN = matrizBinaria[1][0]
#         TP = matrizBinaria[1][1]
#         metricaActual=MetricasDeClase()
#         # print(TP, "/(", FP, "+", TP, ")")
#         metricaActual.precision=TP/(FP+TP) #d/(b+d)
#
#         # print(TN, "/(", FN, "+", FP, ")")
#         metricaActual.especificidad = TN / (TN + FP)  # a/(a+b)
#
#         # print(TP, "/(", TP, "+", FN, ")")
#         metricaActual.sensibilidad = TP / (TP + FN)  # d/(d+c)
#
#         # print(TP, "/(", FP, "+", TP, ")")
#         metricaActual.exactitud = (TN+FP) / (TN + FP+FN+TP)  # (a+d)/(a+b+c+d)
#
#         t=metricaActual.exactitud
#         metricaActual.exactitud=metricaActual.precision
#         metricaActual.precision=t
#
#         metricas.append(metricaActual)
#     return metricas
#
#
# ma=[
#       [75,5,0,0]
#     ,[4,76,0,0]
#     ,[0,0,80,0]
#     ,[0,0,0,80]
# ]
# for i,metrica in enumerate(getMetricasDeClase(ma)):
#     print(i,"  ",metrica)
#

#
# y_true = ["gato", "lobo", "gato", "gato", "lobo", "perro"] # i => Renglones
# y_pred = ["lobo", "lobo", "gato", "gato", "lobo", "gato"] # j => Columnas
#
# Renglones=[]
# Columnas=[]
#
# maximo=3
# fila=[]
# for i,a in enumerate(y_true):
#     indice=i%maximo
#     fila.append(a)
#     if indice==maximo-1:
#         Renglones.append(fila)
#         fila=[]
# print(Renglones)
#




# class PaginacionSimple:
#     def __init__(self,indiceActual,cantidadDeElementos,step,cantidadDeIndicesAMostrarMaximo):
#         """
#         va intentar poner el indice actual en el medio
#         :param indiceActual: 1-... comienza en 1
#         :param cantidadDeElementos:
#         :param step:
#         :param cantidadDeIndicesAMostrarMaximo: 3-....  3 como minimo
#         """
#         cantidadDeIndices = int(cantidadDeElementos / step)
#         if cantidadDeElementos % step != 0:
#             cantidadDeIndices += 1
#
#         #self.listaDeIndices=[i for i in range(1,cantidadDeIndices+1)]
#         cantidadDeIndicesALosLados=cantidadDeIndicesAMostrarMaximo-1
#         if cantidadDeIndicesAMostrarMaximo>2:
#             cantidadDeIndicesALosLados=int((cantidadDeIndicesAMostrarMaximo-1)/2)
#
#         print(cantidadDeIndices)
#         self.listaDeIndices=[]
#         self.iActual=-1
#         if cantidadDeIndices>0 and indiceActual<=cantidadDeIndices:
#             if cantidadDeIndices==1 and indiceActual==1:
#                 self.listaDeIndices=[1]
#                 self.iActual=0
#             else:
#                 la = []
#                 ls = []
#                 indiceAnterior=-1
#                 indiceSiguiente=-1
#                 while (len(la)+len(ls)+1)<cantidadDeIndicesAMostrarMaximo\
#                         and (len(la)+len(ls)+1)<cantidadDeIndices:
#                     if indiceActual>1:
#                         if indiceAnterior==-1:
#                             indiceAnterior=indiceActual-1
#                             la.append(indiceAnterior)
#                         elif indiceAnterior>1:
#                             indiceAnterior = indiceAnterior - 1
#                             la.append(indiceAnterior)
#                     if indiceActual<cantidadDeIndices:
#                         if indiceSiguiente==-1:
#                             indiceSiguiente=indiceActual+1
#                             ls.append(indiceSiguiente)
#                         elif indiceSiguiente<cantidadDeIndices:
#                             indiceSiguiente = indiceSiguiente + 1
#                             ls.append(indiceSiguiente)
#                 la.reverse()
#                 self.listaDeIndices.extend(la)
#                 self.listaDeIndices.append(indiceActual)
#                 #ls.reverse()
#                 self.listaDeIndices.extend(ls)
#                 self.iActual = len(la)
#
#     def __str__(self):
#         return str(self.listaDeIndices)+"  "+str(self.iActual)
#
# print(PaginacionSimple(indiceActual=12,cantidadDeElementos=300,step=20,cantidadDeIndicesAMostrarMaximo=5))

# carpetaOrigen=File(r"C:\_COSAS\temporal\Nueva carpeta\carpeta original")
# carpetaDestino=File(r"C:\_COSAS\temporal\Nueva carpeta\carpeta destino")
#
# print("moviendo...")
# nuevoCarpeta=carpetaOrigen.move(carpetaDestino)
# print("se movio a "+str(nuevoCarpeta) if nuevoCarpeta is not None else "no se pudo mover")

# def utlizar(f):
#     f.rename("0_"+f.getName())
# Archivo.recorrerCarpeta(urlCarpeta,utlizar)
# urlZip=r"C://_COSAS//temporal//Nueva carpeta//Nueva carpeta.zip"
# urlCarpetaSalida=r"D://_Cosas//Programacion//Proyectos//Python//Django 3.1//ProyectoPCChar//media//descomprimido"
# def verNombre(nombre):
#     print("nombre=",nombre)
#     return True
# def verProgreso(total,indice):
#     print("total=",total," indice=",indice," ",((indice/total)*100),"%")
#     return True
# Archivo.extraerZip_BoolContinuar(urlZip=urlZip
#                                   ,urlCarpetaSalida=urlCarpetaSalida
#                                   ,metodoBool_AntesDeExtraer=verNombre
#                                  ,metodoBool_GetProgreso=verProgreso)

# class asd:
#     def __init__(self):
#         self.a = "a"
#         print(1)
#         self.metodoAbstr()
#         print(3)
#         self.c = "c"
#         self.vari()
#     def metodoAbstr(self):
#         pass
#     def vari(self):
#         print(vars(self))
# class qwe(asd):
#     def metodoAbstr(self):
#         print(2)
#         self.b="b"
# qwe()

# import re
# class TipoDeValidacion:
#     NO_NULL=None
#     STR_NO_EMPTY=None
#     STR_CON_ALFANUMERICOS=None
#     def __init__(self,esValido,getMensaje):
#
#         self.esValido=lambda v:True
#         self.getMensaje=lambda :""
#     def setMensaje(self,texto):
#         self.getMensaje=lambda :texto
# PATRON_CONTIENE_LETRAS=re.compile("(?:\\d*)((?![\\d_])\\w+(?<![\\d_]))(?:\\d*)")
# TipoDeValidacion.NO_NULL=TipoDeValidacion((lambda v:v is not None),(lambda :"No puede estar vacío "))

# import inspect
# class Uno(object):
#     def __init__(self,nombre):
#         self.nombre=nombre
# class Dos(object):
#     def __init__(self):
#         self.atributo_1=Uno("a")
#         self.atributo_2 = Uno("b")
#         self.atributo_3 = 3
#     def prueba(self):
#         d=vars(self)
#         print(self.__class__.__name__)
#         return [d[n] for n in d if isinstance(d[n],Uno) ]

        # print(vars(self))
        # print(self.__dir__())
        # print(self.__dict__)
        # print(self.__getattribute__())
        #
        # print(self.__dict__.keys())
        # print(dir(self))
        # l=inspect.getmembers(self)
        # for r in l:
        #     e=r[1]
        #     print(e," c=",inspect.isclass(e)," u=",isinstance(e,Uno))
#
# print(Dos().prueba())
# #print(Dos().__dict__.keys())
# print(vars(Dos()))
# # n = Dos()
#
#
# for i in inspect.getmembers(n):
#
#     if not i[0].startswith('_'):
#
#         if not inspect.ismethod(i[1]):
#             print("i=",i)
        # def calcularTotalDeBachs(cantidadDeImagenes,batch_size,porsentageParaValidacion=None):
#     if porsentageParaValidacion is not None:
#         imagenesParaValidar=cantidadDeImagenes*porsentageParaValidacion
#         print("imagenesParaValidar/batch_size=", imagenesParaValidar / batch_size)
#         print("imagenesParaValidar=",imagenesParaValidar)
#         tieneDecimales=(imagenesParaValidar-int(imagenesParaValidar))>0
#         if tieneDecimales:
#             print("tiene decimales")
#             imagenesParaValidar+=1
#
#         cantidadDeImagenes-=imagenesParaValidar
#         print("cantidadDeImagenes=",cantidadDeImagenes)
#         print("batch_size=", batch_size)
#         print("cantidadDeImagenes/batch_size=",cantidadDeImagenes/batch_size)
#         print("cantidadDeImagenes%batch_size=", cantidadDeImagenes % batch_size)
#     return int(cantidadDeImagenes/batch_size)
# print(calcularTotalDeBachs(cantidadDeImagenes=1120
#                            ,batch_size=32
#                            ,porsentageParaValidacion=0.2))
#
# print(calcularTotalDeBachs(cantidadDeImagenes=1040
#                            ,batch_size=32
#                            ,porsentageParaValidacion=0.2))
# def paraPruebas():
#     class DatosDeResultadoDeEntrenamiento:
#         def __init__(self):
#             self.clases = []
#             self.matrizDeConfusion = []
#             self.presicion = 0
#             self.perdida = 0
#     class Clas:
#         def __init__(self,Indice,NombreCarpetaCorrespondiente,Nombre):
#             self.Indice=Indice
#             self.NombreCarpetaCorrespondiente=NombreCarpetaCorrespondiente
#             self.Nombre=Nombre
#
#     listaDeClasesClasificacion=[Clas(0,'1 VERDE HECHO','VERDE HECHO')
#                                 ,Clas(1,'2 VERDE','VERDE')
#                                 ,Clas(2,'3 RAYONA','RAYONA')
#                                 ,Clas(3,'4 MADURA','MADURA')]
#     #listaDeClasesClasificacion=['1 VERDE HECHO','2 VERDE'',3 RAYONA','4 MADURA']
#
#     dr: DatosDeResultadoDeEntrenamiento=DatosDeResultadoDeEntrenamiento()
#     dr.clases=['1 VERDE HECHO','2 VERDE','3 RAYONA','4 MADURA']
#     dr.matrizDeConfusion=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#
#     matrisDeConfusionOrganizada = [[0 for j in range(len(dr.clases))] for i in range(len(dr.clases))]
#     nombresDeClasesOrganizados = [0 for i in range(len(dr.clases))]
#     for cla in listaDeClasesClasificacion:
#         nombresDeClasesOrganizados[cla.Indice] = cla.Nombre
#
#     for i in range(len(dr.matrizDeConfusion)):
#         for j in range(len(dr.matrizDeConfusion[i])):
#             f = -1
#             c = -1
#             for cla in listaDeClasesClasificacion:
#                 if f != -1 and c != -1:
#                     break
#                 a=cla.NombreCarpetaCorrespondiente
#                 b=dr.clases[i]
#                 cc = dr.clases[j]
#                 if f == -1 and a == b:
#                     f = cla.Indice
#                 if c == -1 and a == cc:
#                     c = cla.Indice
#             matrisDeConfusionOrganizada[f][c] = dr.matrizDeConfusion[i][j]
#     dr.clases = nombresDeClasesOrganizados
#     dr.matrizDeConfusion = matrisDeConfusionOrganizada
#     print("")
# paraPruebas()

# class asd:
# 	def __init__(self,nombre):
# 		self.nombre=nombre
# 	def __str__(self):
# 		return self.nombre+"-"
# 	@staticmethod
# 	def getAll():
# 		return [ asd(e) for e in ["a","b","c"]]
#
# for e in asd.getAll():
# 	print(str(e))


# def dineroAhorradoEnUnAño():
# 	dineroAhorradoEsteDiaEnCentavos=3
# 	dineroAhorradoAcumuladoEnCentavos=3
#
#
# 	cantidadDelDiasDelAño=256
# 	for i in range(cantidadDelDiasDelAño):
# 		diaDelAño=i+1
# 		dineroAhorradoEsteDiaEnPesos=dineroAhorradoEsteDiaEnCentavos/100
# 		dineroAhorradoAcumuladoEnPesos=dineroAhorradoAcumuladoEnCentavos/100
# 		dineroAhorradoEsteDiaEnCentavos*=3
# 		dineroAhorradoAcumuladoEnCentavos+=dineroAhorradoEsteDiaEnCentavos
# 		#este codigo es para ir reportando la cantidad que se va acumulando con los dias
# 		if dineroAhorradoAcumuladoEnPesos<1000000000:
# 			print("Día: %03d ahorrado ese dia en pesos: %13.2f$ acumulado en pesos: %13.2f$"%(diaDelAño,dineroAhorradoEsteDiaEnPesos,dineroAhorradoAcumuladoEnPesos))
# 		else:# A partir de aqui la cantidad de dinero acumulada y ahorrada es absurda desde el punto de vista monetario, y se veria mal en la visualizacion
# 			print("Día: %03d dinero de por vida"%(diaDelAño))
#
# 	dineroAhorradoAcumuladoTotalEnPesos=dineroAhorradoAcumuladoEnCentavos/100
# 	return dineroAhorradoAcumuladoTotalEnPesos
#
#
# print("EL Dinero que ahorro durante el año es de",dineroAhorradoEnUnAño(),"$")

# def metodo():
#     print("pasa por aqui")
#     anterior2=0
#     anterior=1
#     fibo=2
#     while fibo<10:
#         print(fibo)
#         anterior2=anterior
#         anterior=fibo
#         fibo=anterior+anterior2
# metodo()


# from RenePy.Utiles import *
# from RenePy.ClasesUtiles.Compilador import compilarAllPy
# from RenePy.MetodosUtiles.Subprocesos import *
# import threading
# import inspect
# import ctypes
# def _async_raise(tid, exctype):
#     '''Raises an exception in the threads with id tid'''
#     if not inspect.isclass(exctype):
#         raise TypeError("Only types can be raised (not instances)")
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),
#                                                      ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#         # "if it returns a number greater than one, you're in trouble,
#         # and you should call it again with exc=NULL to revert the effect"
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
# class StoppableThread(threading.Thread):
#     """Thread class with a stop() method. The thread itself has to check
#     regularly for the stopped() condition."""
#
#     def __init__(self,  *args, **kwargs):
#         super(StoppableThread, self).__init__(*args, **kwargs)
#         self._stop_event = threading.Event()
#
#     def stop(self):
#         self._stop_event.set()
#
#     def stopped(self):
#         return self._stop_event.is_set()
#
#     def _get_my_tid(self):
#         """determines this (self's) thread id
#
#         CAREFUL: this function is executed in the context of the caller
#         thread, to get the identity of the thread represented by this
#         instance.
#         """
#         if not self.isAlive():
#             raise threading.ThreadError("the thread is not active")
#
#         # do we have it cached?
#         if hasattr(self, "_thread_id"):
#             return self._thread_id
#
#         # no, look for it in the _active dict
#         # for tid, tobj in threading._active.items():
#         #     if tobj is self:
#         #         self._thread_id = tid
#         #         return tid
#         return self.ident
#         # TODO: in python 2.6, there's a simpler way to do: self.ident
#
#         #raise AssertionError("could not determine the thread's id")
#
#     def raiseExc(self, exctype):
#         """Raises the given exception type in the context of this thread.
#
#         If the thread is busy in a system call (time.sleep(),
#         socket.accept(), ...), the exception is simply ignored.
#
#         If you are sure that your exception should terminate the thread,
#         one way to ensure that it works is:
#
#             t = ThreadWithExc( ... )
#             ...
#             t.raiseExc( SomeException )
#             while t.isAlive():
#                 time.sleep( 0.1 )
#                 t.raiseExc( SomeException )
#
#         If the exception is to be caught by the thread, you need a way to
#         check that your thread has caught it.
#
#         CAREFUL: this function is executed in the context of the
#         caller thread, to raise an exception in the context of the
#         thread represented by this instance.
#         """
#         _async_raise(self._get_my_tid(), exctype)
#
# class accionNueva(StoppableThread):
#     def run(self):
#         contador=0
#         while(True):
#             contador+=1
#             print("Hilo c=",contador)

# hilo=accionNueva()
# hilo.start()
# print("siguio a start")
# for i in range(10):
#     print("i=",i)
# print("se intenta detener el hilo")
# hilo.stop()
# for j in range(10):
#     print("j=",j)
# print(hilo.stopped())
# hilo.raiseExc(Exception("para detenerlo"))

# def accion(arg):
#     print("entro al hilo")
#     contador = 0
#     while (True):
#         contador += 1
#         print("Hilo c=", contador)
# import multiprocessing
# proc = multiprocessing.Process(target=accion, args=("",))
# proc.start()
# for i in range(10):
#     print("i=",i)
# print("se intenta detener el hilo")
# # Terminate the process
# proc.terminate()

#
# from multiprocessing import Process
#
# def f(name):
#     print('hello', name)
#     print("entro al hilo")
#     contador = 0
#     while (True):
#     # for i in range(100):
#         contador += 1
#         print("Hilo c=", contador)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     c=threading.Condition()
#     c.acquire()
#     c.wait(4)
#     for i in range(100):
#         print("!!!!!!!!!!!!!!!!!!!!!!!    i=",i)
#     print("va a deternlo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     #p.join()
#     p.terminate()

# BDConexion.new_BDConexionSQLite("nuevo")
# def accion():
#     print("Se ejecuto en ",Date())
# job=executeTodosLos(accion,horas=19,minutos=10)
#
# print("sigue")
#
#
#
# while True:
#     algo = input("pon los segundos")
#     print(algo)
#     #job.modificar(segundos=algo)
#     print(job.proximaEjecucion())
#     t=job.proximaEjecucion().sub(Date())
#     print(t.strTime())
#     print(t.getHora(),":",t.getMinutos()," h")

# print(Date(hora=4,minuto=30).add(Date(hora=8)).strTime())
# print(Date(dia=1,hora=4,minuto=30).sub(Date(hora=18,minuto=30)).strTime())
# d=Date()
# d.set(hora=4,minuto=30)
# compilarAllPy(urlProyectoACompilar=[
#     r"D:\_Cosas\Programacion\Proyectos\Python\para compilar\DeProyectoBot\sin compilar\BotInve"
#     ,r"D:\_Cosas\Programacion\Proyectos\Python\para compilar\DeProyectoBot\sin compilar\RenePython"
#     ,r"D:\_Cosas\Programacion\Proyectos\Python\para compilar\DeProyectoBot\sin compilar\ReneTelegramBot"]
#               ,urlCarpetaSalida=r"D:\_Cosas\Programacion\Proyectos\Python\para compilar\DeProyectoBot\compilado\ConjuntoProyectoBot"
# ,vercionPy="36")

# def accion(f:File,indice):
#     nombre="2_"+str(indice)+".jpg"
#     if f.getName()!=nombre:
#         f.rename(nombre)
# Archivo.recorrerArchivosExternos(r"D:\_Cosas\Programacion\Proyectos\Python\IA\img\originales\guayaba\2",accion)
# print("Termino")

# a="_ , * , [ , ] , ( , ) , ~ , ` , > , # , + , - , = , | , { , } , . , !"
# b="["
# a=a.split(" , ")
# for i in a:
#     b+="\""+i+"\",r\"\\"+i+"\","
# b+="]"
# print(b)



# import io
# import re
# from re import Pattern
#patron = re.compile(r"[<][{](.*)[}][>]=[<][{](.*)")
#patron = re.compile("COLUMNA_ID_TABLA_USUARIO")
# texto="<{COLUMNA_ID_TABLA_USUARIO}>=<{1}> <{COLUMNA_ID_TELEGRAM}>=<{1564402609}> <{COLUMNA_USERNAME}>=<{Anto}> <{FIRST_NAME}>=<{first}> <{LAST_NAME}>=<{last}> "
# lista=texto.split("}> ")
# for t in lista:
#     print(t)
#     re = patron.findall(t)
#     for l in re:
#         print("l:",l)
# import sqlite3
#
# import codecs
# import binascii


# def esUnHashCorrectoEnTransaccion_USDT_BET20(supuestoHash):
#     patron=re.compile("^exprecion que necesito$")
#     return re.match(patron,supuestoHash)!=None

# fecha=Date()
# for i in range(10):
#     fecha=fecha.add(dias=1)
#     print(fecha)

# class asd():
#     def saludar(self):
#         print("hola")
#     def sobreescribirSaludar(self):
#         def saludar2():
#             print("sobreescrito")
#         self.saludar=saludar2


# bd=BDConexion.new_BDConexionSQLite("bdBotTelegram.sqlite")
# #bd.crearTablaYBorrarSiExiste("TABLA_FOTO","COLUMNA_DATA",TipoDeDatoSQL.BLOB,"COLUMNA_NOMBRE")
# data=Archivo.readBinaryData(r"C:\Users\Rene\Pictures\codeMas.png")
#
# print("asd".encode("utf-16").hex())
#
# print(bytes.fromhex("asd".encode("utf-16").hex()).decode("utf-16"))

# print(data.hex())
# print("---------------")
#
# print(bytes.fromhex(data.hex()))
# print("---------------")
# print(data)


#print(codecs.utf_16_be_encode(data.hex()))
# a=""+binascii.hexlify(data)
#print(binascii.hexlify(data))



# bd.insertar("TABLA_FOTO",codecs.decode(data, 'hex_codec'),"codemas3")
#
# data2=bd.select_Where("TABLA_FOTO","COLUMNA_NOMBRE","codemas3")[0][1]
# data2=bytes.fromhex(data.hex())
# Archivo.writeBinaryData(data2,r"C:\Users\Rene\Desktop\Nueva carpeta\Nueva carpeta (12)\imgNueva.png")
#

# A1=15
# B2=24
# C2=54
# D2=67
# COLUMNA_RESULTADO=-1
#
# if A1>0.416:
#     COLUMNA_RESULTADO=(B2*86400)*C2
# else:
#     COLUMNA_RESULTADO=(D2*86400)*C2
#
#
# print(COLUMNA_RESULTADO)

# class Equipo:
#
#     def __init__(self,codigo,concepto,cantidad):
#         self.codigo = codigo
#         self.concepto = concepto
#         self.cantidad = cantidad
#     def __str__(self):
#         return 'Codigo: {} | Concepto: {} | Cantidad: {}'.format(self.codigo,self.concepto,self.cantidad)
#
# nombres = ['Juan', 'Laura', 'Pepe']
# edades = [42, 40, 37]
# cantidades = [1,2,3]
#
#
# df = pd.DataFrame()
# df['Nombre'] = nombres
# df['Edad'] = edades
# df['Cantidad'] = cantidades
#
# lista1 = []
# for i in df.index:
#     e = Equipo(df['Nombre'][i],df['Edad'][i],df['Cantidad'][i])
#     k.append(e)
#
#
#
# from telegram.utils import helpers
# def enviarMensajeConElLinkDeReferencia(update,context):
#     bot = context.bot
#     user = update.effective_message.from_user
#     link=helpers.create_deep_linked_url(bot.username, str(user.id))
#     #Link de referencia de la forma: https://t.me/Tu_Bot?start=XXXXXXXXXX
#     update.message.reply_text("Su link propio es"+str(link))
#
# import re
# from telegram.ext import CommandHandler
# from telegram.ext import Filters
#
# #... Se instancia el updater y el dispatcher
#
# def accionEnStart(update,context):
#     idUsuarioDeTelegramDePatrocinador=context.args[0]
#     update.message.reply_text("Tu patrocinador es " + str(idUsuarioDeTelegramDePatrocinador))
#
#
# dispatcher.add_handler(CommandHandler("start", accionEnStart, Filters.regex("([0-9]{10})")))


# print(strg("hola",2))
# """
# CREATE TABLE "Aplicacion_fruto" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Nombre" varchar(50) NOT NULL, "Tipo" varchar(50) NOT NULL, "UltimaModificacion" datetime NOT NULL, "Descripcion" text NOT NULL)
# CREATE TABLE "Aplicacion_modeloneuronal" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Nombre" varchar(50) NOT NULL, "Tipo" varchar(50) NOT NULL, "UltimaModificacion" datetime NOT NULL, "Descripcion" text NOT NULL, "Fruto_id" bigint NOT NULL REFERENCES "Aplicacion_fruto" ("id") DEFERRABLE INITIALLY DEFERRED, "User_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "Direccion" varchar(256) NOT NULL)
# """
# bd=BDConexion.new_BDConexionSQLite("D:\_Cosas\Programacion\Proyectos\Python\Django 3.1\ProyectoPCChar\db.sqlite3")
# bd.insertar("Aplicacion_fruto","Fruta bomba","Maradol Roja","2022-02-09 00:28:38.636773","""Instituto Nacional de Investigaciones
# Fundamentales de  la Agricultura Tropical""")
# bd.insertar("Aplicacion_fruto","Guayaba","Enana Roja EEA1-23","2022-02-09 00:29:05.342949","""Estación Experimental de
# Alquizar Hibrido 1-23
# """)
# bd.insertar("Aplicacion_modeloneuronal","D:\_Cosas\Programacion\Proyectos\Python\PyQt6\Prueba2\modeloFrutbaBomba70.h5"
#             ,"modeloFrutbaBomba70","Modelo Tensor flow","2022-02-09 23:52:35.298272","simple","1","1")
# bd.insertar("Aplicacion_modeloneuronal","D:\_Cosas\Programacion\Proyectos\Python\PyQt6\Prueba2\modeloGuayaba60.h5"
#             ,"modeloGuayaba60","Modelo Tensor flow","2022-02-09 23:54:10.145664","simple","2","1")
# bd.insertar("Aplicacion_modeloneuronal","D:\_Cosas\Programacion\Proyectos\Python\PyQt6\Prueba2\modeloFrutbaBomba.h5"
#             ,"modeloFrutbaBomba","Modelo Tensor flow","2022-02-09 23:55:54.071075","otro","1","1")
# for i in range(1,4):
#     O=list(bd.select_forID("Aplicacion_modeloneuronal",str(i)))
#     bd.delete_id("Aplicacion_modeloneuronal",i)
#     direccion=O[-1]
#     O.remove(direccion)
#     O.insert(1,direccion)
#
#     bd.insertar("Aplicacion_modeloneuronal",*tuple(O))
print("")
