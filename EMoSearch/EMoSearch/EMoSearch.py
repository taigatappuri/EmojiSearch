import reflex as rx
from EMoSearch import style
from EMoSearch.state import State
import os

def show_result(emoji: str, emoji_name: str, similarity: float) -> rx.Component:
    return rx.box(
        rx.hstack(
            # カードのタイトル（絵文字とその名前）
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.text(emoji, style={"font-size": "2em"}),
                        text_align="center",    
                    ),
                    rx.box(
                        rx.text(emoji_name, style={"font-size": "2em"}),
                        text_align="center",
                    ),
                ),
                style={"padding": "10px"},
            ),
            # similarity の表示
            rx.box(
                rx.text(f"Similarity: {similarity:.2f}", style={"font-size": "1em"}),
                text_align="center",
                style=style.similarity_style,
            ),
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

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.words,   
            placeholder="単語を入力",
            on_change=State.set_words,
            style=style.input_style,
        ),
        rx.button(
            "検索🔍️",
            on_click=State.get_results,
            style=style.button_style
        ),
    )



def index() -> rx.Component:
    print(os.getcwd())
    return rx.container(
        rx.vstack(
            action_bar(),
            chat(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)