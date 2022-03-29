from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
# from pynput.keyboard import Key, Controller as c2
# from pynput.mouse import Button, Controller as c1
import win32api
import win32con
import time
def get_slide_locus(distance):
	#distance += 8
	v = 0
	m = 0.3
	# 保存0.3内的位移
	tracks = []
	current = 0
	mid = distance * 4 / 5
	while current <= distance:
		if current < mid:
			a = 2
		else:
			a = -3
		v0 = v
		s = v0 * m + 0.5 * a * (m ** 2)
		current += s
		tracks.append(round(s))
		v = v0 + a * m
	# 由于计算机计算的误差，导致模拟人类行为时，会出现分布移动总和大于真实距离，这里就把这个差添加到tracks中，也就是最后进行一步左移。
	# tracks.append(-(sum(tracks) - distance * 0.5))
	# tracks.append(10)
	return tracks
#url='https://acs.m.taobao.com:443//gw/mtop.taobao.idle.search.glue/8.0/_____tmd_____/punish?x5secdata=5e0c8e1365474455070961b803bd560607b52cabf5960afff39b64ce58073f7809828a222e0be7bdcaee7d73361ddaa1a29376d0cca44499ae28e940e8cfad9dee5cfa7c5eb40920f3b5e788e84b93944f15dba598f6507c8ab2a036a037d8bc9b1f21d3b21668105d1a94520f2774e41524cc553c9c2b68804d10c0d401ed3245cb0ce36cef9f62cbd52852a03cf8ba461ee819ca12264cfd380e1ff9a318174e5caf42918a01f2ed80fa78c196899f1b03c99860c4ed850fea79b9e5958cde5861e86d30bbe85e06726bc90aa72e6f79a52a883b8d79c21b1904b01749f64f2f7acbadc8157886ad070a1ee53b4f0257f7918a4f2572499cc398910575bb4a39bcaf21bb438351498c3d21f2a8dae0232d72119ccb85c4f5e9ead37afa2a0bc8a5376d5eeb10e4b18bc286a166d1630ba2afb0aa610bf7ac271d0799152c505902274b3176213fa554409d88046e94619198f7b6209761473dbd2e5121d84de52b1850c76473e8a16cf039c12d1ef136eaa76cd060fa7d83f7cf7849fe8a49772cd482ee48ae44b995820b22c8bccd2c5f016142db449be949dec823b11f74629e556dbe25b1fdf039cb616397cf6ab1fb10c2f11086c51a8968065d8ee431&x5step=2&http_referer=https://sec.taobao.com/'
url = 'https://login.taobao.com/member/login.jhtml?style=mini&css_style=b2b&from=b2b&full_redirect=true&redirect_url=https://login.1688.com/member/jump.htm?target=https://login.1688.com/member/marketSigninJump.htm?Done=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&reg= http://member.1688.com/member/join/enterprise_join.htm?lead=http://login.1688.com/member/taobaoSellerLoginDispatch.htm&leadUrl=http://login.1688.com/member/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument('--headless')  # # 浏览器不提供可视化页面
chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速,GPU加速可能会导致Chrome出现黑屏，且CPU占用率高达80%以上
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage') 
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--kiosk') 
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
brower = webdriver.Chrome(chrome_options =chrome_options, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
brower.set_window_size(1920, 1080)
# brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  # "source": """
	# window.navigator.chrome = { runtime: {},  };
	# Object.defineProperty(navigator, 'webdriver', {
	  # get: () => undefined
	# });
	# Object.defineProperty(navigator, 'languages', { 
	  # get: () => ['en-US', 'en'] 
	# });
	# Object.defineProperty(navigator, 'plugins', { 
	  # get: () => [1, 2, 3, 4, 5,6 ]
	# });
  # """
# })
with open(r'C:\Users\RUSSIAVK\eclipse-workspace\regking\regking-core\src\main\resources\lib\stealth.min.js') as f:
	js = f.read()
brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
}) 
brower.get(url)
# user = brower.find_element(By.ID, 'fm-login-id').send_keys('asdasd')#13981980452
# passw = brower.find_element(By.ID, 'fm-login-password').send_keys('10793300d')
# time.sleep(1)
# brower.find_element(By.CLASS_NAME, 'fm-submit').click()
# time.sleep(0.7)


# try:
	# frame=brower.find_element(By.ID, 'baxia-dialog-content')
	# x, y =frame.location.values()
	# x*=2
	# y*=2
	# brower.switch_to.frame(frame)
# except Exception as e:
	# for i in range (6):
		# brower.find_element(By.CLASS_NAME, 'fm-submit').click()
		# time.sleep(0.5)
	# x,y=70,218
# finally:
	
#mouse=c1()

count = 0
while True:
	time.sleep(2)
	slider = brower.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
	x, y =slider.location.values()
	if slider:
		distance = 260
		# actions = webdriver.ActionChains(brower)
		# actions.click_and_hold(slider) # 点击并持续开始拖拽
		# actions.pause(0.4) # 设置按下停顿时间 模拟人为操作
		# # 横向移动 300 纵向0
		# # +5 -10 是为了模拟人为操作  拖动超过了  然后再拖回来
		# l=get_slide_locus(distance)
		# for i in l:
			# actions.move_by_offset(i, 0)
		# actions.pause(0.6)
		# actions.release() # 松开鼠标
		# actions.perform() # 结束动作#
		
		print('x'+str(x))
		print('y'+str(y))
		# mouse.position = (x, y)
		# mouse.press(Button.left)
		# tracks=get_slide_locus(distance)
		# for i in tracks:
			# mouse.move(x+i, y)
		# mouse.release(Button.left)
		win32api.SetCursorPos([x,y])    #为鼠标焦点设定一个位置
		time.sleep(0.1)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
		tracks=get_slide_locus(distance)
		xx=x
		for i in tracks:
			print('i：'+str(i))
			print('x：'+str(i))
			print('y：'+str(y))
			print('\n')
			xx+=i
			win32api.SetCursorPos([xx,y])
		time.sleep(0.1)	
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
		try:
			WebDriverWait(brower, 1).until(ec.presence_of_element_located((By.ID, 'nc_1_refresh1')))
			brower.find_element(By.ID, 'nc_1_refresh1').click()
			print(f'重试第 {count} 次数')
			count += 1
		except Exception as e:break
	
# brower.switch_to.default_content()
# brower.find_element(By.CLASS_NAME, 'password-login')
# time.sleep(2)
# brower.switch_to.default_content()
# print('登录成功')
#brower.quit()
