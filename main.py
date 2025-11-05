import flet as ft
from login import VisuLogin
from home import VisuHome
from cadastro import VisuCadastro

def main(page: ft.Page):
    def Rota(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(VisuLogin(page))
        elif page.route == "/Home":
            page.views.append(VisuHome(page))
        elif page.route == "/Cadastro":
            page.views.append(VisuCadastro(page))
        page.update()
    
    page.on_route_change = Rota
    page.go("/")
ft.app(target=main)