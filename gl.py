#Autor: Mariana David
#Carne: 201055


#importacion modulos
import struct 

def char(c): 
    #1 byte char
    return struct.pack('=c', c.emcpde('ascii'))

def word(w):
    #2bytes
    return struct.pack('=h', w)

def dword(d):
    #4 bytes
    return struct.pack('=l', d)

def color(r,g,b):
    return bytes([int(b * 225),
                int(g * 225),
                int(r * 225)])
    

class Render(object):
    #glInit
    def __init__(self,width, height):

        self.width = width
        self.height = height

        self.clearColor = color (0,0,0)
        self.currColor = color (1,1,1)

        self.glClear()
	
    def glCreateWindow(self, width, height):
        #glCreateWindows (dimension de la imagen)
        self.width = width
        self.height = height
        self.glClear()
    

    def glViewPort(self, x, y, width, height):
        #glViewPort (define area)
        self.viewPortX = x
        self.viewPortY = y
        self.viewPortWidth = width
        self.viewPortHeight = height
        self.drawVPS()

        
    def drawVPS(self):
        # Función para dibujar el cuadrado del viewPort
        for x in range(self.viewPortX, self.viewPortX + self.viewPortWidth):
            for y in range(self.viewPortY, self.viewPortY + self.viewPortHeight):
                self.pixels[x][y] = self.currColor
        

    def glClearColor(self, r, g, b):
        #glCreateWindow (r,g,b)
        self.clearColor= color(r,g,b)

    def glColor(self, r, g, b):
        #glPoint (r,g,b)
        self.currColor = color(r,g,b)

    def glClear(self):
        #glClear
        self.pixels = [[self.clearColor for y in range(self.height)] for x in range(self.width)]

    def glPoint (self, x, y, clr = None):
        #glPoint (x,y)
        if (0 < x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor

    def glFinish(self, filename):
        #glFinish
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 +40))

            #InfoHeader 
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            #Color table 
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])