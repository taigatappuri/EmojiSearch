from rxconfig import config

import reflex as rx
from EMoSearch import style

config.app_name = "EMoSearch"


def search_part() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.box(
                "EMoSearch",
                text_align="center",
            ),
            rx.box(
                set_search_box(),
            )
        )
    )

def result() -> rx.Component:
    return rx.box(
        rx.center(
            "検索結果が表示されます",
            text_align="center",
            style=style.result_style,
        )
    )

def result_part() -> rx.Component:
    return rx.container(
        rx.box(
            rx.center(
                "検索結果",
                text_align="center",
            )
        ),
        result(),
    )

def set_search_box() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="ワードを入力✨️",
            style=style.input_style,
            
        ),
        rx.button(
            "検索🔍️",
            style=style.button_style,
        ),
    )

def index() -> rx.Component:
    return rx.container(

        search_part(),
        result_part(),
    )


app = rx.App()
app.add_page(index)
