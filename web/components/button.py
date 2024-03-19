import reflex as rx
from web.styles.colors import Color
from web.styles.styles import Size

LOCAL_ICONS = ["x", "discord"]


def button(url: str, text="", icon="chevron-right", secondary=False) -> rx.Component:
    return rx.button(
        _button_icon(icon),
        text,
        on_click=lambda: rx.redirect(url),
        size=Size.DEFAULT.value,
        color=Color.BACKGROUND.value,
        background=Color.SECONDARY.value if secondary else Color.ACCENT.value
    )

# Por algo que desconozco (quizás un error), aunque el icon sea local, se intenta inicializar rx.icon. De ahí este fix.


def _button_icon(icon: str) -> rx.Component:
    return rx.cond(
        icon in LOCAL_ICONS,
        rx.image(src=f"/{icon}.svg", width="24px", height="auto"),
        rx.icon("chevron-right" if icon in LOCAL_ICONS else icon)
    )