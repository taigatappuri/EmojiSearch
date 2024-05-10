import reflex as rx
from EMoSearch import style
from EMoSearch.state import State
import os
import time

from typing import List, Tuple

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"

#def emoji_copy(emoji: str) -> None:
#    rx.box(
#        rx.toast.provider(),
#    )

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
                    on_click=rx.set_clipboard(emoji),
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

def top() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.video(
                    url="/bgy.mp4", # ローカルのビデオファイルパスか、外部URLを指定
                    width="100%", # 画面の幅全体をカバー
                    height="auto", # 高さは自動調整
                    playing=True,
                    controls=False, # ビデオコントロールを非表示に設定
                    autoplay=True, # ページロード時に自動再生
                    loop=True, # ビデオをループ再生
                    muted=True, # 自動再生の場合、ミュートを推奨
                    position="absolute", # 背景として配置するために絶対位置指定
                    top="0",
                    left="0",
                    z_index="-1", # コンテンツの背後に配置
                )
            ),
            rx.box(
                rx.text(
                    "EMoSearch", 
                    font_size="4em", 
                    font_weight="bold",
                    text_align="center",
                    color=rx.color("blue", 10),
                    margin_y="auto",
                ),  
            ),
        ),
    )
    
print(f"Current working directory: {os.getcwd()}")
def index() -> rx.Component: 
    return rx.box(
        top(),
        rx.vstack(
            action_bar(),
            chat(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)