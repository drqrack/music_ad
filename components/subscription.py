from nicegui import ui

def show_subscription():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')
    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')

    with ui.element("section").classes('w-full bg-green text-white flex flex-row justify-around items-center px-10 py-10').style('font-family: "Josefin Sans", sans-serif'):
        ui.label("Subscribe for everyday job newsletter").classes('text-5xl w-1/2')
        with ui.row().classes('flex flex-row gap-0 justify-center items-center w-1/2'):
            ui.input(placeholder="Enter your email").classes('bg-white px-5')
            ui.button(text="Subscribe Now").props('flat dense no-caps').classes('text-white bg-gray-800 px-5 py-3').style('border: solid 4px white')