from nicegui import ui
from components.sidebar import show_sidebar

@ui.page("/vendor/dashboard")
def show_vender_dashboard():
    with ui.row().classes("w-full h-screen flex flex-row justify-between items-center"):
       with ui.column().classes("w-[20%]"):
           show_sidebar()
       with ui.column().classes("w-[80%]"):
           ui.label("Dashboard contents remain here")