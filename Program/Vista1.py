import wx
import re
from EstudianteController import addEstudiante
from EstudianteController import getLista
from EstudianteController import ModifyEstudiante
from EstudianteController import deleteEstudiante
from EstudianteController import consultarUno
from EstudianteController import generarEstudiante



class Vista1(wx.Frame):
    def __init__(self,*args,**kw):
        super(Vista1,self).__init__(*args,**kw)


        panel = wx.Panel(self)
        self.mensaje = ""

 #------------------------------- SECCIÓN MÉTODOS -----------------------------------------
  
            

        def verificarString(string):
            return bool(re.search(r'\d',string))

        def programMessage():
            wx.MessageBox(self.mensaje, caption='Mensaje del Programa',
                style= wx.OK|wx.CENTRE|wx.ICON_INFORMATION)

        def capturarDatos(event):
            nombre = self.tcNombre.GetValue()
            nota1 = int(self.tcNota1.GetValue())
            nota2 = int(self.tcNota2.GetValue())
            nota3 = int(self.tcNota3.GetValue())

            if nombre=='':
                 self.mensaje = 'Llene todos los campos'
                 programMessage()

            elif verificarString(nombre):                
                 self.mensaje = 'Solo numeros en la casilla nombre'
                 programMessage()

            else:
                 addEstudiante(nombre,nota1,nota2,nota3)
                 listar()
                 vaciar()                 
                 self.mensaje = 'Registro Exitoso'
                 programMessage()
                 
                   
        def listar():
            self.tabla.DeleteAllItems()
            lista = getLista()
            

            index = 0
            for row in lista:
                indice = str(row[0])
                self.tabla.InsertItem(index,indice)                
                self.tabla.SetItem(index,1,row[1])
                nota1 = str(row[2])
                self.tabla.SetItem(index,2,nota1)
                nota2 = str(row[3])
                self.tabla.SetItem(index,3,nota2)
                nota3 = str(row[4])
                self.tabla.SetItem(index,4,nota3)
                index += 1

        def modificar(event):
            indice = self.scModificar.GetValue()
            estudiante = consultarUno(indice)
            
            if estudiante!=None:
                self.tcNombre.SetValue(estudiante.nombre)
                self.tcNota1.SetValue(estudiante.nota1)
                self.tcNota2.SetValue(estudiante.nota2)
                self.tcNota3.SetValue(estudiante.nota3)
            else:
                self.mensaje = 'No se pude realizar la operación'
                programMessage()

            
        def vaciar():
            self.tcNombre.SetValue('')
            self.tcNota1.SetValue(0)
            self.tcNota2.SetValue(0)
            self.tcNota3.SetValue(0)
            
            
        def modificar2(event):
            if self.tcNombre.GetValue()!='':
                nombre = self.tcNombre.GetValue()
                nota1 = int(self.tcNota1.GetValue())
                nota2 = int(self.tcNota2.GetValue())
                nota3 = int(self.tcNota3.GetValue())
                indice = self.scModificar.GetValue()

                estudiante = generarEstudiante(nombre,nota1,nota2,nota3)
                ModifyEstudiante(indice,estudiante)            
                self.mensaje = 'Modificación exitosa'
                programMessage()
                vaciar()
                listar() 
            else:
                 self.mensaje = 'No se pudo realizar la operación'
                 programMessage()
                

        def eliminar(event):
            valor = self.tabla.GetItemCount()            
            indice = self.scEliminar.GetValue()
            deleteEstudiante(indice)
            listar()           
            if valor>self.tabla.GetItemCount():                
                self.mensaje = 'Borrado Exitoso'
                programMessage()
            else:
                self.mensaje = 'No se pudo realizar la operación'
                programMessage()    
            
            
        def refresar(event):
            listar()

        self.nota = ""
        def mostrarDefinitiva(event):
            indice = self.scConsultarDef.GetValue()
            estudiante = consultarUno(indice)
            if estudiante:                              
                nota1 = estudiante.nota1*0.30
                nota2 = estudiante.nota2*0.30
                nota3 = estudiante.nota3*0.40  
                notadef = nota1+ nota2 + nota3
                notadef = str(notadef)
                self.nota = "NOTA DEFINITVA "+notadef            
                wx.MessageBox(self.nota, caption='Mensaje del Programa',
                style= wx.OK|wx.CENTRE|wx.ICON_INFORMATION)
            else:
                self.nota = 'Operacion no realizada, verifique'       
                wx.MessageBox(self.nota, caption='Mensaje del Programa',
                style= wx.OK|wx.CENTRE|wx.ICON_INFORMATION)    

        
 #------------------------------- SECCIÓN MÉTODOS -----------------------------------------


 #------------------------------- SECCIÓN CREACIÓN -----------------------------------------
  
        self.title1 = wx.StaticText(panel,label='Registro Estudiante',pos=(50,10))
        

        self.stNombre = wx.StaticText(panel,label='Nombre',pos=(20,52))
        self.tcNombre = wx.TextCtrl(panel,pos=(100,45),size=(120,34))

        self.stNota1 = wx.StaticText(panel,label='Nota1',pos=(20,97))
        self.tcNota1 = wx.SpinCtrl(panel,pos=(100,90),size=(120,34),min=0,max=10,initial=0)
        
        self.stNota2 = wx.StaticText(panel,label='Nota2',pos=(20,142))
        self.tcNota2 = wx.SpinCtrl(panel,pos=(100,135),size=(120,34),min=0,max=10,initial=0)
        
        self.stNota3 = wx.StaticText(panel,label='Nota3',pos=(20,187))
        self.tcNota3 = wx.SpinCtrl(panel,pos=(100,180),size=(120,34),min=0,max=10,initial=0)

        self.btnAgregar = wx.Button(panel,label='Agregar',pos=(270,90),size=(120,25))
        self.btnModificar2 = wx.Button(panel,label='Modificar',pos=(270,140),size=(120,25))

        self.title2 = wx.StaticText(panel,label='OPCIONES',pos=(605,10))

        self.stEliminar = wx.StaticText(panel,label='Eliminar',pos=(480,50),size=(100,20))
        self.scEliminar = wx.SpinCtrl(panel,pos=(550,40),size=(130,34),min=1, max=100, initial=1)
        self.btnEliminar = wx.Button(panel,label='Eliminar',pos=(700,40), size=(90,35))

        self.stModificar = wx.StaticText(panel,label='Modificar',pos=(475,100),size=(100,20))
        self.scModificar = wx.SpinCtrl(panel,pos=(550,90),size=(130,34),min=1, max=100, initial=1)
        self.btnModificar = wx.Button(panel,label='Modificar',pos=(700,90), size=(90,35))
        
        self.stConsultarDef = wx.StaticText(panel,label='Consultar DEF',pos=(445,160),size=(100,20))
        self.scConsultarDef = wx.SpinCtrl(panel,pos=(550,150),size=(130,34),min=1, max=100, initial=1)
        self.btnConsultarDef = wx.Button(panel,label='Consultar Def',pos=(700,150), size=(100,35))

        self.title2 = wx.StaticText(panel,label='ESTUDIANTES',pos=(400,255))

        self.tabla = wx.ListCtrl(panel,pos=(25,280),size=(800,300),style=wx.LC_REPORT)
        self.tabla.InsertColumn(0,'ID',format=wx.LIST_FORMAT_LEFT,width=150)
        self.tabla.InsertColumn(1,'Nombre',format=wx.LIST_FORMAT_LEFT,width=200)
        self.tabla.InsertColumn(2,'Nota1',format=wx.LIST_FORMAT_LEFT,width=150)
        self.tabla.InsertColumn(3,'Nota2',format=wx.LIST_FORMAT_LEFT,width=150)
        self.tabla.InsertColumn(4,'Nota3',format=wx.LIST_FORMAT_LEFT,width=150)

        #self.refrescar = wx.Button(panel,label='Refrescar',size=(120,25),pos=(700,250))






        listar()    

 #------------------------------- SECCIÓN CREACIÓN -----------------------------------------





 #------------------------------- SECCIÓN BIND ---------------------------------------------
  
        self.btnAgregar.Bind(wx.EVT_BUTTON, capturarDatos)    
        self.btnEliminar.Bind(wx.EVT_BUTTON, eliminar)
        self.btnModificar.Bind(wx.EVT_BUTTON, modificar)
        self.btnModificar2.Bind(wx.EVT_BUTTON, modificar2)
        #self.refrescar.Bind(wx.EVT_BUTTON, refresar)
        self.btnConsultarDef.Bind(wx.EVT_BUTTON, mostrarDefinitiva)





 #------------------------------- SECCIÓN BIND -----------------------------------------------
