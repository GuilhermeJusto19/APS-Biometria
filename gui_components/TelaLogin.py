from pathlib import Path
from tkinter import Button, Canvas, Entry, PhotoImage, Text, Tk, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r'C:\Users\GuiJu\Workspace\APS_BIOMETRIA\projeto-biometria\assets\frame0'
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title('Ministerio do Meio Ambiente - Login')
window.geometry('700x550')
window.configure(bg='#FFFFFF')


class Button_Functions:
    def NovaConta(self):
        message_box = messagebox.askyesno()


button_functions = Button_Functions()

canvas = Canvas(
    window,
    bg='#FFFFFF',
    height=550,
    width=700,
    bd=0,
    highlightthickness=0,
    relief='ridge',
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets('image_1.png'))
image_1 = canvas.create_image(350.0, 275.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets('image_2.png'))
image_2 = canvas.create_image(
    600.5282287597656, 492.2825622558594, image=image_image_2
)

image_image_5 = PhotoImage(file=relative_to_assets('image_5.png'))
image_5 = canvas.create_image(170.0, 47.0, image=image_image_5)

canvas.create_rectangle(
    214.0, 110.0, 487.0, 504.0, fill='#EFEFEF', outline='#DDDDDD'
)

button_image_1 = PhotoImage(file=relative_to_assets('button_1.png'))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_1 clicked'),
    relief='flat',
)
button_1.place(x=316.0, y=385.70574951171875, width=68.0, height=77.0)

button_image_2 = PhotoImage(file=relative_to_assets('button_2.png'))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_2 clicked'),
    relief='flat',
)
button_2.place(x=238.0, y=320.04449462890625, width=225.0, height=35.0)

button_image_3 = PhotoImage(file=relative_to_assets('button_3.png'))
senha_esquecida_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=button_functions.NovaConta,
)
senha_esquecida_button.place(
    x=239.0452880859375, y=282.4906311035156, width=107.0, height=15.0
)

entry_image_1 = PhotoImage(file=relative_to_assets('entry_1.png'))
entry_bg_1 = canvas.create_image(350.5, 175.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0)
entry_1.place(
    x=244.80000019073486, y=158.0, width=211.39999961853027, height=33.0
)

canvas.create_text(
    252.9547119140625,
    214.0,
    anchor='nw',
    text='Senha',
    fill='#000000',
    font=('Poppins Regular', 13 * -1),
)

image_image_3 = PhotoImage(file=relative_to_assets('image_3.png'))
image_3 = canvas.create_image(244.00000762939453, 223.5, image=image_image_3)

entry_image_2 = PhotoImage(file=relative_to_assets('entry_2.png'))
entry_bg_2 = canvas.create_image(
    349.5782012939453, 258.9906311035156, image=entry_image_2
)
entry_2 = Entry(bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0)
entry_2.place(
    x=243.87820148468018,
    y=241.49063110351562,
    width=211.39999961853027,
    height=33.0,
)

canvas.create_text(
    253.0,
    132.0,
    anchor='nw',
    text='Login',
    fill='#000000',
    font=('Poppins Regular', 13 * -1),
)

image_image_4 = PhotoImage(file=relative_to_assets('image_4.png'))
image_4 = canvas.create_image(245.0452880859375, 140.5, image=image_image_4)

canvas.create_text(
    195.0,
    42.0,
    anchor='nw',
    text='MINISTERIO DO MEIO AMBIENTE',
    fill='#1E1E1E',
    font=('Poppins ExtraBold', 20 * -1),
)

button_image_4 = PhotoImage(file=relative_to_assets('button_4.png'))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_4 clicked'),
    relief='flat',
)
button_4.place(
    x=616.0, y=12.34405517578125, width=64.0, height=46.65594482421875
)


class Login_Screen(Button_Functions):
    def __init__(self):
        window.resizable(False, False)
        window.mainloop()


Login_Screen()
