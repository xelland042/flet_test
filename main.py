import flet as ft


def main(page: ft.Page):
    page.bgcolor = '#1F1D2B'

    pie_chart_icon = ft.Image(src='assets/pie_chart.svg', width=40, height=40)

    menu_icon = ft.Image(src='assets/home_icon.svg', width=40, height=40)

    pie_chart_icon_text = ft.Text('Hisob', size=32, color='#ffffff', weight=ft.FontWeight.W_600)

    menu_text = ft.Text('Menu', size=32, color='#ffffff', weight=ft.FontWeight.W_600)

    pie_chart_icon_white = ft.Image(src='assets/pie_chart_white.svg', width=40, height=40)

    menu_icon_white = ft.Image(src='assets/home_icon_white.svg', width=40, height=40)

    def on_click(e: ft.ControlEvent):
        button = e.control.parent.controls[1]
        container = e.control.parent.controls[0]
        all_buttons = e.control.parent.controls[1].parent.parent.parent.controls
        for i in all_buttons:
            if i.content.controls[1].data['pressed']:
                i.content.controls[1].data['pressed'] = False
                i.content.controls[1].width = 195
                i.content.controls[1].bgcolor = 'transparent'
                i.content.controls[1].content.controls = [i.content.controls[1].data['main_icon'],
                                                          i.content.controls[1].data['text']]
                i.content.controls[0].offset.y = 1
            i.content.controls[0].update()
            i.content.controls[1].update()
        if button.data['pressed']:
            pass
        elif not button.data['pressed']:
            button.data['pressed'] = True
            button.width = 90
            button.bgcolor = '#EA7C69'
            button.content.controls = [button.data['second_icon']]
            container.offset.y = 0
            button.update()
            container.update()

    def bg_container(index):
        if index == 0:
            return ft.Container(
                height=135,
                width=164,
                offset=ft.transform.Offset(0, 0),
                animate_offset=ft.animation.Animation(500, ft.AnimationCurve.EASE),
                animate=ft.animation.Animation(500, ft.AnimationCurve.EASE),
                bgcolor='#252937',
                data=index,
                content=ft.Row([
                    ft.Container(
                        width=22,
                        bgcolor='#1f1d2b',
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=0, bottom_right=20
                        ),
                    ),
                    ft.Container(
                        width=120,
                        bgcolor='#1f1d2b',
                        content=ft.Container(
                            bgcolor='#252937',
                            border_radius=ft.BorderRadius(
                                top_left=20, top_right=20, bottom_left=0, bottom_right=0
                            ),
                        )
                    ),
                    ft.Container(
                        width=22,
                        bgcolor='#1f1d2b',
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=20, bottom_right=0
                        ),
                    )
                ], spacing=0)
            )
        else:
            return ft.Container(
                height=135,
                width=164,
                offset=ft.transform.Offset(0, 1),
                animate_offset=ft.animation.Animation(500, ft.AnimationCurve.EASE),
                animate=ft.animation.Animation(500, ft.AnimationCurve.EASE),
                bgcolor='#252937',
                data=index,
                content=ft.Row([
                    ft.Container(
                        width=22,
                        bgcolor='#1f1d2b',
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=0, bottom_right=20
                        ),
                    ),
                    ft.Container(
                        width=120,
                        bgcolor='#1f1d2b',
                        content=ft.Container(
                            bgcolor='#252937',
                            border_radius=ft.BorderRadius(
                                top_left=20, top_right=20, bottom_left=0, bottom_right=0
                            ),
                        )
                    ),
                    ft.Container(
                        width=22,
                        bgcolor='#1f1d2b',
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=20, bottom_right=0
                        ),
                    )
                ], spacing=0)
            )

    def small_icon_text_button(main_icon, second_icon, text, index):
        if index == 0:
            return ft.Container(
                width=90,
                height=90,
                border_radius=16,
                border=ft.border.all(2, '#EA7C69'),
                bgcolor='#EA7C69',
                on_click=on_click,
                animate=ft.animation.Animation(500, ft.AnimationCurve.EASE),
                data={
                    'index': index,
                    'main_icon': main_icon,
                    'second_icon': second_icon,
                    'text': text,
                    'pressed': True,
                },
                content=ft.Row(
                    spacing=25,
                    controls=[
                        second_icon
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        else:
            return ft.Container(
                width=195,
                height=90,
                border_radius=16,
                border=ft.border.all(2, '#EA7C69'),
                bgcolor='transparent',
                on_click=on_click,
                animate=ft.animation.Animation(500, ft.AnimationCurve.EASE),
                data={
                    'index': index,
                    'main_icon': main_icon,
                    'second_icon': second_icon,
                    'text': text,
                    'pressed': False,
                },
                content=ft.Row(
                    spacing=25,
                    controls=[
                        main_icon,
                        text
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

    whole_button_1 = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Stack([bg_container(0), small_icon_text_button(
            main_icon=menu_icon, text=menu_text,
            second_icon=menu_icon_white, index=0)], alignment=ft.alignment.center), width=195, height=135)
    whole_button_2 = ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Stack([bg_container(1), small_icon_text_button(
            main_icon=pie_chart_icon,
            text=pie_chart_icon_text,
            second_icon=pie_chart_icon_white,
            index=1)], alignment=ft.alignment.center), width=195, height=135)

    page.add(ft.Row(
        controls=[
            whole_button_1,
            whole_button_2,
        ], spacing=15.5))


ft.app(target=main)
