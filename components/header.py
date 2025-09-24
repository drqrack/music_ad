from nicegui import ui



def show_header():
    ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>')

    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    with ui.element("header").classes('w-full bg-green text-white flex flex-row justify-between items-center px-20 py-4 fixed top-0 left-0 z-10').style('font-family: "Josefin Sans", sans-serif'):
        with ui.element("div"):
            ui.label("kolkit").style('font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normai').classes('text-4xl font-bold')

        with ui.row().classes('text-sm space-x-4'):
            ui.link(text="Home", target="/").classes('no-underline text-white cursor-pointer')
            ui.link(text="Talent Directory", target="/view_advert").classes('no-underline text-white')
            ui.link(text="About Us", target="/about").classes('no-underline text-white')
            ui.link(text="Blog", target="/").classes('no-underline text-white')
            ui.link(text="Contact Us", target="/contact").classes('no-underline text-white')
            ui.link(text="Record Label", target="/vendor/dashboard").classes('no-underline text-white')
            

        with ui.row().classes('gap-4 flex flex-row items-center'):
            ui.link(text="Post Ad", target="/artist_create_advert").classes('no-underline text-gray-600 font-bold text-lg')
            with ui.row().classes('gap-0'):
                ui.button(text="Registration", on_click=lambda: ui.navigate.to('/artist_signup')).props('flat dense no-caps').classes('bg-white px-4 py-2 text-green')
                ui.button(text="Login", on_click=lambda: ui.navigate.to('/signin')).props('flat dense no-caps').classes('bg-green-700 px-6 py-2 text-white')
        