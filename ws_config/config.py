import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv()
print(f"- .env: {find_dotenv()}")
print(f"- WS_CONFIG_TYPE: {os.environ.get('WS_CONFIG_TYPE')}")
print(f"- FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")
print(f"- Config File: {os.path.join(os.environ.get('CONFIG_PATH_WORKSTATION'), os.environ.get('CONFIG_FILE_NAME'))}")
print(f"- PROJECT_RESOURCES: {os.environ.get('PROJECT_RESOURCES')}")


match os.environ.get('WS_CONFIG_TYPE'):
    case 'dev' | 'prod':
        config_path = os.environ.get('CONFIG_PATH_SERVER')
        config_file_name = os.environ.get('CONFIG_FILE_NAME')
        with open(os.path.join(config_path, config_file_name)) as config_json_file:
            config_json_dict = json.load(config_json_file)
    case _:
        config_path = os.environ.get('CONFIG_PATH_WORKSTATION')
        config_file_name = os.environ.get('CONFIG_FILE_NAME')
        with open(os.path.join(config_path, config_file_name)) as config_json_file:
            config_json_dict = json.load(config_json_file)

# NOTE:
# config.json: config_json_dict.get()
# .env: os.environ.get()

class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = config_json_dict.get('SECRET_KEY')
        self.WEB_ROOT = os.environ.get('WEB_ROOT')
        self.API_ROOT = os.environ.get('API_ROOT')
        self.APPLE_SERVICE_11_ROOT = os.environ.get('APPLE_SERVICE_11_ROOT')
        self.SCHEDULER_SERVICE_11_ROOT = os.environ.get('SCHEDULER_SERVICE_11_ROOT')
        
        # Database
        self.PROJECT_RESOURCES = os.environ.get('PROJECT_RESOURCES')
        # self.DB_MYSQL_ROOT = os.environ.get('DB_MYSQL_ROOT')
        self.MYSQL_USER = config_json_dict.get('MYSQL_USER')
        self.MYSQL_PASSWORD = config_json_dict.get('MYSQL_PASSWORD')
        self.MYSQL_SERVER = config_json_dict.get('MYSQL_SERVER')
        self.MYSQL_DATABASE_NAME = config_json_dict.get('MYSQL_DATABASE_NAME')
        self.SQL_URI_WHAT_STICKS_DB = f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}/{self.MYSQL_DATABASE_NAME}"

        # database helper files
        self.DATABASE_HELPER_FILES = os.path.join(self.PROJECT_RESOURCES,"database_helpers")
        self.APPLE_HEALTH_DIR = os.path.join(self.DATABASE_HELPER_FILES,"apple_health")# <-- store Apple Health compressed
        self.DATAFRAME_FILES_DIR = os.path.join(self.DATABASE_HELPER_FILES,"dataframe_files")# <-- store pkl files for dashbaord data item
        self.USER_LOCATION_JSON = os.path.join(self.DATABASE_HELPER_FILES,"user_location_json")
        self.DB_UPLOAD = os.path.join(self.DATABASE_HELPER_FILES,"db_upload")# <-- move pickle or csv files dircetly via CyberDuck or other FTP here then, use website gui to manage upload.

        # wsios_helper files
        self.WS_IOS_HELPER_FILES = os.path.join(self.PROJECT_RESOURCES,"ws_ios_helpers")
        self.DASHBOARD_FILES_DIR = os.path.join(self.WS_IOS_HELPER_FILES,"dashboard_table_obj_files")# <-- store pkl files for dashbaord data item
        self.DATA_SOURCE_FILES_DIR = os.path.join(self.WS_IOS_HELPER_FILES,"data_source_obj_files")# <-- store pkl files for dashbaord data item

        # user files
        self.USER_FILES = os.path.join(self.PROJECT_RESOURCES,"user_files")
        self.DAILY_CSV = os.path.join(self.USER_FILES,"daily_csv")
        self.RAW_FILES_FOR_DAILY_CSV = os.path.join(self.USER_FILES,"raw_files_for_daily_csv")

        # website files
        self.WEBSITE_FILES = f"{self.PROJECT_RESOURCES}website_files"# <-- store website files
        self.DIR_WEBSITE_UTILITY_IMAGES = os.path.join(self.WEBSITE_FILES,"website_utility_images")# <-- store blog word documents
        self.DIR_WEBSITE_VIDEOS = os.path.join(self.WEBSITE_FILES,"website_videos")# <-- store videos

        
        # paramters for database/dataframe files
        self.APPLE_HEALTH_QUANTITY_CATEGORY_FILENAME_PREFIX = "AppleHealthQuantityCategory"
        self.APPLE_HEALTH_WORKOUTS_FILENAME_PREFIX = "AppleHealthWorkouts"

        #Email stuff
        self.MAIL_SERVER = config_json_dict.get('MAIL_SERVER_GMAIL')
        self.MAIL_PORT = config_json_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = config_json_dict.get('EMAIL_WHAT_STICKS_GMAIL')
        self.MAIL_PASSWORD = config_json_dict.get('EMAIL_WHAT_STICKS_GMAIL_PASSWORD')
        # self.ACCEPTED_EMAILS = config_json_dict.get('ACCEPTED_EMAILS')
        self.LIST_NO_CONFIRMASTION_EMAILS = config_json_dict.get('LIST_NO_CONFIRMASTION_EMAILS')

        #API
        self.WS_API_PASSWORD = config_json_dict.get('WS_API_PASSWORD')

        #Admin stuff
        self.ADMIN_EMAILS = config_json_dict.get('ADMIN_EMAILS')
        self.DIR_LOGS = os.path.join(self.PROJECT_RESOURCES,"logs")
        self.ACTIVATE_TECHNICAL_DIFFICULTIES_ALERT = config_json_dict.get('ACTIVATE_TECHNICAL_DIFFICULTIES_ALERT') == "True"

        #Captcha
        # self.SITE_KEY_CAPTCHA = env_support_dict.get('SITE_KEY_CAPTCHA')
        # self.SECRET_KEY_CAPTCHA = env_support_dict.get('SECRET_KEY_CAPTCHA')
        self.VERIFY_URL_CAPTCHA = 'https://www.google.com/recaptcha/api/siteverify'

        #Visual Crossing - weather
        self.VISUAL_CROSSING_BASE_URL = config_json_dict.get('VISUAL_CROSSING_BASE_URL')
        # https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/
        # self.VISUAL_CROSSING_BASE_URL = "https://weather.visualcrossing.com"
        self.VISUAL_CROSSING_TOKEN = config_json_dict.get('VISUAL_CROSSING_TOKEN')
        self.VISUAL_CROSSING_UNIT_GROUP = config_json_dict.get('VISUAL_CROSSING_UNIT_GROUP')

        #Nominatim API - location
        self.NOMINATIM_API_URL = "https://nominatim.openstreetmap.org"
        # f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"




