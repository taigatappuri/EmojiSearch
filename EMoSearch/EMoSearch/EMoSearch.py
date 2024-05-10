import reflex as rx
from EMoSearch import style
from EMoSearch.state import State
import os
import time

from typing import List, Tuple

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"

def emoji_copy(emoji: str) -> None:
    rx.box(
        rx.toast.provider(),
    )

def show_result(emoji: str, emoji_name: str, similarity: float) -> rx.Component:
    return rx.box(
        rx.hstack(
            # カードのタイトル（絵文字とその名前）
            rx.box(
                rx.text(
                    emoji,
                    font_size="3em",
                    high_contrast=True,
                ),
            ),
            rx.box(
                rx.text(
                    emoji_name,
                    color=rx.color("gray", 8),
                    font_size="1.5em",
                    high_contrast=True,
                    font_family="IBM Plex Mono",
                ),
                text_align="left",
                margin_left="auto",
                margin_y="auto",
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
                    "📋",
                    on_click=emoji_copy(emoji),
                    style=style.button_style,
                    border_radius="150%",
                    color_scheme='yellow', # white が使えるはずだが、使えない...
                    box_shadow=shadow, 
                ),
                text_align="center",
                style={"padding": "10px"},
                margin_left="auto",
                margin_y="auto",
            ),
        ),
        style=style.card_style,
        width="500px",
        #hover_style=style.card_hover_style,  # ホバー時のスタイル
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
    return rx.hstack(
            rx.form(
                rx.hstack(
                    rx.input(
                        placeholder="Enter the text✨️",
                        name="words",
                        on_change=State.set_words,
                        width="400px",
                    ),
                    rx.button(
                        "Search🔍️",
                        on_click=State.get_results,
                        type="submit"
                    ),
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
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