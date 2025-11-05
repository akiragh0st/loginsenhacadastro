import flet as ft

def VisuCadastro(page: ft.Page):
    page.theme_mode = "white"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    usuario = ft.TextField(label="Nome de usuario", width= 300)
    email_login = ft.TextField(label="Digite seu email", width= 300)
    Senha_Cadastro = ft.TextField(label="Crie uma senha", width= 300, password= True, can_reveal_password= True)
    botão_cadastro = ft.ElevatedButton("Criar uma conta", on_click=lambda _:page.go('/Home'))
    botão_login = ft.ElevatedButton("Não tem uma conta?", on_click = lambda _:page.go('/'))
    return ft.View(
        route = '/Cadastro',
        controls= [
            usuario,
            email_login,
            Senha_Cadastro,
            botão_cadastro,
            botão_login,
        ], vertical_alignment="CENTER", 
        horizontal_alignment="CENTER"
    )
