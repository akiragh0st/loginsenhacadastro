import flet as ft
from login import VisuLogin
from home import VisuHome
from cadastro import VisuCadastro

def main(page: ft.Page):
    page.window.min_width = 320  
    page.window.max_width = 500 
    page.window.min_height = 500  
    page.window.max_height = 800 
    page.window.height = 800
    page.window.width = 500
    def Rota(e):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(VisuLogin(page))
        elif page.route == "/home":
            page.views.append(VisuHome(page))
        elif page.route == "/cadastro":
            page.views.append(VisuCadastro(page))
        
        page.update()
    
    page.on_route_change = Rota

    page.go("/")
    
ft.app(target=main)

