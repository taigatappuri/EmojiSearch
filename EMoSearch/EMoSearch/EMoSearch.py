import reflex as rx
from EMoSearch import style
from EMoSearch.state import State

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
                style={"padding": "10px"},
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
        # カード全体のスタイル
        style={
            "border": "1px solid #ccc",  # 境界線
            "border-radius": "10px",     # 角の丸み
            "margin": "10px",            # 外側の余白
            "padding": "20px",           # 内側の余白
            "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",  # 影
            "transition": "0.3s",        # ホバー時のトランジション
            "background-color": "#fff",  # 背景色
        },
        hover_style={
            "box-shadow": "0 8px 16px 0 rgba(0,0,0,0.2)",  # ホバー時の影
        }
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
    return rx.container(
        rx.vstack(
            action_bar(),
            chat(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)