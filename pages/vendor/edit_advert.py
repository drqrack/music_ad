from nicegui import ui
from components.sidebar import show_sidebar

@ui.page('/vendor/edit_advert')
def show_edit_advert():
    with ui.row().classes("w-full"):
       with ui.column().classes("w-[20%]"):
           show_sidebar()
       with ui.column().classes("w-[80%]"):
           ui.label("Dashboard contents remain here")