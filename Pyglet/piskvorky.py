import pyglet
from pyglet.gl import gl
from pyglet.window import mouse

width = 600
height = 600

#vytvori okno
window = pyglet.window.Window(width=600, height=600)

#definujem dlzku ciar do premennych
def ciary(x1, y1, x2, y2):
    gl.glBegin(pyglet.gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x1, y2)
    gl.glVertex2f(x2, y2)
    gl.glVertex2f(x2, y1)
    gl.glEnd()
"""
label1 = pyglet.text.Label("lavy", x=300, y=300)
label2 = pyglet.text.Label("pravy", x=300, y=300)
"""
#toto nakresli mriezku
def nakresli():
    gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(0, 255, 0)
    ciary(width / 3 - 5, 0, width / 3 + 5, height)
    ciary(width / 3 * 2 - 5, 0, width / 3 * 2 + 5, height)
    ciary(0, height / 3 - 5, width, height / 3 + 5)
    ciary(0, height / 3 * 2 - 5, width, height / 3 * 2 + 5)

def stlac_mys(x, y, tlacitko, modifikatory):
    if tlacitko == mouse.LEFT:
        print("lavy")
    if tlacitko == mouse.RIGHT:
        print("pravy")
    if tlacitko == mouse.MIDDLE:
        print("stredny")


#toto je to co to ma urobit
window.push_handlers(
    on_draw=nakresli,
    on_mouse_press=stlac_mys
)

#program zacne bezat
pyglet.app.run()
