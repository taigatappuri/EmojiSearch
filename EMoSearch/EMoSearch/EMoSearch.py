import reflex as rx
from EMoSearch import style
from EMoSearch.state import State
import os
import time

from typing import List, Tuple

def show_result(emoji: str, emoji_name: str, similarity: float) -> rx.Component:
    return rx.flex(
        # カードのタイトル（絵文字とその名前）
        rx.box(
            rx.text(emoji, style={"font-size": "2em"}),
            text_align="center",    
            margin_left="auto",
        ),
        rx.box(
            rx.text(emoji_name, style={"font-size": "2em"}),
            text_align="center",
            margin_left="auto",
        ),
        # # similarity の表示
        # rx.box(
        #     rx.text(f"Similarity: {similarity:.2f}", style={"font-size": "1em"}),
        #     text_align="center",
        #     margin_left="auto",
        #     style=style.similarity_style,
        # ),
        # コピーボタン
        rx.box(
            rx.button(
                "コピー",
                on_click=rx.set_clipboard(emoji),
                style=style.button_style,
            ),
            text_align="center",
            style={"padding": "10px"},
        ),
        style=style.card_style,
        hover_style=style.card_hover_style,  # ホバー時のスタイル
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.results,
            lambda res: show_result(res[0], res[1], res[2]),
        )
    )

class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data



def action_bar() -> rx.Component:
    return rx.vstack(
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="単語を入力してください",
                        name="words",
                        on_change=State.set_words,
                    ),
                    rx.button(
                        "検索",
                        on_click=State.get_results,
                        type="submit"
                    ),
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.heading("Search Words"),
            rx.text(State.words),
        )



def index() -> rx.Component: 
    return rx.container(
        rx.vstack(
            action_bar(),
            chat(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)