# _*_ coding:UTF-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import random

path_web_page_screenshot = '.\\screenshot\\page.png'
path_captcha_image = '.\\screenshot\\captcha.png'
path_ocr_result_file = '.\\screenshot\\ocr_result'

# 根节点 ：5488779
# M1 : 5694975,6181496
# M2 ：5701889

account_set = [5488779,5694975,6181496,5701889]
seed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
phone_number_base = [13000000000, 13100000000, 13200000000, 13300000000, 13400000000, 13500000000, 13600000000, 13700000000, 13800000000, 13900000000, 18100000000, 18600000000, 18700000000, 15100000000, 15700000000]

def url_generator():
	return 'http://bit93.com/i/' + str(account_set[random.randint(0,len(account_set) - 1)])

def password_generator():
	char_set = []
	for i in range(8):
		char_set.append(random.choice(seed))
	pswd = ''.join(char_set)
	return pswd

def phone_number_generator():
	return str(phone_number_base[random.randint(0,len(phone_number_base) - 1)] + random.randint(00000000, 99999999))


def get_chrome_options():
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--start-maximized')
	return chrome_options

def capture_verification_code_image(webdriver):
	webdriver.get_screenshot_as_file(path_web_page_screenshot)
	im = Image.open(path_web_page_screenshot)
	img_size = im.size
	#print("screenshot image size is {}".format(img_size))
	region = im.crop((1160, 674, 1160 + 140, 674 + 61))
	region.save(path_captcha_image)
	return orc_captcha_image()
	
def orc_captcha_image():
	cmd = 'tesseract ' + path_captcha_image + ' ' + path_ocr_result_file  + ' -l fontyp'
	#print cmd
	os.system(cmd)
	with open(path_ocr_result_file + '.txt') as f:
		return f.read().replace(' ','').replace('\n','').replace('\r','')
		

	

def start(_webdriver):
	
	url = url_generator()
	phone = phone_number_generator()
	pswd = password_generator()
	
	_webdriver.maximize_window()
	_webdriver.get(url)
	_webdriver.set_window_size(1920,1080)
	try:
		_webdriver.find_element_by_id('phone').send_keys(phone)
		_webdriver.find_element_by_id('User_password').send_keys(pswd)
		_webdriver.find_element_by_id('User_password2').send_keys(pswd)
		captcha = capture_verification_code_image(_webdriver)
		_webdriver.find_element_by_id('captcha').send_keys(captcha)
		_webdriver.find_element_by_id('captcha').send_keys(Keys.ENTER)
		print phone,pswd,captcha,url
	
		start(_webdriver)
	except:
		print 'regist succes'
		try:
			_webdriver.find_element_by_xpath('//*[@id="nav"]/li[4]/a').click()
			start(_webdriver)
		except:
			print 'exit or Restart!!!'
			_webdriver.quit()
			_driver = webdriver.Chrome('.\chromedriver.exe',chrome_options = get_chrome_options())
			start(_driver)

	
driver = webdriver.Chrome('.\chromedriver.exe',chrome_options = get_chrome_options())
start(driver)





