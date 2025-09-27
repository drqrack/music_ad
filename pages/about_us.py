from nicegui import ui

@ui.page('/about_us')
def show_about_us():
     ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')
     ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
     with ui.element('section').classes('w-full h-screen flex flex-col justify-center items-center bg-[url("/assets/bg-smoke.png")] bg-cover bg-center text-white px-20').style('font-family: "Josefin Sans", sans-serif'):
        ui.label("Established in 2013, Kolkit is a global educational media platform for music industry professionals, primarily artist managers and professionally self-managed artists.We help artists & managers make their dreams come true by providing business tools, training, and mentorship from GRAMMY-level experts so that they can become high-demand music industry entrepreneurs.Each year we connect thousands of people from around the globe with the music industry’s top experts through live mentorship, training, interviews, downloads, and online courses.Our experts work in all areas of the industry from major label A&R to tour managers with long lists of superstar artists on their client rosters including everyone from The Rolling Stones to Dolly Parton to Beyonce.").style("line-height: 2em;").classes('text-lg')
        with ui.row().classes("flex flex-row justify-center items-center"):
            ui.button(
                text="Apply Now", on_click=lambda: ui.navigate.to("/about")
            ).classes(
                "mt-4 px-6 py-3 rounded-full text-white shadow-sm shadow-green-100"
            ).props(
                "flat dense no-caps"
            ).style(
                "border: solid 2px green"
            )
            ui.label("or").classes('text-lg')
            ui.button(
                text="Find the Talent", on_click=lambda: ui.navigate.to("/")
            ).classes(
                "mt-4 px-6 py-3 rounded-full text-white bg-green shadow-sm shadow-green-100"
            ).props(
                "flat dense no-caps"
            )