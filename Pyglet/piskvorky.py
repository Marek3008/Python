import random
import pyglet
from pyglet.gl import gl



#definujem dlzku ciar do premennych
def ciary(x1, y1, x2, y2):
    gl.glBegin(pyglet.gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x1, y2)
    gl.glVertex2f(x2, y2)
    gl.glVertex2f(x2, y1)
    gl.glEnd()

#nakresli mriezku
def nakresli():
    gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(0, 255, 0)
    ciary(195, 0, 205, 600)
    ciary(395, 0, 405, 600)
    ciary(0, 195, 600, 205)
    ciary(0, 395, 600, 405)

def stlac_mys():
    pass
#vytvori okno
window = pyglet.window.Window(width=600, height=600)
#toto je to co to ma urobit
window.push_handlers(
    on_draw=nakresli,
    #on_mouse_press=
)
#program zacne bezat
pyglet.app.run()