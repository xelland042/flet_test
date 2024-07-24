import flet as ft


class MyApp(object):
    def __init__(self, e):
        super().__init__()
        self.active_button = 'Birinchi taom'

    def build(self):
        self.update_buttons()
        return ft.Container(
            padding=ft.padding.only(top=50),
            width=188,
            content=ft.Row(
                spacing=0,
                controls=[
                    ft.Column(
                        expand=True,
                        spacing=30,
                        controls=[
                            self.build_button('Salatlar'),
                            self.build_button('Birinchi taom'),
                            self.build_button('Ikkinchi taom'),
                            self.build_button('Ichimlik'),
                            self.build_button('Desert')
                        ]
                    ),
                ]
            )
        )

    def build_button(self, button_text):
        indicator = ft.Container(bgcolor='#EA7D68', height=54, width=4,
                                 border_radius=2) if self.active_button == button_text else None
        return ft.Row(
            spacing=0,
            controls=[
                ft.Container(
                    alignment=ft.Alignment(0, 0),
                    expand=True,
                    content=ft.TextButton(
                        button_text,
                        content=ft.Text(button_text, size=26),
                        style=ft.ButtonStyle(color='white'),
                        on_click=self.handle_click
                    )
                ),
                indicator
            ]
        )

    def handle_click(self, e):
        self.active_button = e.control.content.value
        self.update_buttons()

    def update_buttons(self):
        self.controls.clear()
        self.controls.append(self.build())


ft.app(target=MyApp)
