
import os

class Config:

    BOT_TOKEN = os.environ.get('6004366181:AAHszsmk9lVj2NaddTz-v5ff2sW9dr6LVXo')
    APP_ID = os.environ.get('13125592')
    API_HASH = os.environ.get('4c08ab6b656c6e18fa3c68508ef5e5b0')

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1165215979').split(',')]

    DOWNLOAD_DIR = 'downloads'
