import random


from pyglet.gl import gl
from pyglet.window import key
width = 1000
height = 700

ball_size = 20
ball_speed = 200

width_palka = 10
height_palka = 100
palka_speed = ball_speed * 1.5

speed = 200

mid_line_width = 20

font_size = 42
odsadenie_textu = 30

pozicia_palok = [height //2, height //2]
pozicia_lopty = [width //2, height //2]
rychlost_lopty = [0, 0]
stisknutie_klavesy = set()
skore = [0, 0]

def reset():
    pozicia_lopty[0] = width // 2
    pozicia_lopty[1] = height // 2

    if random.randint(0,1):
        rychlost_lopty[0] = speed
    else:
        rychlost_lopty[0] = -speed
    rychlost_lopty[1] = random.uniform(0,1)


def vykresli_obdlznik(x1, y1, x2, y2):
    gl.glBegin(pong.gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()

def vykresli():
    gl.glClear(pong.gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1, 1, 1)

    vykresli_obdlznik(
        pozicia_lopty[0] - ball_size //2,
        pozicia_lopty[1] - ball_size //2,
        pozicia_lopty[0] + ball_size //2,
        pozicia_lopty[1] + ball_size //2
    )

    for x, y in [(0, pozicia_palok[0]), (width, pozicia_palok[1])]:
        vykresli_obdlznik(
            x - width_palka,
            y - height_palka // 2,
            x + width_palka,
            y + height_palka // 2,
        )
    for y in range(mid_line_width // 2, height, mid_line_width * 2):
        vykresli_obdlznik(
            width // 2 - 1,
            y,
            width // 2 + 1,
            y + mid_line_width
        )


def nakresli_text(text, x, y, pozicia_x):
    napis = pong.text.Label(text, font_size = font_size, x = x, y = y, anchor_x=pozicia_x)
    napis.draw()
def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknutie_klavesy.add(("hore", 0))
    if symbol == key.S:
        stisknutie_klavesy.add(("dole", 0))
    if symbol == key.UP:
        stisknutie_klavesy.add(("hore", 1))
    if symbol == key.DOWN:
        stisknutie_klavesy.add(("dole", 1))

def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknutie_klavesy.discard(("hore", 0))
    if symbol == key.S:
        stisknutie_klavesy.discard(("dole", 0))
    if symbol == key.UP:
        stisknutie_klavesy.discard(("hore", 1))
    if symbol == key.DOWN:
        stisknutie_klavesy.discard(("dole", 1))


    nakresli_text(str(skore[0]), x=odsadenie_textu, y=height-odsadenie_textu-font_size,pozicia_x="left")
    nakresli_text(str(skore[1]), x=width-odsadenie_textu, y=height-odsadenie_textu-font_size, pozicia_x="right")

def obnov_stav(dt):
    for cislo_palky in (0,1):
        if ("hore", cislo_palky) in stisknutie_klavesy:
            pozicia_palok[cislo_palky] += palka_speed * dt
        if ("dole", cislo_palky) in stisknutie_klavesy:
            pozicia_palok[cislo_palky] -= palka_speed * dt
        #dolna zarazka
        if pozicia_palok[cislo_palky] < height_palka / 2:
            pozicia_palok[cislo_palky] = height_palka / 2
        #horna zarazka
        if pozicia_palok[cislo_palky] > height - height_palka / 2:
            pozicia_palok[cislo_palky] = height - height_palka / 2

    pozicia_lopty[0] += rychlost_lopty[0] * dt
    pozicia_lopty[1] += rychlost_lopty[1] * dt

    if pozicia_lopty[1] < ball_size//2:
        ball_speed[1] = abs(ball_speed[1])
    if pozicia_lopty[1] > height - ball_size//2:
        ball_speed[1] = -abs(ball_speed[1])

    palka_min = pozicia_lopty[1] - ball_size / 2 - height_palka / 2
    palka_max = pozicia_lopty[1] + ball_size / 2 - height_palka / 2

    #odraz zlava
    if pozicia_lopty[0] < width_palka + ball_size / 2:
        if palka_min < pozicia_palok[0] < palka_max:
            rychlost_lopty[0] = abs(rychlost_lopty[0])
        else:
            skore[1] += 1
            reset()

    #odraz sprava
    if pozicia_lopty[0] > width - (width_palka + ball_size / 2):
        if palka_min < pozicia_palok[1] < palka_max:
            ball_speed[0] = -abs(ball_speed[0])
        else:
            skore[0] += 1
            reset()
reset()
window = pong.window.Window(width = width, height = height)
window.push_handlers(
    on_draw = vykresli,
    on_key_press = stisk_klavesnice,
    on_key_release = pusti_klavesnice
)
pong.clock.schedule(obnov_stav)

pong.app.run()