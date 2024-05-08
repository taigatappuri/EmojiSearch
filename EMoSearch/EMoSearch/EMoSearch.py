from rxconfig import config

import reflex as rx

class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.box(
            
        )
    )


app = rx.App()
app.add_page(index)