class ConfigWorkstation(ConfigBasic):
    
    def __init__(self):
        super().__init__()
        
        #API
        self.API_URL = config_json_dict.get("WS_API_URL_BASE_WORKSTATION")
        self.API_URL_LOCAL = config_json_dict.get("WS_API_URL_BASE_WORKSTATION")
        self.WEB_URL = config_json_dict.get("WS_WEB_URL_BASE_WORKSTATION")
        self.WEB_URL_LOCAL = config_json_dict.get("WS_WEB_URL_BASE_WORKSTATION")

    DEBUG = True

class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()

        #API
        self.API_URL = config_json_dict.get("WS_API_URL_BASE_DEVELOPMENT")
        self.API_URL_LOCAL = config_json_dict.get("WS_API_URL_BASE_DEV_LOCAL")
        self.WEB_URL = config_json_dict.get("WS_WEB_URL_BASE_DEVELOPMENT")
        self.WEB_URL_LOCAL = config_json_dict.get("WS_WEB_URL_BASE_DEV_LOCAL")

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

        #API
        self.API_URL = config_json_dict.get("WS_API_URL_BASE_PRODUCTION")
        self.API_URL_LOCAL = config_json_dict.get("WS_API_URL_BASE_PROD_LOCAL")
        self.WEB_URL = config_json_dict.get("WS_WEB_URL_BASE_PRODUCTION")
        self.WEB_URL_LOCAL = config_json_dict.get("WS_WEB_URL_BASE_PROD_LOCAL")

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
