from nicegui import ui, app
from pages.home import *
from pages.about import *
from pages.view_advert import *
from pages.edit_advert import *
from pages.create_advert import *
from pages.signin import *
from pages.signup import *

app.add_static_files("/assets", "assets")

ui.run()