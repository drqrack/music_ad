from nicegui import ui

@ui.page('/record_label_signup')
def show_record_label_signup_page():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    with ui.element("main").classes('w-full h-screen flex flex-col justify-center items-center p-4'):
        with ui.card().classes('w-[40%] bg-gray-100 justify-center items-center shadow-lg'):
            ui.label("kolkit").style('font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normal').classes('text-xl font-bold text-gray-800')
            ui.label("Register Now").classes('text-xl font-bold text-green-900')
            ui.separator().classes('w-[10%] h-0.5 bg-green-800 mb-4')
            with ui.row().classes("gap-0 mb-2"):
                ui.button(text="Artist", on_click=lambda: ui.navigate.to('/artist_signup'), icon="interpreter_mode").props(
                    "flat dense no-caps"
                ).classes('bg-white text-green px-8 py-2 ')
                ui.button(text="Record Label", on_click=lambda: ui.navigate.to('/record_label_signup'), icon="business_center").props(
                    "flat dense no-caps"
                ).classes('bg-green text-white px-2 py-2')
            ui.input(placeholder="Email").props('type=email borderless').classes('w-[80%] bg-white px-4')
            ui.input(placeholder="Password").props('type=password borderless').classes('w-[80%] bg-white px-4')
            ui.input(placeholder="Confirm Password").props('type=password borderless').classes('w-[80%] bg-white px-4')
            ui.checkbox(text="Accept our terms and conditions and privacy policy").classes('text-gray-600 text-sm')
            ui.button(text="Register").classes('w-[80%] bg-green text-white py-2').props('flat dense no-caps')
            with ui.row().classes('text-gray-600 gap-0 space-x-2'):
                ui.label("Already have an account?")
                ui.link("Login", "/signin").classes('text-green no-underline')