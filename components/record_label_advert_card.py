from nicegui import ui

def show_record_label_advert_card(advert):
    # with ui.card().on(type="click", handler=lambda: ui.navigate.to(f"/advert?id={advert["id"]}")).classes("w-80 p-6 rounded-2xl shadow-md cursor-pointer"):
    with ui.card().on(type="click", handler=lambda: ui.navigate.to("/view_advert")).classes("w-80 p-6 rounded-2xl shadow-md cursor-pointer"):
        with ui.row().classes("items-center space-x-4"):
            ui.image(source=advert["flyer_url"]).classes("w-14 h-14 rounded-lg")
            with ui.column().classes("items-start"):
                ui.label(text=advert["description"]).classes("font-semibold text-lg")
                ui.label("Kumasi, Ghana").classes("text-sm").style("margin-top: -10px;")
        ui.label(text=advert["title"]).style("font-size: 1.2rem; font-weight: bold")
        ui.label(text=advert["category"]).style("font-size: 0.9rem; color: #000;")
        ui.label("Mixing, Mastering, Production").classes("")
        with ui.row().classes("justify-between items-center flex flex-row space-x-8 w-full"):
            ui.label("Ghc 5000/monthly")
            with ui.row().classes('flex flex-row gap-1'):
                ui.button(icon="edit").props("flat dense no-caps").classes("px-2 py-2 bg-green text-white")
                ui.button(icon="delete").props("flat dense no-caps").classes("px-2 py-2 bg-red text-white")