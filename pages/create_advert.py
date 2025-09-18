from nicegui import ui
from components.header import show_header

@ui.page('/create_advert')
def show_create_advert():
    show_header()
    with ui.element('main').classes('w-full h-screen flex flex-col justify-center items-center bg-[url("/assets/pos.jpg")] bg-cover bg-center').style('font-family: "Josefin Sans", sans-serif'):
        with ui.card().classes('w-[40%] flex flex-col justify-center items-center'):
            ui.label("kolkit").style('font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normai').classes('text-2xl font-bold text-green-900')
            ui.label("Create an Ad").classes('text-2xl')
            ui.label("Let your works be seen")
            ui.input(label="Title", placeholder="Enter title")
            ui.input(label="")