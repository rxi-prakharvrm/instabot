from selenium import webdriver 
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import time 

# Input for Instagram credentials
username = input('Username: ')
password = getpass.getpass(prompt='Password: ', stream=None)
recepientUser = input('Recepeint User: ')  # Gets username of the user to message

# Initialize Chrome WebDriver
chrome = webdriver.Chrome()
chrome.maximize_window()  # Starts Chrome in a maximized window
url = ('https://www.instagram.com/accounts/login/?source=auth_switcher') 

def url_name(url): 
    """Opens the given URL in the Chrome browser."""
    chrome.get(url)
    time.sleep(4) 

def login(username, your_password):
    """Logs into Instagram using the provided username and password."""
    time.sleep(4)
    # Finds the username input box and sends the entered username
    usern = chrome.find_element("xpath",'//*[@id="loginForm"]/div/div[1]/div/label/input')
    usern.send_keys(username)
    time.sleep(4)
    usern.send_keys("\ue004")  # Sends the enter key
    
    # Focus on the password field and send the password
    focused_elem = chrome.switch_to.active_element
    focused_elem.send_keys(your_password)

    # Finds and clicks the login button
    log_cl = chrome.find_element("xpath",'//*[@id="loginForm"]/div/div[3]/button')
    log_cl.click()  
    time.sleep(10)

    # Dismiss the 'Not Now' pop-up for notifications
    # not_now = chrome.find_element("xpath",'//*[@id="mount_0_0_VZ"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
    # not_now.click()
    # time.sleep(4)

def search_user(username):
    url_name("https://instagram.com/"+username)
    time.sleep(10)

    # Clicks the message button to initiate a conversation
    msg_button = chrome.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[2]/div')
    msg_button.click()
    time.sleep(10)

def logout():
    """Logs out of the Instagram account."""
    profileUrl = 'https://www.instagram.com/' + username
    url_name(profileUrl)
    time.sleep(10)
    settings_button = chrome.find_element("xpath",'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[3]')
    settings_button.click()  # Clicks on settings
    time.sleep(10)

    # Clicks on the logout option
    logout_opt = chrome.find_element("xpath",'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/button[8]')
    logout_opt.click()

def dm():
    url_name("https://instagram.com/direct/inbox/")
    time.sleep(4)

def like():
    """Automatically likes all currently loaded posts."""
    actionchains = ActionChains(chrome)
    posts = chrome.find_elements_by_css_selector("[class^=_9AhH0]")
    time.sleep(4)
    for post in posts:
        actionchains.double_click(post).perform()  # Double-click to like the post

def share_a_post():
    """Shares the first post to a specific user."""
    time.sleep(4)
    postsOption = chrome.find_elements_by_css_selector("[class^=MEAGs]")
    for post in postsOption:
        post.click()  # Click on the post
        time.sleep(3)
        sh_button = chrome.find_element("xpath",'/html/body/div[4]/div/div/div/button[4]')
        sh_button.click()  # Clicks the share button
        time.sleep(3)

        sh_button_direct = chrome.find_element("xpath",'/html/body/div[4]/div/div/div[2]/div/div[1]')
        sh_button_direct.click()  # Clicks on share via direct message
        time.sleep(4)

        # Searches for the recipient user
        search_box = chrome.find_element("xpath",'/html/body/div[5]/div/div[2]/div[1]/div/div[2]/input')
        search_box.send_keys('amanraj')
        time.sleep(5)

        result = chrome.find_element("xpath",'/html/body/div[5]/div/div[2]/div[2]/div[1]')
        result.click()  # Clicks on the search result
        time.sleep(3)

        # Clicks the send button
        send_bttn = chrome.find_element("xpath",'/html/body/div[5]/div/div[1]/div/div[2]/div/button')
        send_bttn.click()
        time.sleep(4)

# Log in to Instagram
url_name(url)
login(username, password)

def message_first_user(message):
    """Sends a message to the first user in direct messages."""
    dm()
    msg_box = chrome.find_element("xpath",'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div/textarea')
    msg_box.send_keys(message)  # Sends the message
    time.sleep(2)
    msg_box.send_keys("\ue007")  # Presses the enter key to send the message

def message_user(search_name):
    """Messages a specified user with a list of predefined messages."""
    # dm()
    search_user(search_name)
    
    # Finds the message input box
    msg_box = chrome.find_element("xpath", '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')

    # List of messages to send
    msg_list = [str('this is message' + str(x)) for x in range(5)]
    msg_list[0] = 'Hey there I\'m using Instagram'

    # Sends each message in the list
    for your_message in msg_list:
        msg_box.send_keys(your_message)  # Sends the message
        time.sleep(2)
        msg_box.send_keys("\ue007")  # Presses enter to send
        time.sleep(2)

def search_user_from_home(search_name):
    """Searches for a user from the home page and navigates to their bio."""
    searchBox = chrome.find_element("xpath",'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    searchBox.send_keys(search_name)  # Sends the username to search
    time.sleep(3)
    
    firstRelevantResult = chrome.find_element("xpath",'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
    firstRelevantResult.click()  # Clicks on the first search result
    time.sleep(10)
    
    # Clicks on the bio link
    bioURL = chrome.find_element("xpath",'/html/body/div[1]/section/main/div/div[1]/a[1]')
    time.sleep(8)
    bioURL.click()



# Example function calls

message_user(recepientUser)  # Messages the user
logout()  # Logs out of Instagram