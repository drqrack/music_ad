from nicegui import ui


# def show_talent_card(adrtve):
    # with ui.card().on(
    #     type="click", handler=lambda: ui.navigate.to(f"/advert?id={advert["id"]}")
    # ).classes("cursor-pointer"):
    #     ui.label(text=advert["title"]).classes("text-green-800 font-bold")
    #     ui.image(source=advert["flyer"])
    #     ui.label(text=advert["description"])
    #     ui.label(text=advert["price"])
    #     ui.label(text=advert["category"])
def show_talent_card():
    with ui.card().classes("").classes('w-[20%] bg-gray-100 cursor-pointer'):
        ui.label("Name").classes("text-green-800 font-bold")
        ui.image("/assets/sing.jpg").classes('w-14 h-14')
        ui.label("Description")
        ui.label("Genre")
        with ui.row().classes('flex flex-row justify-between items-center w-full'):
            ui.label("Category")
            ui.button(icon="visibility", on_click=lambda: ui.navigate.to('/artist_profile')).props('flat dense').classes('bg-green text-white px-2 text-sm')