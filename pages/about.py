from nicegui import ui
from components.header import show_header
from components.talent_card import show_talent_card
from components.subscription import show_subscription
from components.footer import show_footer
from components.advert_card import show_advert_card
import requests
from utils.api import base_url

@ui.page("/about")
def show_about_page():
    show_header()
    with ui.element("main").classes(
        'w-full h-screen bg-[url("/assets/bg-smoke.png")] bg-cover bg-center flex flex-col justify-center items-center'
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
                ui.label("Here You Can Prove Your Talent").classes("text-3xl")
    
    with ui.element('section').classes('w-full h-screen flex flex-col justify-center items-center bg-[url("/assets/bg-smoke.png")] bg-cover bg-center text-white px-20'):
        ui.label("Established in 2013, Tolkit is a global educational media platform for music industry professionals, primarily artist managers and professionally self-managed artists.We help artists & managers make their dreams come true by providing business tools, training, and mentorship from GRAMMY-level experts so that they can become high-demand music industry entrepreneurs.Each year we connect thousands of people from around the globe with the music industry’s top experts through live mentorship, training, interviews, downloads, and online courses.Our experts work in all areas of the industry from major label A&R to tour managers with long lists of superstar artists on their client rosters including everyone from The Rolling Stones to Dolly Parton to Beyonce.").style("line-height: 2em;").classes('text-lg')
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


    with ui.element('section').classes('w-full h-full flex flex-col justify-center items-center py-10 px-10 bg-gray-100 mb-10').style('font-family: "Josefin Sans", sans-serif'):
        with ui.column().classes('flex flex-col justify-center items-center'):
            ui.label("Recent Job Posts").classes('text-4xl')
            ui.separator().classes('h-1 bg-green w-1/5 mb-8')
            with ui.grid(columns=3).classes('gap-10'):
                for i in range(6):
                    show_advert_card()

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

    with ui.element("section").classes('w-full h-screen text-gray-700 flex flex-col justify-center items-center px-10 py-10').style('font-family: "Josefin Sans", sans-serif'):
        with ui.column().classes('flex flex-col justify-center items-center'):
            ui.label("Recently Registered Talents").classes('text-4xl')
            ui.separator().classes('h-1 bg-green w-1/3 mb-8')
            with ui.grid(columns=4).classes('flex justify-center items-center w-full gap-10'):
                response = requests.get(f"{base_url}/adverts?limit=4")
                json_data = response.json()
                for advert in json_data["data"]:
                    show_talent_card(advert)

    

    with ui.element('section').classes('w-full h-screen flex flex-col justify-center items-center ').style('font-family: "Josefin Sans", sans-serif'):
        ui.label("Popular Genres").classes('text-4xl')
        ui.label("Genres based on its form, style, and cultural influence").classes('text-lg')
        with ui.grid(columns=4).classes('p-8 text-center gap-5'):
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Afrobeat').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Highlife').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Jùjú').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Amapiano').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Bongo Flavor').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Gqom').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Azonto').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('HipLife').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Gospel').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Drill').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('AfroPop').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Dancehall').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Reggae').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('Jazz').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('HipLife').classes('text-green no-underline text-lg')
            with ui.card().classes('px-14 py-5 bg-gray-100 cursor-pointer hover:bg-green-200'):
                ui.link('HipLife').classes('text-green no-underline text-lg')

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
                        with ui.row().classes('flex flex-row justify-between items-center w-1/2'):
                            ui.image("/assets/client.jpeg").classes('object-cover w-full')
                            with ui.column().classes(''):
                                ui.label("Name").classes('text-black text-lg')
                                ui.label("Role")

    show_subscription()
    show_footer()