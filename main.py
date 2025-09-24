from nicegui import ui, app
from pages.home import *
from pages.about import *
from pages.view_advert import *
from pages.vendor.edit_advert import *
from pages.artist_create_advert import *
from pages.vendor.record_label_create_advert import *
from pages.vendor.dashboard import *
from pages.vendor.adverts import *
from pages.signin import *
from pages.artist_signup import *
from pages.record_label_signup import *
from pages.contact import *
from pages.artist_profile import *

app.add_static_files("/assets", "assets")

ui.run(title="Kolkit", favicon="")