import reflex as rx
import web.styles.styles as styles
from web.components.text import text
from web.styles.colors import Color
from web.styles.styles import SizeEM


def info() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.icon(
                "terminal",
                size=32,
                color=Color.BACKGROUND.value
            ),
            text(
                "Últimas noticias:",
                True,
                True,
                Color.BACKGROUND
            ),
            text(
                "Del 20 marzo al 4 de abril podrás enviar tu propuesta de charla o taller.",
                big=True,
                color=Color.BACKGROUND
            ),
            align="center",
            padding_y=SizeEM.MEDIUM.value,
            style=styles.container
        ),
        width="100%",
        background=Color.ACCENT.value
    )