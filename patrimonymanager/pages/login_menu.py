import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
import sys
import os

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('database'))

import main_menu
from database import database


def main(page: ft.Page) -> None:
    page.title = 'Login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 800
    page.window_height = 800
    page.window_resizable = False

    # Connect to the SQLite database
    conn = database.create_connection()
    valid_credentials = database.get_valid_credentials(conn)

    # Setup our fields
    text_username: TextField = TextField(
        label='Username', text_align=ft.TextAlign.LEFT, width=500
    )
    text_password: TextField = TextField(
        label='Password',
        text_align=ft.TextAlign.LEFT,
        width=500,
        password=True,
    )
    checkbox_signup: Checkbox = Checkbox(label='I agree stuf', value=False)
    button_submit: ElevatedButton = ElevatedButton(
        text='Sign up', width=500, disabled=True
    )

    def validate(e: ControlEvent) -> None:

        if (
            all(
                [
                    text_username.value,
                    text_password.value,
                    checkbox_signup.value,
                ]
            )
            and text_username.value == valid_credentials[0]
            and text_password.value == valid_credentials[1]
        ):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        if (
            text_username.value == valid_credentials[0]
            and text_password.value == valid_credentials[1]
        ):
            # Navigate to the main_menu
            page.update(main_menu.main(page))
        else:
            # display an error message
            text_error = Text(value='Invalid credentials', color='red')
            page.add(text_error)

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Render the page sign-up page
    page.add(
        Row(
            controls=[
                Column(
                    [
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit,
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
