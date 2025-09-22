from nicegui import ui


def show_footer():
    ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>')

    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">'
    )
    ui.query('.nicegui-row').classes('flex-nowrap')

    with ui.element("section").classes(
        "bg-gray-900 w-full h-full text-white flex flex-row justify-center items-center"
    ).style('font-family: "Stoke", serif; font-style: normal;'):
        with ui.grid(rows=5).classes(
            "w-[100%] flex flex-row justify-between items-center px-20 py-20"
        ):
            with ui.column().classes('w-[15%]'):
                ui.label("kolkit").style(
                    'font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normai'
                ).classes("text-4xl text-green font-bold py-8")
                ui.label("That necessitat music platform that optimi your store popularised the release")
                with ui.row().classes('flex flex-row justify-around items-center w-full'):
                    ui.html('<i class="fa-brands fa-facebook-f"></i>').classes('rounded-full bg-white text-blue px-4 py-2')
                    ui.html('<i class="fa-brands fa-x-twitter"></i>').classes('rounded-full bg-white text-black px-3 py-2')
                    ui.html('<i class="fa-brands fa-instagram"></i>').classes('rounded-full bg-white text-orange px-3 py-2')


            with ui.column().classes('w-[15%]'):
                ui.label("Company").classes("text-2xl font-bold py-8")
                ui.label("About Us")
                ui.label("Why Kolkit")
                ui.label("Contact With Us")
                ui.label("Our Partners")

            with ui.column().classes('w-[15%]'):
                ui.label("Resources").classes("text-2xl font-bold py-8")
                ui.label("Quick Links")
                ui.label("Albums")
                ui.label("Sign New Artist")
                ui.label("Producers")

            with ui.column().classes('w-[15%]'):
                ui.label("Legal").classes("text-2xl font-bold py-8")
                ui.label("Affiliate")
                ui.label("Blog")
                ui.label("Help & Support")
                ui.label("Careers")

            with ui.column().classes('w-[15%]'):
                ui.label("Products").classes("text-2xl font-bold py-8")
                ui.label("Start a Trial")
                ui.label("How It Works")
                ui.label("Features")
                ui.label("Price & Planing")

        ui.separator().classes('h-0.5 bg-green-300 w-[80%]')
        with ui.row().classes('gap-1'):
            ui.html('<h1> &copy 2025 Kolkit. Made with nicegui by</h1>')
            ui.html('<h1>FreeWorld. </h1>').classes('text-green')
