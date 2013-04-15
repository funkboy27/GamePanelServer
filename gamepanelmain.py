from Tkinter import *
from twisted.internet import tksupport, reactor
import SendKeys
from twisted.internet.protocol import Factory, Protocol
import time
import sys
from sys import exit

class MyApp(object):
  def __init__(self, reactor,parent):
    self.myParent = parent   
    self.myContainer1 = Frame(parent)
    self.myContainer1.pack()
    
    self.button1 = Button(self.myContainer1, command=self.button1Click)  
    self.button1.bind("<Return>", self.button1Click_a)    
    self.button1.configure(text="Start Server")
    self.button1.pack(side=LEFT)
    self.button1.focus_force()       
    
    self.button2 = Button(self.myContainer1, command=self.button2Click)   
    self.button2.bind("<Return>", self.button2Click_a)    
    self.button2.configure(text="Quit")     
    self.button2.pack(side=RIGHT)
    
  def button1Click(self):  
    #print "button1Click event handler" 
    self.button1["background"] = "yellow"
    import select
    import sys
    import pybonjour

    name    = 'simpleserver'
    regtype = '_server._tcp'
    port    = 3333
##name    = sys.argv[1]
##regtype = sys.argv[2]
####port    = int(sys.argv[3])


    def register_callback(sdRef, flags, errorCode, name, regtype, domain):
        if errorCode == pybonjour.kDNSServiceErr_NoError:
            print 'Registered service:'
            print '  name    =', name
            print '  regtype =', regtype
            print '  domain  =', domain
    sdRef = pybonjour.DNSServiceRegister(name = name,
                                   regtype = regtype,
                                   port = port,
                                   callBack = register_callback)


    class IphoneChat(Protocol):
        def connectionMade(self):
            self.factory.clients.append(self)
            #print "clients are ", self.factory.clients

        def connectionLost(self, reason):
            self.factory.clients.remove(self)

        def dataReceived(self, data):
          a = data
          #print a
          if a == data:
#             import SendKeys
             SendKeys.SendKeys(a)         
             time.sleep(1)
#             reactor.run(installSignallHandlers=True)

        def message(self, message):
           self.transport.write(message)
    
    factory = Factory()
    factory.protocol = IphoneChat
    factory.clients = []
    reactor.listenTCP(3333, factory)
  
    
    
    
        
    self.button1["background"] = "green"
    
  def button2Click(self): 
    while True:
      try:
        #print "button2Click event handler" 
        self.myParent.destroy()
        root.mainloop.destroy()
      except Exception:
        pass
              
    #root.mainloop()
    
    
  
  def button1Click_a(self, event):  
    #print "button 1 Click event" 
    self.button1Click()
        
  def button2Click_a(self, event):  
    #print "button 2 Click event" 
    self.button2Click()
        


root = Tk()
tksupport.install(root)
myapp = MyApp(reactor, root)
reactor.run()
#root.mainloop.destroy()
    



 
    
  

  


  
