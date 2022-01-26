import pyglet
from pyglet.gl import gl

width = 1000
height = 700

ball_size = 20
ball_speed = 200

width_palka = 10
height_palka = 100
palka_speed = ball_speed * 1.5

mid_line_width = 20

font_size = 42
odsadenie_textu = 30

pozicia_palok = [height // 2, height // 2]
pozicia_lopty = [width // 2, height // 2]
rychlost_lopty = [0, 0]
stisknutie_klavesy = set()
skore = [0, 0]


def vykresli_obdlznik(x1, y1, x2, y2):
    gl.glBegin(pyglet.gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()
def vykresli():
    gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1, 1, 1)

vykresli_obdlznik(
    pozicia_lopty[0] - ball_size // 2,
    pozicia_lopty[1] - ball_size // 2,
    pozicia_lopty[0] - ball_size // 2,
    pozicia_lopty[1] - ball_size // 2
)
def nakresli_text(text, x, y, pozicia_x):
    napis = pyglet.text.Label(text, font_size = font_size, x = x, y = y, anchor_x = pozicia_x)
    napis.draw()
for x, y in [(0, pozicia_palok[0]), (width, pozicia_palok[1])]:
    vykresli_obdlznik(
        x - width_palka,
        y - height_palka // 2,
        x + width_palka,
        y + height_palka // 2
    )
for y in range(mid_line_width // 2, height, mid_line_width * 2):
    vykresli_obdlznik(
        width // 2 - 1,
        y,
        width // 2 + 1,
        y + mid_line_width
    )



nakresli_text(str(skore[0]), x = odsadenie_textu, y = height-odsadenie_textu-font_size, pozicia_x="left")
nakresli_text(str(skore[1]), x = width-odsadenie_textu, y = height-odsadenie_textu-font_size, pozicia_x="right")


window = pyglet.window.Window(width = width, height = height)
window.push_handlers(
    on_draw = vykresli
)

pyglet.app.run()