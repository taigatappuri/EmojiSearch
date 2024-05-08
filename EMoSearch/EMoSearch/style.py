import reflex as rx
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"

input_style = dict(
	border_width="1px", padding="1em", box_shadow=shadow
)

result_style = dict(
	padding="1em",
	border_width="1px",
	margin_y="0.5em",
	box_shadow=shadow,
	max_width="50em",
	display="inline-block",
	background_color=rx.color("yellow", 5),
)

button_style = dict(
	background_color=rx.color("accent",10),
	box_shadow=shadow,
)