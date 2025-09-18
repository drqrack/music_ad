from nicegui import ui

@ui.page('/signin')
def show_signin_page():
    ui.label('this is the signin page')