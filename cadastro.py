import flet as ft
import os
import re
import cv2
import json

ARQUIVO_USUARIOS = "usuarios.json"
def ler_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def VisuCadastro(page: ft.Page):
    page.theme_mode = 'White'
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.min_width = 320
    page.window.max_width = 500
    page.window.min_height = 500
    page.window.max_height = 800
    page.window.height = 800
    page.window.width = 500

    usuario = ft.TextField(label="Nome de usuário", 
                           width=300, 
                           adaptive=True, 
                           prefix_icon=ft.Icon(ft.Icons.PERSON, size=30))
    email_login = ft.TextField(label="Digite seu e-mail", 
                               width=300, 
                               adaptive=True, 
                               prefix_icon=ft.Icon(ft.Icons.EMAIL, size=25))
    Senha_Cadastro = ft.TextField(label="Crie uma senha", 
                                  width=300, 
                                  adaptive=True, 
                                  password=True, can_reveal_password=True,
                                  prefix_icon=ft.Icon(ft.Icons.LOCK, size=25))
    Senha_Cadastro_confirme = ft.TextField(label="Confirme a senha", 
                                           width=300, adaptive=True, 
                                           password=True, can_reveal_password=True, 
                                           prefix_icon=ft.Icon(ft.Icons.LOCK, size=25))
    termoseserviço = ft.Checkbox()
    def tirar_foto(e):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            foto_path = "foto_perfil.jpg"
            cv2.imwrite(foto_path, frame)
            cam.release()
            page.snack_bar = ft.SnackBar(ft.Text("📸 Foto salva com sucesso!"))
            page.snack_bar.open = True
            page.update()
            a1.content = ft.Image(src=foto_path, fit=ft.ImageFit.COVER, width=120, height=120)
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("❌ Erro ao acessar a câmera!"))
            page.snack_bar.open = True
            page.update()

    def on_file_picked(result: ft.FilePickerResultEvent):
        if result.files:
            path = os.path.abspath(result.files[0].path)
            if os.path.exists(path):
                a1.content = ft.Image(src=path, fit=ft.ImageFit.COVER, width=120, height=120)
                page.update()

    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    def abrir_arquivo(e):
        file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["png", "jpg", "jpeg", "jfif"]
        )
        page.update()

    a1 = ft.Container(
        width=120,
        height=120,
        border_radius=ft.border_radius.all(60),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        bgcolor=ft.Colors.GREY_200,
        content=ft.Icon(ft.Icons.PERSON, size=50, color=ft.Colors.GREY_600),
    )

    def abrir_opcoes_camera(e):
        action_sheet = ft.CupertinoActionSheet(
            title=ft.Text("Escolher foto de perfil"),
            message=ft.Text("Selecione uma opção:"),
            actions=[
                ft.CupertinoActionSheetAction(
                    text="📷 Tirar foto",
                    is_default_action=True,
                    on_click=lambda _: [page.close(dialog), tirar_foto(e)]
                ),
                ft.CupertinoActionSheetAction(
                    text="🗂️ Escolher arquivo",
                    on_click=lambda _: [page.close(dialog), abrir_arquivo(e)]
                ),
                ft.CupertinoActionSheetAction(
                    text="Cancelar",
                    is_destructive_action=True,
                    on_click=lambda _: page.close(dialog)
                ),
            ],
        )
        dialog = ft.CupertinoAlertDialog(
            content=action_sheet,
            open=True,  
        )

        page.overlay.append(dialog)
        page.update()

    botao_camera = ft.IconButton(
        icon=ft.Icons.CAMERA_ALT,
        icon_color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE_500,
        icon_size=20,
        style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=5),
        on_click=abrir_opcoes_camera,
    )

    avatar_com_camera = ft.Stack(
        width=120,
        height=120,
        controls=[
            a1,
            ft.Container(content=botao_camera, alignment=ft.alignment.bottom_right),
        ]
    )

    def criar_conta(e):
        if not usuario.value.strip() or not email_login.value.strip() or not Senha_Cadastro.value.strip() or not Senha_Cadastro_confirme.value.strip():
            page.open(ft.SnackBar(ft.Text("⚠️ Todos os campos devem ser preenchidos!"), bgcolor="RED"))
            return
        email_regex = r"^[\w\.-]+@(gmail\.com|yahoo\.com|outlook\.com|hotmail\.com)$"
        if not re.match(email_regex, email_login.value.strip()):
            page.open(ft.SnackBar(ft.Text("👎 E-mail inválido!"), bgcolor="RED"))
            return
        if Senha_Cadastro.value != Senha_Cadastro_confirme.value:
            page.open(ft.SnackBar(ft.Text("👎 Senhas não coincidem!"), bgcolor="RED"))
            return

        usuarios = ler_usuarios()
        novo_usuario = {
            "nome": usuario.value.strip(),
            "email": email_login.value.strip(),
            "senha": Senha_Cadastro.value.strip(),
            "foto": a1.content.src if isinstance(a1.content, ft.Image) else None
        }
        usuarios.append(novo_usuario)
        salvar_usuarios(usuarios)

        page.go('/home')
        
    botão_cadastro = ft.TextButton("Criar uma conta", on_click=criar_conta)
    botão_login = ft.TextButton("Tem uma conta?", on_click=lambda _: page.go('/'))
    return ft.View(
        route='/Cadastro',
        controls=[
            ft.Column(
                controls=[
                    avatar_com_camera,
                    usuario,
                    email_login,
                    Senha_Cadastro,
                    Senha_Cadastro_confirme,
                    ft.Row(
                        controls=[botão_cadastro, botão_login],
                        alignment="center",
                        spacing=20
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
