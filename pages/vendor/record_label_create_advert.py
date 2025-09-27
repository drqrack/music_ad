from nicegui import ui, run, app
import requests
from utils.api import base_url
from components.sidebar import show_sidebar

_create_advert_btn: ui.button = None


def _run_create_advert(data, files, token):
    return requests.post(
        url=f"{base_url}/adverts",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {token}"},
    )

# save the uploaded image
_advert_image = None

def _handle_image_upload(advert):
    global _advert_image
    _advert_image = advert.content


async def _post_advert(data, files):
    _create_advert_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_create_advert, data, files, app.storage.user.get("access_token"))
    print(response.status_code, response.content)
    _create_advert_btn.props(remove="disable loading")
    if response.status_code == 200:
        ui.notify(message="Adverts added successfully", type="positive")
        return ui.navigate.to("/vendor/dashboard")
    elif response.status_code == 422:
        return ui.notify(
            message="Please ensure all inputs are filled!", type="negative"
        )
    # elif response.status_code == 403:
    #     return ui.notify(
    #         message="Please ensure all inputs are filled!", type="warning"
    #     )


@ui.page("/vendor/record_label_create_advert")
def show_record_label_create_advert():
    global _create_advert_btn
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">'
    )

    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.row().classes("w-full h-screen flex flex-row justify-between items-center"):
        with ui.column().classes("w-[20%] h-full"):
            show_sidebar()
        with ui.column().classes("w-[80%] h-full"):
            with ui.element("main").classes(
                "w-full h-full flex flex-col justify-center items-center p-4"
            ).style('font-family: "Josefin Sans", sans-serif'):
                with ui.card().classes(
                    "w-[40%] flex flex-col justify-center items-center shadow-lg bg-gray-100"
                ):
                    ui.label("kolkit").style(
                        'font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normal'
                    ).classes("text-xl font-bold text-gray-800")
                    ui.label("Create an Ad").classes("text-xl font-bold text-green-900")
                    ui.separator().classes("w-[10%] h-0.5 bg-green-800")

                    ui.button(
                        text="Record Label",
                        on_click=lambda: ui.navigate.to("/record_label_create_advert"),
                        icon="business_center",
                    ).props("flat dense no-caps").classes(
                        "bg-green text-white px-2 py-2 mb-2"
                    )

                    advert_title = (
                        ui.input(label="Title", placeholder="Title of advert")
                        .classes("w-full bg-white px-2")
                        .props("borderless")
                    )
                    company_name = (
                        ui.input(
                            label="Company", placeholder="Enter the name of your label"
                        )
                        .classes("w-full bg-white")
                        .props("borderless")
                    )
                    advert_description = (
                        ui.textarea(
                            label="Description", placeholder="Enter the details"
                        )
                        .classes("w-full bg-white px-2")
                        .props("borderless")
                    )
                    advert_price = (
                        ui.number(label="Price", placeholder="Enter the price")
                        .classes("w-full bg-white px-w")
                        .props("borderless")
                    )

                    advert_job_type = ui.select(
                        options=["Job-type", "Full-time", "Part-time", "Contract"],
                        label="Job Type",
                        value="Job-type",  # Set a default value
                    ).classes("w-full bg-white")
                    # advert_job_type = ui.input(placeholder="E.g Full-time, Part-Time, Contract").classes('w-full bg-white')
                    ui.upload(auto_upload=True, on_upload=_handle_image_upload).classes(
                        "w-full mb-4"
                    ).props("color=green")
                    _create_advert_btn = ui.button(
                        text="Post",
                        on_click=lambda: _post_advert(
                            data={
                                "title": advert_title.value,
                                "company": company_name.value,
                                "description": advert_description.value,
                                "price": advert_price.value,
                                "job_type": advert_job_type.value,
                            },
                            files={"image": _advert_image},
                        ),
                    ).props("flat dense").classes(
                        "bg-green text-white w-[80%] py-2"
                    ).style(
                        "border: solid 2px gray"
                    )
