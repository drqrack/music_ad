from nicegui import ui


@ui.page("/")
def show_homepage():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.row().classes("h-screen w-full relative"):
        ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

        # Video background container
        ui.html(
            f"""
            <video autoplay loop muted class="-z-10 absolute inset-0 w-full h-full object-cover">
                <source src="/assets/background_video.mp4" type="video/mp4">
            </video>
        """
        )

        # Content to be placed on top of the video
        with ui.column().classes(
            "flex flex-col items-center justify-center w-full h-screen" \
            " text-white bg-black/50"
        ).style('font-family: "Josefin Sans", sans-serif'):
            ui.label("kolkit").classes("text-9xl font-bold drop-shadow-md").style(
                'font-family: "Gwendolyn", cursive; font-weight: 400; font-style: normai'
            )
            ui.label("Join the Kolk!t Community").classes('text-6xl font-bold')
            ui.label("Connect with artists, discover new music, and grow your network").classes('text-2xl')
            ui.button(
                text="Get Started", on_click=lambda: ui.navigate.to("/about")
            ).classes(
                "mt-4 px-6 py-3 rounded-full font-semibold text-white text-lg shadow-lg shadow-green-100"
            ).props(
                "flat dense no-caps"
            ).style(
                "border: solid 2px green"
            )