from nicegui import ui
from components.sidebar import show_sidebar
from components.record_label_advert_card import show_record_label_advert_card

@ui.page('/vendor/adverts')
def show_vendor_adverts():
    ui.query('.nicegui-row').classes('flex-nowrap')
    with ui.row().classes("w-full h-screen flex flex-row justify-between items-center"):
       with ui.column().classes("w-[20%] h-full"):
           show_sidebar()
       with ui.column().classes("w-[80%] h-full"):
           with ui.column().classes('flex flex-col justify-center items-center w-full py-20 px-10'):
            ui.label("Recent Job Posts").classes('text-4xl')
            ui.separator().classes('h-1 bg-green w-1/5 mb-8')
            with ui.grid(columns=3).classes('gap-10'):
                for i in range(6):
                    show_record_label_advert_card()