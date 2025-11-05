import flet as ft

def VisuLogin(page: ft.Page):
    page.theme_mode = "white"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    usuarioemail_login = ft.TextField(label="Usuario ou Email", width= 300)
    Senha_login = ft.TextField(label="Senha", width= 300, password= True, can_reveal_password= True)
    botão_login = ft.ElevatedButton("Entrar")
    botão_cadastro = ft.ElevatedButton("Não tem uma conta?", on_click = lambda _:page.go('/Cadastro'))
    botão_home = ft.ElevatedButton("Voltar para a tela inicial", on_click = lambda _:page.go('/'))
    return ft.View(
        route = '/Login',
        controls= [
            usuarioemail_login, 
            Senha_login,
            botão_cadastro,
            botão_login,
            botão_home,
        ], vertical_alignment="CENTER", 
        horizontal_alignment="CENTER"
    )
