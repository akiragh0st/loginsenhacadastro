import flet as ft
import re
def VisuLogin(page: ft.Page):
    page.window.min_width = 320  
    page.window.max_width = 500  
    page.window.min_height = 500  
    page.window.max_height = 800  
    page.window.height = 800
    page.window.width = 500
    usuarioemail_login = ft.TextField(label="Usuario ou Email", width= 300)
    Senha_login = ft.TextField(label="Senha", width= 300, password= True, can_reveal_password= True)
    botão_login = ft.ElevatedButton("Entrar", on_click=lambda _:page.go('/home'))
    botão_cadastro = ft.ElevatedButton("Cadastro", on_click = lambda _:page.go('/cadastro'))



    def entra_na_conta(e):
        if not usuarioemail_login.value.strip() or not usuarioemail_login.strip() or not Senha_login.value.strip():
            page.open(ft.SnackBar(ft.Text("⚠️ Todos os campos devem ser preenchidos!"), bgcolor="RED"))
            return
         
        if not re.match(usuarioemail_login,usuarioemail_login.value.strip()):
                page.open(ft.SnackBar(ft.Text("👎 E-mail inválido!"), bgcolor="RED"))
                return
    botão_login = ft.TextButton("entrando na sua conta", on_click=entra_na_conta)
        
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
                spacing=15  
            ),
        ],
        vertical_alignment="center", 
        horizontal_alignment="center"
    )
