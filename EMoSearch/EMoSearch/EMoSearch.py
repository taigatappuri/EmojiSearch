from rxconfig import config

import reflex as rx

config.app_name = "EMoSearch"

def SearchBox(words: str) -> rx.Component:
    return rx.box(
        words,
        text_align="center",
        padding=10,
        margin=10,
        border="1px solid black",
        border_radius=5,
        background_color="lightgrey",
    )


def search_part() -> rx.Component:
    return rx.container(
        rx.box(
            "EMoSearch",
            text_align="center",
        ),
        rx.box(
            set_search_box(),
        )
    )

def result_part() -> rx.Component:
    return rx.container(
        rx.box(
            "検索結果",
            text_align="center",
        ),
        rx.box(
            "検索結果が表示されます",
            text_align="center",
        )
    )

def set_search_box() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="ワードを入力✨️"),
        rx.button("検索🔍️"),
    )

def index() -> rx.Component:
    return rx.container(
        search_part(),
        result_part(),
    )


app = rx.App()
app.add_page(index)
