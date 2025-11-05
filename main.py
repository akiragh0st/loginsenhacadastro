import flet as ft
from login import VisuLogin
from home import VisuHome
from cadastro import VisuCadastro

def main(page: ft.Page):
    # Configura o tamanho da janela uma única vez
    page.window.min_width = 320  # Mínimo de largura para dispositivos móveis
    page.window.max_width = 500  # Máximo de largura para garantir que seja adaptável
    page.window.min_height = 500  # Minimo de altura
    page.window.max_height = 800  # Máximo de altura
    page.window.height = 800
    page.window.width = 500
    # Função que trata a navegação entre as páginas
    def Rota(e):
        # Limpa a lista de views e adiciona a nova conforme a rota
        page.views.clear()
        
        # Adiciona a view correspondente à rota
        if page.route == "/":
            page.views.append(VisuLogin(page))
        elif page.route == "/home":
            page.views.append(VisuHome(page))
        elif page.route == "/cadastro":
            page.views.append(VisuCadastro(page))
        
        # Atualiza a página para refletir a mudança
        page.update()
    
    # Define o evento que dispara quando a rota é alterada
    page.on_route_change = Rota

    # Redireciona para a página inicial ao iniciar
    page.go("/")
    
# Inicia o aplicativo
ft.app(target=main)
