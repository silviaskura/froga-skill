from mycroft import MycroftSkill, intent_file_handler


class Froga(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('froga.intent')
    def handle_froga(self, message):
        self.speak_dialog('froga')


def create_skill():
    return Froga()

