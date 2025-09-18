from nicegui import ui
from components.header import show_header


@ui.page("/view_advert")
def show_view_advert():
    show_header()
    ui.label("this is the view ad page")
