from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import base64
import time
import os

# TealRed先生のデッキ画像ジェネレータ（このサービスが死んだら終わりです）
# base_urlの後にデッキコードを続けてアクセスするとデッキコードが入力された状態になる（2021.12.12現在）
base_url = "https://tealred.net/archives/deckimage-generator/?ja_jp#"

# 環境に応じて設定を変更すること
options = Options()
options.binary_location = '/usr/bin/firefox'
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 画像をキャッシュしておくフォルダ
cache_dir = "/tmp"

def fetchDeckImage(deckcode):
    # キャッシュの確認
    file_name = f'{cache_dir}/{deckcode}.png'
    if os.path.exists(file_name):
        return file_name

    driver = webdriver.Firefox(options=options, log_path=os.path.devnull)
    wait = WebDriverWait(driver, 10)
    url = f'{base_url}{deckcode}'
    driver.get(url)
    wait.until(EC.presence_of_all_elements_located)

    # デッキ画像ジェネレータのバグでURLにアクセスした直後は画像が表示されないため、更新ボタンを押す
    # sleepは画像が描画し終わるのを待つ
    driver.execute_script('javascript:change_all();')
    time.sleep(1)

    # Canvasからデッキ画像を取得する
    xpath = '//*[@id="canvas"]'
    img = driver.find_element_by_xpath(xpath)
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", img)
    # デコード
    canvas_png = base64.b64decode(canvas_base64)
    
    # ファイルに保存しないとDiscordに送信できないので一度ローカルに保存
    with open(file_name, 'wb') as f:
        f.write(canvas_png)

    return file_name
    