# Telegram Bot for Loan, Repayment and Job Information
This project features a Telegram bot that integrates with a PostgreSQL database to provide information on loans, repayments, and job statuses through Telegram chat commands.

## Features
Retrieve Loan Information: Type /loan in the Telegram chat to get information about loans grouped by branch for the current date.
Retrieve Repayment Information: Type /repayment to get information about repayments grouped by branch for the current date.
Retrieve Job Statuses: Type /jobs to get the status and description of jobs for the current date.

## Setup

### 1. Install Dependencies:

Ensure you have the required Python packages installed. You can use pip to install them:

```python 
pip install pyodbc psycopg2-binary pyTelegramBotAPI```

### 2. Configuration:
Update the config.py file with your own configuration:
```	
token = 'YOUR_TELEGRAM_BOT_TOKEN'
telegram_user_id_list = [YOUR_USER_ID_LIST]  # List of allowed user IDs
Replace placeholders with your actual values:```

YOUR_TELEGRAM_BOT_TOKEN: Your Telegram bot token from BotFather.
YOUR_USER_ID_LIST: A list of Telegram user IDs who are allowed to access the bot.

### 3. Database Configuration:
Modify the server, database, username, and password variables to match your PostgreSQL database settings.

### 4. Running the Bot:
To start the bot, run the following command:

`python
python your_script_name.py
The bot will start polling for messages and respond to the commands.`

# Code Overview

### Imports and Configuration:
pyodbc and psycopg2 for database connections.
config for configuration settings.
TeleBot from pyTelegramBotAPI for Telegram bot interactions.
threading for running the bot in a separate thread.
### Command Handlers:

/loan: Retrieves and sends loan information.
/repayment: Retrieves and sends repayment information.
/jobs: Retrieves and sends job statuses.

### Query Functions:
stand_qry(param1, user_id): Executes SQL queries and sends the results to the Telegram user if they are authorized.

### Bot Initialization:
runBot(): Starts the bot's polling loop.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to submit issues, feature requests, or pull requests.