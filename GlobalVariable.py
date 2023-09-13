import os

# 全局参数
# API
BASE_URL = "https://api.moguding.net:9000/"
SIGN_URL = "http://mgd.lftools.ltd:2658/api/"

headers = {
        "Host": "api.moguding.net:9000",
        "accept-language": "zh-CN,zh;q=0.8",
        "user-agent": "Mozilla/5.0 (Linux; Android 7.0; HTC M9e Build/EZG0TF) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.1566.54 Mobile Safari/537.36",
        "sign": "",
        "authorization": "",
        "rolekey": "",
        "content-type": "application/json; charset=UTF-8",
        "accept-encoding": "gzip",
        "cache-control": "no-cache"
}

# 当前版本
version = "20210915"

# 环境变量
PERSONAL_INFORMATION = os.environ.get("PERSONAL_INFORMATION",'information.json')

SERVERPUSHKEY = os.environ.get("SERVERPUSHKEY", "SCT222993Thdr00DdFGikWMXVYcbuvQVnw")  # Server酱推送
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")  # Telegram推送服务Token
TG_USER_ID = os.environ.get("TG_USER_ID", "")  # Telegram推送服务UserId
BARK = os.environ.get("BARK", "")  # bark消息推送服务,自行搜索; secrets可填;形如jfjqxDx3xxxxxxxxSaK的字符串
PUSHPLUS = os.environ.get("PUSHPLUS", "")  # PUSHPLUS消息推送Token
ACCESSTOKEN = os.environ.get("ACCESSTOKEN", "")  # 企业微信access_token     获取地址:https://work.weixin.qq.com/api/doc/90000/90135/91039
CORPID = os.environ.get("CORPID", "")  # 企业ID  （如果已经填写ACCESSTOKEN  则无需填写这个）
CORPSECRET = os.environ.get("CORPSECRET", "")  # 应用的凭证密钥  （如果已经填写ACCESSTOKEN  则无需填写这个）
TOUSER = os.environ.get("TOUSER", "")  # touser指定接收消息的成员  默认为全部
AGENTID = os.environ.get("AGENTID", "")  # agentid企业应用的id
THUMB_MEDIA_ID = os.environ.get("THUMB_MEDIA_ID", "") #企业微信素材库图片id
AUTHOR = os.environ.get("AUTHOR", "") #企业微信文章作者
DING_PUSH_TOKEN = os.environ.get("DING_PUSH_TOKEN","") #钉钉机器人推送设置

