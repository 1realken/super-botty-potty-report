import requests
import random
from requests.sessions import session
from colorama import Fore, Back, Style
import time
report = requests.session()
citylist = ['Moscow', 'Lyon', 'Cologne', 'Valencia', 'Kyiv', 'Milan', 'Brussels', 'Minsk', 'Antwerp', 'Bologna', 'Warsaw', 'Lisbon', 'Seville', 'Hamburg', 'Osio', 'Belgrade', 'Riga']
countrylist = ['GB', 'IT', 'CZ', 'DK', 'EE', 'EL', 'ES', 'FR', 'HR', 'LV']
while True:
    report.post("https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36&channel=tiktok_web&cookie_enabled=true&current_region=US&device_id=7102427461703419394&device_platform=web_pc&focus_state=true&from_page=user&history_len=3&is_fullscreen=false&is_page_visible=true&lang=en&nickname=David Degea&object_id=6905304069154456578&os=mac&owner_id=6905304069154456578&priority_region=&reason=1001&referer=&region=" + random.choice(countrylist) + "&report_type=user&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuREegK8dNya80Bzb9X_CuN8XQQT6AIMp6_Mk821R0ljSUJ8CnjtwmMAlHEqeoX0I&target=6905304069154456578&tz_name=Europe/" + random.choice(citylist) + "&webcast_language=en&msToken=PIkSQMU0a5aLhL9F1pqD7yt8v1hhkf-x40IED4lz1m90L9vWIZtDNFk7Ep--TJ07WejxV797Ippu6JOVM0eptDDUlYjdq-jJVACHCt6S5ADweVtZcUqVzFIVFf4SOLIettNf-PY=&X-Bogus=DFSzs3juryzANcKDSfGGRK/F6qH5&_signature=_02B4Z6wo00001YFpp3gAAIDA-adMfUS-eQ2BaevAAALha8")
    print(Back.GREEN + 'Suckcess!' + Style.RESET_ALL + ' Report dun')
    time.sleep(15)
