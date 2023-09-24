
import os

class Config:

    BOT_TOKEN = os.environ.get('5800802984:AAG0EUk9edno0k83LcHcnfwT1FtPtdjdQRk')
    APP_ID = os.environ.get('22404062')
    API_ID = os.environ.get('22404062')
    API_HASH = os.environ.get('162d4eb8c9cbfe558121c6cf41f8df43')

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1961399977').split(',')]

    DOWNLOAD_DIR = 'downloads'
