from pathlib import Path
from tkinter import Button, Canvas, Entry, PhotoImage, Tk, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r'C:\Users\GuiJu\Workspace\APS_BIOMETRIA\projeto-biometria\assets\frame0'
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class ButtonFunctions:
    def NovaConta(self):
        self.message_box = messagebox.askyesno()


button_functions = ButtonFunctions()

window = Tk()


class LoginScreen(ButtonFunctions):
    def __init__(self):
        self.window = window
        self.tela()
        self.incia_componentes()
        window.mainloop()

    # Criação da Janela e componentes
    def tela(self):
        self.window.title('Ministerio do Meio Ambiente - Login')
        self.window.geometry('700x550')
        self.window.configure(bg='#FFFFFF')
        self.window.resizable(False, False)

    def incia_componentes(self):
        # Canvas Principal
        self.canvas = Canvas(
            window,
            bg='#FFFFFF',
            height=550,
            width=700,
            bd=0,
            highlightthickness=0,
            relief='ridge',
        )
        self.canvas.place(x=0, y=0)
        # Imagem fundo
        self.imagem_imagem_fundo = PhotoImage(
            file=relative_to_assets('image_fundo.png')
        )
        self.imagem_fundo = self.canvas.create_image(
            350.0, 275.0, image=self.imagem_imagem_fundo
        )
        # Imagem do GOV
        self.imagem_imagem_gov = PhotoImage(
            file=relative_to_assets('image_gov.png')
        )
        self.image_gov = self.canvas.create_image(
            600.5282287597656, 492.2825622558594, image=self.imagem_imagem_gov
        )
        # Imagem da Logo
        self.imagem_imagem_logo = PhotoImage(
            file=relative_to_assets('image_logo.png')
        )
        self.image_logo = self.canvas.create_image(
            170.0, 47.0, image=self.imagem_imagem_logo
        )
        # Texto principal - Ministerio
        self.canvas.create_text(
            195.0,
            42.0,
            anchor='nw',
            text='MINISTERIO DO MEIO AMBIENTE',
            fill='#1E1E1E',
            font=('Poppins ExtraBold', 20 * -1),
        )
        # Area do formulario
        self.canvas.create_rectangle(
            214.0, 110.0, 487.0, 504.0, fill='#EFEFEF', outline='#DDDDDD'
        )
        # Insert e Icon Login
        self.image_icon_user = PhotoImage(
            file=relative_to_assets('icon_user.png')
        )
        self.icon_user = self.canvas.create_image(
            245.0452880859375, 140.5, image=self.image_icon_user
        )
        self.canvas.create_text(
            253.0,
            132.0,
            anchor='nw',
            text='Login',
            fill='#000000',
            font=('Poppins Regular', 13 * -1),
        )
        self.entry_image_login = PhotoImage(
            file=relative_to_assets('entry_small.png')
        )
        self.entry_bg_login = self.canvas.create_image(
            350.5, 175.5, image=self.entry_image_login
        )
        self.entry_login = Entry(
            bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0
        )
        self.entry_login.place(
            x=244.80000019073486,
            y=158.0,
            width=211.39999961853027,
            height=33.0,
        )
        # Insert e Icon de Senha
        self.image_icon_key = PhotoImage(
            file=relative_to_assets('icon_key.png')
        )
        self.icon_key = self.canvas.create_image(
            244.00000762939453, 220.5, image=self.image_icon_key
        )
        self.canvas.create_text(
            252.9547119140625,
            214.0,
            anchor='nw',
            text='Senha',
            fill='#000000',
            font=('Poppins Regular', 13 * -1),
        )
        self.entry_image_senha = PhotoImage(
            file=relative_to_assets('entry_small.png')
        )
        self.entry_bg_senha = self.canvas.create_image(
            349.5782012939453, 258.9906311035156, image=self.entry_image_senha
        )
        self.entry_senha = Entry(
            bd=0, bg='#FFFFFF', fg='#000716', highlightthickness=0
        )
        self.entry_senha.place(
            x=243.87820148468018,
            y=241.49063110351562,
            width=211.39999961853027,
            height=33.0,
        )
        # Botão 'Esqueci minha senha'
        self.button_image_esqueci = PhotoImage(
            file=relative_to_assets('button_esqueci.png')
        )
        self.button_esqueci = Button(
            image=self.button_image_esqueci,
            borderwidth=0,
            highlightthickness=0,
            relief='flat',
            command=button_functions.NovaConta,
        )
        self.button_esqueci.place(
            x=239.0452880859375, y=282.4906311035156, width=107.0, height=15.0
        )
        # Botão de Entrar
        self.button_image_entrar = PhotoImage(
            file=relative_to_assets('button_entrar.png')
        )
        self.button_entrar = Button(
            image=self.button_image_entrar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('button_2 clicked'),
            relief='flat',
        )
        self.button_entrar.place(
            x=238.0, y=320.04449462890625, width=225.0, height=35.0
        )
        # Botão da Digital
        self.button_image_digital = PhotoImage(
            file=relative_to_assets('button_digital.png')
        )
        self.button_digital = Button(
            image=self.button_image_digital,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('button_1 clicked'),
            relief='flat',
        )
        self.button_digital.place(
            x=316.0, y=385.70574951171875, width=68.0, height=77.0
        )
        # Botão Criar Conta
        self.button_image_criarconta = PhotoImage(
            file=relative_to_assets('button_criarconta.png')
        )
        self.button_criarconta = Button(
            image=self.button_image_criarconta,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('button_4 clicked'),
            relief='flat',
        )
        self.button_criarconta.place(
            x=616.0,
            y=12.34405517578125,
            width=64.0,
            height=46.65594482421875,
        )


LoginScreen()
