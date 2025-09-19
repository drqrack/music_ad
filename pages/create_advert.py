from nicegui import ui
import requests
from utils.api import base_url

# save the uploaded image
_advert_image = None

def _handle_image_upload(advert):
    global _advert_image
    _advert_image = advert.content

def _post_event(data, files):
    response = requests.post(url=f"{base_url}/adverts", data=data, files=files)
    if response.status_code == 200:
        ui.notify(
            message= "Events added successfully",
            type= "positive")
        return ui.navigate.to("/")
    elif response.status_code == 422:
        return ui.notify(message="Please ensure all inputs are filled!", type="negative")
    print(response.status_code)
    json_data = response.json()
    print(json_data)
        

@ui.page('/create_advert')
def show_create_advert():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    with ui.element('main').classes('w-full h-full flex flex-col justify-center items-center p-4').style('font-family: "Josefin Sans", sans-serif'):
        with ui.card().classes('w-[40%] flex flex-col justify-center items-center shadow-lg bg-gray-100'):
            ui.label("kolkit").style('font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normal').classes('text-xl font-bold text-gray-800')
            ui.label("Create an Ad").classes('text-xl font-bold text-green-900')
            ui.separator().classes('w-[10%] h-0.5 bg-green-800')
            advert_title = ui.input(label="Title", placeholder="Enter the title").classes('w-full bg-white px-2')
            advert_description = ui.textarea(label="Description", placeholder="Enter the details").classes('w-full bg-white px-2')
            advert_price = ui.number(label="Price", placeholder="Enter the price").classes('w-full bg-white px-w')
            advert_category = ui.input(label="Category", placeholder="Enter the category").classes('w-full bg-white px-2')
            ui.upload(auto_upload=True, on_upload=_handle_image_upload).classes('w-full mb-4').props('color=green')
            ui.button(text="Post", on_click=lambda: _post_event(
                data={
                    "title": advert_title.value,
                    "description": advert_description.value,
                    "price": advert_price.value,
                    "category": advert_category.value
                }, files={"flyer": _advert_image}
            )).props('flat dense').classes('bg-green text-white w-[80%] py-2').style('border: solid 2px gray')
            