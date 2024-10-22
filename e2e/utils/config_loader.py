import json


def load_config():
    with open("e2e/config/config.json") as config_file:
        return json.load(config_file)


def load_login_data():
    with open("e2e/config/login_data.json") as login_file:
        return json.load(login_file)["user_credentials"]
