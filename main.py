import flet as ft
from password_generator import password_generator
import clipboard


def main(page: ft.Page):
    def generate_clicked(e):
        new_task.value = password_generator(
            size=int(characters_size.value),
            special_chars=special_characters.value,
            digits=digit_characters.value,
        )
        page.update()

    def copy_clicked(e):
        clipboard.copy(new_task.value)

    new_task = ft.TextField(
        hint_text="Generated password",
        width=300,
        read_only=True,
    )

    page.add(
        ft.Row(
            [
                new_task,
                ft.ElevatedButton("Generate", on_click=generate_clicked),
                ft.ElevatedButton("Copy", on_click=copy_clicked),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    special_characters = ft.Switch(label="Specials")
    digit_characters = ft.Switch(label="Digits")
    characters_size = ft.TextField(width=60, height=60, value=12)

    page.add(
        ft.Row(
            [special_characters, digit_characters, characters_size],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
