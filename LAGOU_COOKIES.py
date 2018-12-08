import requests
import re
url = "https://passport.lagou.com/login/login.html"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get(url, headers=header)

X_Anti_Forge_Token = re.findall(r'window.X_Anti_Forge_Token = \'(.*?)\'', r.text, re.S)
X_Anti_Forge_Code = re.findall(r'window.X_Anti_Forge_Code = \'(.*?)\'', r.text, re.S)
print(X_Anti_Forge_Code, X_Anti_Forge_Token)