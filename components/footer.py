from nicegui import ui

def show_footer():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    with ui.element("section").classes('bg-gray-800 w-full h-full text-white flex flex-row justify-between items-center'):
        with ui.grid(rows=5).classes('flex flex-row '):
            with ui.column():
                ui.label("kolkit").style('font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normai').classes('text-5xl font-bold')

            with ui.column():
                ui.label("Company")