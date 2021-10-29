# Author: Athul Prakash
# Selenium based responder [temporary support as classes changes on whatsapp web]

import argparse
from time import sleep
from selenium import webdriver, common
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from controller import createAndRun, getData
from os import system
import logging
import json
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename="logs.log")


#################################################
#		    		Variables					#
#################################################

unread_icon = "_23LrM"
body_path = "/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[3]"


###############################################################################
#                          A`RGUMENT PARSING START                             #
###############################################################################

parser = argparse.ArgumentParser(prog="app", description="Options for customizing program")
parser.add_argument('-n', '--mbr', type=int, metavar="", help="Number of messages to ignore before sending the auto response again")
parser.add_argument('-m', '--message', type=str, metavar="", help="Message to display as an automated response")
parser.add_argument('-b', '--browser', type=str.lower, metavar="", help="Browser to use Whatsapp Web on [Chrome is default]", choices=['chrome', 'firefox'])

parser.add_argument('-M', '--mode',type=str, metavar="",help="Reply mode, [Auto is default]",choices=['auto','manual'])
parser.add_argument('-i', '--ignore',type=str, metavar="",help="File with list of people to ignore")
parser.add_argument('-c', '--custom',type=str, metavar="",help="Json file with messages to specific people")
parser.add_argument('-r', '--remember',type=str, metavar="",help="True if you want to make it a permenent session Default: True")
parser.add_argument('-p', '--profile',type=str, metavar="",help="Firefox profile path (chrome not supported)")


args = vars(parser.parse_args())

mode = 'auto' if args['mode'] is None else args['mode'].lower()

# Get --mbr command line argument value or assign a default
messages_before_response = 3 if args['mbr'] is None else args['mbr']


prof = None if args['profile'] is None else args['profile']


#Ignored People

ignoredPeople = []

if args['ignore']:
    with open(args['ignore']) as f:
        ignored = f.read()
        for people in ignored.split('\n'):
            ignoredPeople.append(people.lower())
    print(f"Ignoring: \n{ignoredPeople}")



if args['custom']:
	with open(args['custom']) as f:
		customMessages = json.load(f)


###############################################################################
#                           AUTO RESPONSE LOGIC                               #
###############################################################################

# Create a list that holds the names of people who message
# Names will be duplicated if the person sends multiple messages
# Once the count of duplicates for a name equals to --mbr value,
# all the duplicates will be removed from the list and only one stays

selected_browser = args['browser']

try:		
		# Support for Chromeium
	if (selected_browser is None) or (selected_browser == 'chrome'):
		browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
	# Support for Firefox
	elif selected_browser.lower() == 'firefox':
		if prof!=None:
			logging.warning(f'Loading custom profile {prof}')
		fp = webdriver.FirefoxProfile(prof)
		browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)

	else:
		exit("🚫 Invalid choice. Quitting now...")


except Exception as e:
	print('🚫 Make sure you choose a browser..')
	print(e)


people_list = []



def scrollBody():
	try:
		body = browser.find_element_by_xpath(body_path)
		body.click()
		body.send_keys(Keys.PAGE_UP)
	except:
		print('\nSmall Chat window detected, no scrolling..')
		pass
	return


def logOut():
	print("🚫 Logging out")
	drop_down_menu = browser.find_element_by_xpath("//div[@id='side']/header/div[2]/div/span/div[3]/div/span")
	drop_down_menu.click()
	sleep(1)
	logOut_btn = browser.find_element_by_xpath("//div[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[7]/div")
	logOut_btn.click()
	sleep(1)
	print('✅ Loggged out')
	logging.warning("Logged Out")
	return




# Try to access Whatsapp on the browser
try:
	print("Starting web browser...")
	browser.get('https://web.whatsapp.com')
	
	print("✅ Loaded browser..")
	sleep(4)


	if args['remember']=='False':
		print('⚠️ Remember disabled, temporary session')
		remember = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div/div[3]/label/input')
		remember.click()
	else:
		print('✅ Remember enabled')
		pass
	input("\n⚠️ Scan QR CODE and press enter ")

	browser.minimize_window()
	logging.warning('Logged In')
	
	createAndRun()
	sleep(3)
	
	# Run an infinite loop to keep on checking for new messages
	while True:

		sessionStatus=getData()['session']
		session=getData()['status']

		if sessionStatus.lower()=='loggedout':
			logOut()
			browser.close()
			system('rm -rf /tmp/whatsAuto; mkdir /tmp/whatsAuto')
			exit("🚫 Quitting now")
		elif session.lower()=='quit':
			browser.close()
			system('rm -rf /tmp/whatsAuto; mkdir /tmp/whatsAuto')
			exit("🚫 Quitting now")
		else:
			sleep(3.5)

		# Get unread messages
		unread_elements = browser.find_elements_by_class_name(unread_icon)

		for message in unread_elements:
			try:
				# Click on the first message
				message.click()

				scrollBody()

				# Span containing the name of the sender

				#name_span = browser.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[1]/div/span")
				name_span = browser.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div/div/span")
				

				# Get person's name and add it to the list
				name = name_span.text
				print(f"\n👉 Message from {name}")
				if name.lower() in ignoredPeople:
					print(f'Ignored {name}')
					logging.warning(f'Ignored {name}')
					continue
				else:
					pass
				# Count of duplicates for a name in the list

				if mode=='auto':

					name_count = people_list.count(name)

					# First time the user receives a message from someone
					if name_count == 0:
						# Add the sender to the list and auto respond
						people_list.append(name)

					# Remove name from list if its time to auto respond again
					elif name_count == messages_before_response:
						# Remove all occurrences of the given name but keep 1
						people_list = [word for word in people_list if word != name]

					elif (name_count > 0) and (name_count < messages_before_response):
						# Add the name to the list and skip responding
						people_list.append(name)
						continue


					# Get the text box element
					logging.warning(f'Message from {name}')
					textbox_element = browser.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div/div/div[2]")


					if args['custom']:
						if name in customMessages:
							response_message = customMessages[name]
						# Get --message command line argument value or assign a default
						elif args['message'] is None:
							response_message = "Sorry, I'm busy at the moment, will get back to you later. _Note that this is an auto generated message_ "
						else:
							response_message = args['message']

							
					elif args['message'] is None:
						response_message = "Sorry, I'm busy at the moment, will get back to you later. _Note that this is an auto generated message_ "
					else:
						response_message = args['message']

					# Set response text in the text field
					textbox_element.send_keys(f"Hey {name}.... _This is an autogenerated message_\n")
					textbox_element.send_keys(f"{response_message} \n")
					print(f"✅ Replied")
					sleep(1.5)
					scrollBody()

				elif mode=='manual':
					textbox_element = browser.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div/div/div[2]")
					replyInp = input("Reply👉 ")
					reply = response_message if replyInp =="" else replyInp

					print(f"✅ Replied: {reply}")
					
					textbox_element.click()

					textbox_element.send_keys(f"{reply} \n")
					sleep(2)
					scrollBody()

					
					
			except common.exceptions.WebDriverException as e:
				if selected_browser =='chrome':
					print(e)
					print("🚫 NO EMOJI PLEASE")
				else:
					print(e)
			
			except KeyboardInterrupt:
				logOut()
#				browser.close()
#				exit("🚫 Quitting now")

except common.exceptions.WebDriverException as e:
	print(e)

	browser.close()
	system('rm -rf /tmp/whatsAuto; mkdir /tmp/whatsAuto')
	exit("🚫 Quitting now")

#/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[7]/div[1]
