class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'l\x9aeX\xbf\xe5\x19\xe0\xcdCb(\xd7G\x17\x13S\xd2\xbfsp\x16\x1b\x05'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
