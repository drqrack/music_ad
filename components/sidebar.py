from nicegui import ui, app


def show_sidebar():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    with ui.column().classes(
        "bg-gray-100 p-4 w-full shadow-lg h-full justify-between items-center"
    ).style('font-family: "Stoke", serif; font-style: normal;'):
        # Top section with branding and vendor info
        with ui.column().classes("w-full items-center mb-6"):
            ui.link("Kolkit", "/vendor/dashboard").classes(
                "text-2xl font-extrabold text-green no-underline"
            ).style('font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normal')
            ui.label("Record Label").classes("text-3xl font-bold text-gray-800")

        ui.separator().classes("w-full bg-green h-0.5 mb-6")

        # Navigation links section
        with ui.column().classes("w-full space-y-4 flex-grow"):
            # Dashboard
            with ui.row().classes(
                "w-full items-center cursor-pointer hover:bg-green transition-colors p-2 rounded-lg"
            ):
                ui.icon("dashboard").classes("text-green")
                ui.link("Dashboard", "/vendor/dashboard").classes(
                    "text-gray-700 font-semibold no-underline text-lg"
                )

            # Events (Manage and Create)
            with ui.row().classes(
                "w-full items-center cursor-pointer hover:bg-green transition-colors p-2 rounded-lg"
            ):
                ui.icon("event").classes("text-green")
                ui.link("Adverts", "/vendor/adverts").classes(
                    "text-gray-700 font-semibold no-underline text-lg"
                )

            # Analytics
            with ui.row().classes(
                "w-full items-center cursor-pointer hover:bg-green transition-colors p-2 rounded-lg"
            ):
                ui.icon("analytics").classes("text-green")
                ui.link("Analytics", "/vendor/dashboard").classes(
                    "text-gray-700 font-semibold no-underline text-lg"
                )

            # Settings
            with ui.row().classes(
                "w-full items-center cursor-pointer hover:bg-green transition-colors p-2 rounded-lg"
            ):
                ui.icon("settings").classes("text-green")
                ui.link("Settings", "/vendor/dashboard").classes(
                    "text-gray-700 font-semibold no-underline text-lg"
                )

        # Logout button at the bottom
        with ui.column().classes("w-full items-center mt-auto"):
            ui.separator().classes("w-full bg-green h-0.5 my-6")
            with ui.row().classes(
                "w-full items-center cursor-pointer p-2 rounded-lg hover:bg-green-100 transition-colors"
            ):
                ui.icon("logout").classes("text-green-600")
                ui.button(
                    "Logout", on_click=lambda: app.storage.user.clear(), color="green"
                ).classes(
                    "bg-transparent text-green-600 font-semibold shadow-none text-lg"
                ).props(
                    "flat no-caps"
                )
