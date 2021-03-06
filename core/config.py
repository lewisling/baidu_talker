# 调用百度语音借口的相关配置
# 参考 http://yuyin.baidu.com/docs/tts/136
class ApiConfig:
    # not None
    client_id = None
    client_secret = None
    # alternative
    spd = None
    pit = None
    vol = None
    per = None
    # const
    tk_url = 'http://tsn.baidu.com/text2audio'
    at_url = 'https://openapi.baidu.com/oauth/2.0/token'
    grant_type = 'client_credentials'
    lan = 'zh'
    ctp = '1'
    # Mac Address of this Device
    cuid = None

    def __init__(self, client_id, client_secret, spd=5, pit=5, vol=5, per=0):
        from tools.net import get_mac_address
        self.cuid = get_mac_address()
        self.client_id = client_id
        self.client_secret = client_secret
        # TODO
        if (not set([spd, pit, vol]).issubset(range(0, 10)) or per not in range(0, 2)):
            raise KeyError('spd, pit, vol, per out of range')
        self.spd = str(spd)
        self.pit = str(pit)
        self.vol = str(vol)
        self.per = str(per)

    # 获取请求 access_token 接口的参数
    def get_at_params(self):
        return {'grant_type': self.grant_type,
                'client_id': self.client_id,
                'client_secret': self.client_secret}

    # 获取语音设置参数
    def get_tk_params(self, text, access_token):
        return {'tex': text,
                'lan': self.lan,
                'tok': access_token,
                'ctp': self.ctp,
                'cuid': self.cuid,
                'spd': self.spd,
                'pit': self.pit,
                'vol': self.vol,
                'per': self.per}


# 软件设置
class SoftConfig:
    # 合成的mp3文件的保存位置
    mp3_dict = r'../output/mp3/'
