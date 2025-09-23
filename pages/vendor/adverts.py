from nicegui import ui
from components.sidebar import show_sidebar

@ui.page('/vendor/adverts')
def show_vendor_adverts():
    with ui.row().classes("w-full"):
       with ui.column().classes("w-[20%]"):
           show_sidebar()
       with ui.column().classes("w-[80%]"):
           ui.label("Vendor Adverts goes here")