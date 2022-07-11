#Autor: Mariana David
#Carne: 201055


#importaciones
from gl import Render 

rend = Render(512, 512)

rend.glClearColor (0.45,0.30,0.50)
rend.glColor(0.177,0.30,0.4)
rend.glClear()

for i in range (512):
    rend.glPoint(i,i)

rend.glFinish("output.bmp")