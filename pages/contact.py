from nicegui import ui
from components.header import show_header
from components.subscription import show_subscription
from components.footer import show_footer

@ui.page('/contact')
def show_contact_page():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    show_header()
    with ui.row().classes('w-[100%] h-full bg-gray-100 flex flex-row justify-between items-center text-gray-700 py-20 px-10 mt-10').style('font-family: "Josefin Sans", sans-serif'):
        with ui.row().classes('w-1/3 flex flex-row justify-center items-center'):
            with ui.element('div').classes('w-1/4 p-4 bg-white flex justify-center items-center'):
                ui.html('<i class="fa-solid fa-phone"></i>').classes('text-green text-2xl')
            with ui.column().classes('w-1/2 flex flex-col'):
                ui.label('Call Us:').classes('font-bold text-2xl')
                ui.label("+233 55 071 6364")

        with ui.row().classes('w-1/3 flex flex-row justify-center items-center'):
            with ui.element('div').classes('w-1/4 p-4 bg-white flex justify-center items-center'):
                ui.html('<i class="fa-solid fa-envelopes-bulk"></i>').classes('text-green text-2xl')
            with ui.column().classes('w-1/2 flex flex-col'):
                ui.label('Email:').classes('font-bold text-2xl')
                ui.label("kolkit@mail.com")

        with ui.row().classes('w-1/3 flex flex-row justify-center items-center'):
            with ui.element('div').classes('w-1/4 p-4 bg-white flex justify-center items-center'):
                ui.html('<i class="fa-solid fa-location-dot"></i>').classes('text-green text-2xl')
            with ui.column().classes('w-1/2 flex flex-col'):
                ui.label('Address:').classes('font-bold text-2xl')
                ui.label("Buro, Labone-Osu")

    with ui.element("main").classes('w-full h-full bg-gray-100 flex flex-row justify-center items-center py-20').style('font-family: "Josefin Sans", sans-serif'):
        with ui.element('div').classes('w-[40%] bg-gray-100 px-12 py-4'):
            ui.label("Get in Touch").classes('text-3xl py-4 font-bold text-gray-700')
            ui.separator().classes('w-[10%] h-1 bg-green mb-8')
            ui.input(placeholder="Name:").classes('bg-white px-4 mb-1').props('borderless')
            ui.input(placeholder="Email:").classes('bg-white px-4 mb-1').props('borderless')
            ui.input(placeholder="Subject:").classes('bg-white px-4 mb-1').props('borderless')
            ui.textarea(placeholder="Message").classes('bg-white px-4 mb-4').props('borderless')
            ui.button(text="Send Message").props('flat dense no-caps').classes('bg-green text-white w-full py-4')

        with ui.element('div').classes('w-[40%] px-10'):
            ui.html('<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d15883.291381306237!2d-0.2713955!3d5.59317755!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sgh!4v1758378697242!5m2!1sen!2sgh" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>').classes('w-80%')

    show_subscription()
    show_footer()