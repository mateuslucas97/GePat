import flet as ft


def main(page: ft.Page):
    page.title = 'Gestão de Patrimônio'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                '/',
                [
                    ft.AppBar(
                        title=ft.Text('Menu Principal'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    ft.ElevatedButton(
                        'Cadastrar', on_click=lambda _: page.go('/cadastrar')
                    ),
                    ft.ElevatedButton(
                        'Consultar', on_click=lambda _: page.go('/consultar')
                    ),
                    ft.ElevatedButton(
                        'Alterar', on_click=lambda _: page.go('/alterar')
                    ),
                ],
            )
        )
        if page.route == '/cadastrar':
            page.views.append(
                ft.View(
                    '/cadastrar',
                    [
                        ft.AppBar(
                            title=ft.Text('Cadastro'),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.ElevatedButton(
                            'Pagina Inicial', on_click=lambda _: page.go('/')
                        ),
                    ],
                )
            )
        elif page.route == '/consultar':
            page.views.append(
                ft.View(
                    '/consultar',
                    [
                        ft.AppBar(
                            title=ft.Text('Consultar'),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.ElevatedButton(
                            'Pagina inicial', on_click=lambda _: page.go('/')
                        ),
                    ],
                )
            )
        elif page.route == '/alterar':
            page.views.append(
                ft.View(
                    '/alterar',
                    [
                        ft.AppBar(
                            title=ft.Text('Alterar'),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.ElevatedButton(
                            'Pagina inicial', on_click=lambda _: page.go('/')
                        ),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

