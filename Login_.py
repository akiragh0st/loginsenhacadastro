import flet as ft

def main(page: ft.Page):
    page.theme_mode = "white"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    def click_cadastro(route):
        usuario_cadastro = ft.TextField(label="Nome de usuario", width= 300)
        email_cadastro = ft.TextField(label="Digite seu email")
        Senha_cadastro = ft.TextField(label="Digite sua senha", width= 300, password= True, can_reveal_password= True)
        page.update   
    
    usuarioemail_login = ft.TextField(label="Usuario ou Email", width= 300)
    Senha_login = ft.TextField(label="Senha", width= 300, password= True, can_reveal_password= True)
    botão_login = ft.ElevatedButton("Entrar")
    botão_cadastro = ft.ElevatedButton("Não tem uma conta?", on_click= click_cadastro)
    
    page.add(ft.Row([usuarioemail_login], alignment = "center"),
            ft.Row([Senha_login], alignment = "center"),
            ft.Row([botão_login], alignment = "center"), botão_cadastro)
ft.app(target = main)
