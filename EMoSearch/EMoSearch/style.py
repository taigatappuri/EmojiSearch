import reflex as rx

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"

input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow
)

button_style = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow,
)



similarity_style = dict(
    text_align= "center", 
    padding="10px",
    color=rx.color("gray", 10),
)

card_style = dict(
    border="1px solid #ccc",  # 境界線
    border_radius="10px",     # 角の丸み
    margin="10px",            # 外側の余白
    padding="20px",           # 内側の余白
    box_shadow="0 4px 8px 0 rgba(0,0,0,0.2)",  # 影
    transition="0.3s",        # ホバー時のトランジション
    background_color="#fff",  # 背景色
)

card_hover_style = dict(
    box_shadow="0 8px 16px 0 rgba(0,0,0,0.2)"  # ホバー時の影
)