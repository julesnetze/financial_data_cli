from view.error_message import error_message
from view.options_messages import options_menu
from view.welcome_message import welcome_message


class MessageController:

    def render_welcome_message(self):
        return welcome_message()

    def render_options_menu(self):
        return options_menu()

    def render_error_message(self):
        return error_message()