import flet as ft

def VisuHome(page: ft.Page):
    texto = ft.Text("Home")
    voltar = ft.ElevatedButton("Voltar", on_click=lambda _:page.go('/'))

    return ft.View(
        route = "/",
        controls = [texto, voltar
                    ],
                    vertical_alignment= "center",
                    horizontal_alignment= "center"
    )