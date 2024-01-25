

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# APP Language
# ///////////////////////////////////////////////////////////////
class Language(object):
    # LOAD SETTINGS
    # ///////////////////////////////////////////////////////////////
    setup_settings = Settings()
    _settings = setup_settings.items

    # APP PATH
    # ///////////////////////////////////////////////////////////////
    json_file = f"gui/language/{_settings['language']}.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"gui/language/{_settings['language']}.json\" not found! check in the folder {settings_path}")

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Language, self).__init__()

        # DICTIONARY WITH SETTINGS
        self.items = {}

        # DESERIALIZE
        self.deserialize()

        # SERIALIZE
        self.serialize()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        # WRITE JSON FILE
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        # READ JSON FILE
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.items = settings