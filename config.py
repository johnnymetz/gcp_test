class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'l\x9aeX\xbf\xe5\x19\xe0\xcdCb(\xd7G\x17\x13S\xd2\xbfsp\x16\x1b\x05'
    API_KEY = '0050344aa077ab4bebd2bd0c63e18393'
    NUMBER_OF_DAYS = 7


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    NUMBER_OF_DAYS = 2


class TestingConfig(BaseConfig):
    TESTING = True
    NUMBER_OF_DAYS = 2


class ProductionConfig(BaseConfig):
    pass
