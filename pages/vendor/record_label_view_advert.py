from nicegui import ui
from components.header import show_header
from components.subscription import show_subscription
from components.footer import show_footer
import requests
from utils.api import base_url


@ui.page("/vendor/record_label_view_advert")
def show_view_advert():
    show_header()

    advert_id = ui.context.client.request.query_params.get("id")
    response = requests.get(url=f"{base_url}/adverts/{advert_id}")
    # print(response.status_code, response.content)
    if response.status_code == 200:
        json_data = response.json()
        # print(json_data)
        advert = json_data["data"]

    with ui.element("main").classes(
        "w-full h-screen flex flex-col justify-center items-center py-20 px-20"
    ).style('font-family: "Stoke", serif; font-style: normal;'):
        with ui.row().classes(
            "w-[95%] h-[40%] bg-gray-100 flex flex-row justify-between items-center px-10 py-10 mb-4"
        ):
            with ui.row().classes("flex flex-row justify-center w-1/2 h-full"):
                # with ui.element("div").classes("w-[30%] h-full bg-[url('/assets/pos.jpg')] bg-cover bg-center"):
                # pass
                ui.image("/assets/mixer.jpeg").classes(
                    "w-[30%] h-full rounded-lg object-contain"
                )

                with ui.column().classes(""):
                    ui.label(text=advert["title"]).classes("text-xl font-semibold")
                    ui.label(text=advert["company"]).classes("text-green font-bold")
                    with ui.row().classes("text-gray-700"):
                        ui.label("Kumasi, Ghana")
                        ui.label("+233 55 071 6364")
            with ui.column().classes("flex flex-col justify-between h-full"):
                with ui.row().classes(
                    "flex flex-row justify-center items-center gap-0"
                ):
                    ui.label(text=advert["price"]).classes("text-xl font-semibold")
                    ui.label("/monthly").classes("text-gray-700")
                ui.button("Apply Now").props("flat dense no-caps").classes(
                    "bg-green text-white px-4 py-2"
                )

        with ui.element("div").classes("text-gray-700 w-[95%] "):
            ui.label(text=advert["description"]).classes("text-2xl font-bold text-gray-900 py-5")
            ui.label(
                "It is a long established fact that a reader will be distracted the readable content of page when looking atits layout. The point of using is that has more-or-less normal a distribution of letters, as opposed to usin content publishing packages web page editors. It is a long established fact that a reader will be distracts by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that has look like readable publishing packages and web page editors."
            )
            ui.label(
                "It is a long established fact that a reader will be distracted the readable content of a page when looking atits layout. The point of using is that has more-or-less normal a distribution of letters, as opposed to usin content publishing packages web page editors."
            )
    # Left-Side
    with ui.element("section").classes(
        "w-full h-full flex flex-row justify-between items-center px-20 text-gray-700 mb-8"
    ).style('font-family: "Stoke", serif; font-style: normal;'):
        with ui.element("div").classes("w-[70%]"):
            ui.label("Responsibilities").classes("text-2xl font-bold text-gray-900 py-5")
            with ui.column().classes('py-1 mb-10'):
                ui.label("Developing custom themes (WordPress.org & ThemeForest Standards).")
                ui.label("Creating reactive website designs.")
                ui.label("Working under strict deadlines.")
                ui.label("Develop page speed optimized themes.")
            
            ui.label("Requirements").classes("text-2xl font-bold text-gray-900 py-5")
            with ui.column().classes('py-1 mb-10'):
                ui.label("Having approved theme/s on ThemeForest will be given high preference.")
                ui.label("Strong knowledge of WordPress Theme Standards.")
                ui.label("Ability to convert HTML templates into fully functional WordPress themes.")
                ui.label("Good knowledge in O OP PHP and front-end stuffs like HTML, CSS, JS, jQuery, etc.")
                ui.label("Ability to debug and fix bugs arising from other developer’s code.")
                ui.label("Sense of humor")
                ui.label("Moderate knowledge in WordPress Core APIs like options, metadata, REST, hooks, settings, etc.")
                ui.label("Hard worker and passionate – we are growing super fast.")
            
            ui.label("Educational Requirements").classes("text-2xl font-bold text-gray-900 py-5")
            with ui.column().classes('py-1 mb-10'):
                ui.label("It doesn’t matter where you went to college or what your CGPA was as long as you are smart, passionate, ready to work hard, and have fun.")
                

        # Right-Side
        with ui.element('div').classes('w-[30%]'):
            with ui.element('div').classes('w-full bg-gray-100 px-10 mb-10'):
                ui.label("Summary").classes("text-2xl font-bold text-gray-900 py-5")
                ui.separator().classes('w-[10%] h-1 bg-green mb-8')
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Job Type ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("Full Time").classes("text-green")
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Category ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("Engineering")
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Posted ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("21 Sep, 2025")
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Experience ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("5 years")
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Qualification ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("BSC, MSC")
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Level ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("Senior")
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Applied ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("14 applicants")
                with ui.row().classes('flex flex-row justify-between items-center py-2'):
                    ui.label("Deadline ").classes('font-semibold text-black')
                    ui.label(":")
                    ui.label("20 Nov, 2025").classes('text-red')

            with ui.element('div').classes('w-full bg-gray-100 px-10'):
                ui.label("Share With").classes("text-2xl font-bold text-gray-900 py-5")
                ui.separator().classes('w-[10%] h-1 bg-green mb-8')
                with ui.row().classes('flex justify-between text-lg py-2'):
                    ui.html('<i class="fa-brands fa-facebook-f"></i>')
                    ui.html('<i class="fa-brands fa-x-twitter"></i>')
                    ui.html('<i class="fa-brands fa-instagram"></i>')
                    ui.html('<i class="fa-brands fa-tiktok"></i>')
                    ui.html('<i class="fa-brands fa-whatsapp"></i>')

    # elif response.status_code == 422:
    #     ui.label(text="Something went wrong!")
    
    show_subscription()
    show_footer()
