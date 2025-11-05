import flet as ft

def VisuLogin(page: ft.Page):
    page.window.min_width = 320  # Mínimo de largura para dispositivos móveis
    page.window.max_width = 500  # Máximo de largura para garantir que seja adaptável
    page.window.min_height = 500  # Minimo de altura
    page.window.max_height = 800  # Máximo de altura
    page.window.height = 800
    page.window.width = 500
    usuarioemail_login = ft.TextField(label="Usuario ou Email", width= 300)
    Senha_login = ft.TextField(label="Senha", width= 300, password= True, can_reveal_password= True)
    botão_login = ft.ElevatedButton("Entrar", on_click=lambda _:page.go('/home'))
    botão_cadastro = ft.ElevatedButton("Cadastro", on_click = lambda _:page.go('/cadastro'))

    
    return ft.View(
        route='/Cadastro',
        controls=[
            ft.Column(
                controls=[
                    usuarioemail_login,
                    Senha_login,
                    ft.Row(
                        controls=[
                            botão_cadastro,
                            botão_login,
                        ],
                        alignment="center",  # Alinha os botões horizontalmente no centro
                        spacing=20  # Espaçamento entre os botões
                    ),
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=15  # Adiciona um espaçamento entre os campos de entrada
            ),
        ],
        vertical_alignment="center", 
        horizontal_alignment="center"
    )
