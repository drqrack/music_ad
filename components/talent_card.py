from nicegui import ui


def show_talent_card(advert):
    with ui.card().on(
        type="click", handler=lambda: ui.navigate.to(f"/advert?id={advert["id"]}")
    ).classes("cursor-pointer"):
        ui.label(text=advert["title"]).classes("text-green-800 font-bold")
        ui.image(source=advert["flyer"])
        ui.label(text=advert["description"])
        ui.label(text=advert["price"])
        ui.label(text=advert["category"])