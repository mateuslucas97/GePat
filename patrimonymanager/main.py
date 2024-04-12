import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Menu Principal:  {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Cdastrar: {e.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(target=main, view=ft.AppView.FLET_APP)
