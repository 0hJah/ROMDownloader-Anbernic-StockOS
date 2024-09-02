import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
import ssl
import zipfile


class Myrient:

    def __init__(self):
        self.__console_list = [
            ("GB", "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy/"),
            ("GBC", "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Color/"),
            ("GBA", "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Advance/"),
            ("PS", "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation/"),
            ("PSP", "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20Portable/"),
            ("NDS", "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20DS%20%28Decrypted%29/"),
            ("N64", "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%2064%20%28BigEndian%29/"),
        ]
        self.__roms_list = []
    
    def get_console(self):
        return self.__console_list

    def get_roms(self, console_idx):
        if len(self.__roms_list) > 0:
            return self.__roms_list
        try:
            context = ssl._create_unverified_context()
            request = Request(self.__console_list[console_idx][1])
            response = urlopen(request, context=context)
            html = response.read().decode("utf8")
            bs = BeautifulSoup(html, features="html.parser")
            items = bs.find(id="list").find_all("tr")
            for item in items[2:]:
                if item is not None:
                    elem = item.find("a")
                    self.__roms_list.append((elem.text, self.__console_list[console_idx][1] + elem["href"]))
            return self.__roms_list
        except:
            return []
    
    def reset_roms_list(self):
        self.__roms_list = []
    
    def download_rom(self, rom_url, rom_path):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            rom_file, _ = urlretrieve(rom_url)
            with zipfile.ZipFile(rom_file, "r") as zip_ref:
                zip_ref.extractall(os.path.dirname(rom_path))
            return True
        except:
            return False


        

