#pridam do kodu veci s ktorymi budem pracovat
import pyglet
from pyglet.gl import gl
from pyglet.window import mouse

#sirka, vyska
width = 600
height = 600

#vytvori okno, bez zadania width a height bude mat okno defaultne rozmery
window = pyglet.window.Window(width=width, height=height)

#definujem dlzku ciar a ked pouzijem tuto definiciu, tak namiesto pismen napisem cisla - suradnice, aby som to nemusel pisat dookola
def ciary(x1, y1, x2, y2):
    gl.glBegin(pyglet.gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x1, y2)
    gl.glVertex2f(x2, y2)
    gl.glVertex2f(x2, y1)
    gl.glEnd()

#toto nakresli mriezku (tu je pouzita definicia ciar a namiesto pismen su cisla, a usetril som cas a miesto takze kod je priehladnejsi)
def nakresli():
    gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(0, 0, 190)
    ciary(width / 3 - 5, 0, width / 3 + 5, height)
    ciary(width / 3 * 2 - 5, 0, width / 3 * 2 + 5, height)
    ciary(0, height / 3 - 5, width, height / 3 + 5)
    ciary(0, height / 3 * 2 - 5, width, height / 3 * 2 + 5)
    
#toto definuje stlacenie mysi a podmienky kedy sa co vykona
#je jedno ako si nazvem funkciu ale v atributoch musia byt tieto 4 veci pricom x,y su suradnice
def stlac_mys(x, y, tlacitko, modifikatory):
    if tlacitko == mouse.LEFT:
        print("lavy", x, y)
    if tlacitko == mouse.RIGHT:
        print("pravy", x, y)
    if tlacitko == mouse.MIDDLE:
        print("stredny", x, y)



#toto je to co to ma urobit 
#ak pouzijem @window.event tak veci ako on_draw atd zaradim do definicie
#za "=" su funkcie, ale zatvorky sa v tomto pripade za ne nedavaju pretoze potom to nebude fungovat
window.push_handlers(
    on_draw=nakresli,
    on_mouse_press=stlac_mys
)

#program zacne bezat
pyglet.app.run()