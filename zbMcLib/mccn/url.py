import zbToolLib as f

import hashlib
import time
from urllib.parse import urlparse


def decryptUrl(url: str):
    """
    解密来自g79.gdl.netease.com的链接
    :param url: 链接
    :return: 带有key1和key2的链接
    """
    if "g79.gdl.netease.com" not in url:
        raise  Warning("该链接并非来自可解密的域名，很可能无法正常解密。")
    if "?" in url:
        url = url.split("?")[0]
    private_key = "mEE7Cot48r9j2AvEL2N6jpXEc"
    current_time = int(time.time())
    expiration_time = current_time + 60*60*24*365
    expiration_time_hex = hex(expiration_time)[2:]

    signature = private_key + urlparse(url).path + expiration_time_hex
    key1 = hashlib.md5(signature.encode()).hexdigest()
    return f"{url}?key1={key1}&key2={expiration_time_hex}"
