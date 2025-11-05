import flet as ft

def VisuLogin(page: ft.Page):
    page.theme_mode = "white"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    usuarioemail_login = ft.TextField(label="Usuario ou Email", width= 300)
    Senha_login = ft.TextField(label="Senha", width= 300, password= True, can_reveal_password= True)
    botão_login = ft.ElevatedButton("Entrar", on_click=lambda _:page.go('/'))
    botão_cadastro = ft.ElevatedButton("Cadastro", on_click = lambda _:page.go('/Cadastro'))
    return ft.View(
        route = '/Login',
        controls= [
            usuarioemail_login, 
            Senha_login,
            botão_cadastro,
            botão_login,
        ], vertical_alignment="CENTER", 
        horizontal_alignment="CENTER"
    )

