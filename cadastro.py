import flet as ft

def VisuCadastro(page: ft.Page):
    # Definindo tema e alinhamento da página
    page.theme_mode = ft.ThemeMode.LIGHT  # Tema claro
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.min_width = 320  # Mínimo de largura para dispositivos móveis
    page.window.max_width = 500  # Máximo de largura
    page.window.min_height = 500  # Mínimo de altura
    page.window.max_height = 800  # Máximo de altura
    page.window.height = 800
    page.window.width = 500
    
    # Definindo os controles
    usuario = ft.TextField(label="Nome de usuário", width=300, prefix=ft.Icon(ft.Icons.PERSON, size= 16))
    email_login = ft.TextField(label="Digite seu e-mail", width=300, prefix=ft.Icon(ft.Icons.EMAIL, size= 16))
    Senha_Cadastro = ft.TextField(label="Crie uma senha", width=300, password=True, can_reveal_password=True, prefix=ft.Icon(ft.Icons.KEY, size= 16))
    Senha_Cadastro_confirme = ft.TextField(label="Confirme a senha", width=300, password=True, can_reveal_password=True, prefix=ft.Icon(ft.Icons.KEY_OFF, size= 16))
    icone = ft.Icon(ft.Icons.PERSON, size = 40)
    
    # Botões de ação
    botão_cadastro = ft.TextButton("Criar uma conta", on_click=lambda _: page.go('/home'))
    botão_login = ft.TextButton("Tem uma conta?", on_click=lambda _: page.go('/'))
    
    # Colocando os campos em uma coluna para alinhamento vertical
    return ft.View(
        route='/Cadastro',
        controls=[
            ft.Column(
                controls=[
                    icone,
                    usuario,
                    email_login,
                    Senha_Cadastro,
                    Senha_Cadastro_confirme,
                    # Row com os botões lado a lado
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
