'''BiliBili Helper Config Information

'''
from Exception import ConfigException

START_URL     = 'https://passport.bilibili.com/login'
OAUTH_KEY_URL = 'https://passport.bilibili.com/qrcode/getLoginUrl'

QR_LOGIN_URL   = 'https://account.bilibili.com/qrcode/login?oauthKey=%s'
LOGIN_INFO_URL = 'https://passport.bilibili.com/qrcode/getLoginInfo'

CAPTCHA_URL   = 'https://passport.bilibili.com/captcha'

VIDEO_URL = 'http://www.bilibili.com/video/av%s/'
LIVE_URL  = 'http://live.bilibili.com/%s'

def QrLoginUrl(oAuthKey = None):
    if oAuthKey is None:
        raise ConfigException('oAuthKey parameter must be specified')
    else:
        if len(oAuthKey) != 32:
            raise ConfigException('oAuthKey format error, length is not 32')
        return QR_LOGIN_URL % oAuthKey

def videoUrl(av = None):
    if av is None:
        raise ConfigException('avCode parameter must be specified')
    if not isinstance(av, int):
        raise ConfigException('avCode must be int type')
    return VIDEO_URL % av
