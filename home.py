import flet as ft

def VisuHome(page: ft.Page):
    texto = ft.Text("Home")
    voltar = ft.ElevatedButton("Voltar", on_click=lambda _:page.go('/'))
    page.window.min_width = 320  # Mínimo de largura para dispositivos móveis
    page.window.max_width = 500  # Máximo de largura para garantir que seja adaptável
    page.window.min_height = 500  # Minimo de altura
    page.window.max_height = 800  # Máximo de altura
    page.window.height = 800
    page.window.width = 500
    
    return ft.View(
        route = "/home",
        controls = [texto, voltar
                    ],
                    vertical_alignment= "center",
                    horizontal_alignment= "center"
    )
