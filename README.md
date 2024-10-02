---

### **Repository Description**:
Automated Instagram Interaction Bot using Selenium

This Python project automates several common interactions on Instagram, such as logging in, sending direct messages, liking posts, sharing posts, and logging out. By utilizing Selenium WebDriver, it simulates user interactions in the browser, making it a versatile tool for anyone looking to automate Instagram tasks. The project can be extended to include more advanced functionalities like scheduled messaging or dynamic interaction flows.

---

### **README.md**:

```md
# Instagram Interaction Automation Bot 🤖

This project is a Python-based automation bot that interacts with Instagram using Selenium WebDriver. It automates a variety of tasks such as logging in, sending direct messages, liking posts, and sharing posts. The project serves as an efficient tool to simulate user interactions, which could be beneficial for bulk messaging, marketing campaigns, or simply automating routine tasks on Instagram.

## 🚀 Features
- **Login Automation**: Log into Instagram by providing your credentials.
- **Direct Messaging**: Send a series of predefined messages to a specified user.
- **Liking Posts**: Automatically likes all posts on the current page.
- **Post Sharing**: Share a specific post with a target user.
- **User Search**: Search for a specific user and access their profile.
- **Logout Functionality**: Logs out of Instagram securely after the task is complete.

## 📋 Prerequisites

Ensure you have the following installed before proceeding:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Selenium**: Install via pip.
  ```bash
  pip install selenium
  ```
- **Chrome WebDriver**: Download the correct version of ChromeDriver that matches your installed Chrome browser from [here](https://sites.google.com/chromium.org/driver/). Ensure the WebDriver path is correctly set up.

## 🛠 Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/instagram-automation-bot.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and configure Chrome WebDriver as mentioned above.

4. Run the script:
   ```bash
   python instagram_bot.py
   ```

5. Follow the input prompts to enter your Instagram credentials and the target username for messaging or interaction.

## 📄 Usage

### Direct Messaging a User:
The bot allows you to send a list of predefined messages to a specified user on Instagram.

```python
message_user('username_to_message')
```

### Auto Liking Posts:
You can automate liking posts on the current page.

```python
like()
```

### Sharing a Post with Another User:
The bot also allows you to share a post with a specified user.

```python
share_a_post()
```

### Searching and Visiting a User Profile:
You can search for a specific user directly from the homepage and access their profile.

```python
search_user_from_home('username')
```

### Logging Out:
After completing tasks, you can securely log out of Instagram.

```python
logout()
```

## 💡 Future Enhancements

- **Scheduled Messaging**: Add support for scheduled messaging at specific intervals.
- **Bot Interactions**: Build in interactive features like auto-replying to direct messages.
- **Error Handling**: Improve error handling to manage cases of unexpected website behavior or loading failures.

## ⚠️ Disclaimer

This bot is for educational purposes only. Use responsibly and ensure you adhere to Instagram's [Terms of Service](https://help.instagram.com/581066165581870).

## 👨‍💻 Author

[Your Name](https://github.com/your-username) - Master of Computer Applications, University of Delhi

```
