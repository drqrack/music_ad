from nicegui import ui
import requests
from components.sidebar import show_sidebar
from components.record_label_advert_card import show_record_label_advert_card
# from components.advert_card import show_advert_card
from utils.api import base_url

@ui.page("/vendor/dashboard")
def show_vender_dashboard():
    ui.query('.nicegui-row').classes('flex-nowrap')
    with ui.row().classes("w-full h-screen flex flex-row justify-between items-center"):
       with ui.column().classes("w-[20%] h-full"):
           show_sidebar()
       with ui.column().classes("w-[80%] h-full py-20 mt-10"):
           with ui.element("section").classes('w-full h-full text-gray-700 flex flex-col justify-center items-center px-10 py-10').style('font-family: "Josefin Sans", sans-serif'):
            with ui.column().classes('flex flex-col justify-center items-center'):
                ui.label("Recently Posted Adverts").classes('text-4xl')
                ui.separator().classes('h-1 bg-green w-1/3 mb-8')
                with ui.grid(columns=4).classes('flex justify-center items-center w-full h-[30%] gap-10'):
                    response = requests.get(f"{base_url}/adverts?limit=6")
                    json_data = response.json()
                    for advert in json_data["data"]:
                        show_record_label_advert_card(advert)
                        # show_advert_card(advert)