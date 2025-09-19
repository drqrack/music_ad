from nicegui import ui
from components.header import show_header
from components.talent_card import show_talent_card
from components.subscription import show_subscription
from components.footer import show_footer
import requests
from utils.api import base_url

@ui.page("/about")
def show_about_page():
    show_header()
    with ui.element("main").classes(
        'w-full h-screen bg-[url("/assets/asset10.jpeg")] bg-cover bg-center flex flex-col justify-center items-center'
    ):
        with ui.element("div").classes(
            "bg-black/40 w-full h-full flex flex-col justify-center items-center"
        ):
            with ui.column().classes("w-1/2 text-white").style(
                'font-family: "Stoke", serif; font-style: normal;'
            ):
                with ui.row().classes("gap-0"):
                    ui.label("Talent").style("font-weight: 700;").classes("text-7xl")
                    ui.label("Hunt").style("font-weight: 700;").classes(
                        "text-7xl text-green-500"
                    )
                ui.label("Here You Can Prove Your Talent").classes("text-2xl")
                ui.label(
                    "Etiam nec imperdiet nisi. Nullam in turpis placerat, elementum felis vitae, varius erat. Sed eleifend, metus ac convallis tincidunt, lorem turpis pharetra nibh, id blandit mi lacus ."
                ).style("line-height: 2em;")
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

    with ui.element("section").classes('w-full h-screen text-gray-700 flex flex-col justify-center items-center').style('font-family: "Josefin Sans", sans-serif'):
        with ui.column().classes('flex flex-col justify-center items-center'):
            ui.label("Recently Registered Talents").classes('text-4xl')
            ui.separator().classes('h-1 bg-green w-1/2 mb-8')
        with ui.grid(columns=4).classes('flex justify-center items-center w-full'):
            ui.label("Contruction ongoing")
            # response = requests.get(f"{base_url}/adverts?limit=12")
            # json_data = response.json()
            # for advert in json_data["data"]:
            #     show_talent_card(advert)

    with ui.element("section").style('font-family: "Josefin Sans", sans-serif').classes(
        "w-full h-screen flex flex-col justify-center items-center text-white "
    ):
        with ui.element().classes('w-full h-[50%] relative flex flex-col justfiy-center items-center py-8'):
            ui.html(
                f"""
                <video autoplay loop muted class="-z-10 absolute inset-0 w-full h-full object-cover">
                    <source src="/assets/pinpage.mp4" type="video/mp4">
                </video>
            """
            )
            with ui.element():
                ui.label("Talent Hunt ? Discover Some Amazing Talent").classes(
                    "font-bold text-5xl p-4"
                )
                ui.label(
                    "Reach thousands of actors, models, musicians and other creatives by placing a free casting call, or hand-pick from our Talent Directory"
                ).classes("text-lg mb-16")
            with ui.row().classes(""):
                ui.button(text="Create Your Free Profile", icon="description").props(
                    "flat dense no-caps"
                ).style("border: solid 2px white").classes('bg-green text-white px-2 py-2')
                ui.button(text="See Our Plans & Services", icon="subject").props(
                    "flat dense no-caps"
                ).style("border: solid 2px green").classes('bg-white text-green px-2 py-2')

    with ui.element("section").classes('w-full h-full flex flex-row justify-between bg-gray-100 text-gray-600').style('font-family: "Josefin Sans", sans-serif'):
        with ui.column().classes('w-1/2 flex flex-col justify-center items-center px-8'):
            ui.label('Top 6 reasons why you should choose us').classes('text-4xl font-bold')
        with ui.element('div').classes('w-1/2'):
            ui.image('https://kayapati.com/demos/talenthunt/wp-content/uploads/elementor/thumbs/hunt-women-ovy4qmzybt1u1kb13e7zfw2piiv2mfjwt7mo7lj7v4.jpg')

    with ui.element('section').style('font-family: "Josefin Sans", sans-serif').classes('w-full h-screen text-gray-700 flex flex-col justify-center items-center'):
        ui.label("What Our Clients Say").classes('text-4xl')
        ui.separator().classes('h-1 bg-green w-[20%] mb-10')
        with ui.grid(columns=4).classes('w-full px-10 py-10'):
                for i in range(4):
                    with ui.card().classes('w-full flex flex-col'):
                        ui.label("Testimony")
                        with ui.row().classes('flex flex-row justify-between items-center'):
                            ui.image("https://kayapati.com/demos/talenthunt/wp-content/uploads/2020/09/42b51358-5681-4b80-b002-a88533ed27ca.jpg").classes('object-cover')
                            with ui.column().classes(''):
                                ui.label("Name").classes('text-black text-lg')
                                ui.label("Role")

    show_subscription()
    show_footer()