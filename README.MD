# Instagram Bot for Usernames

Instagram Bot for Username, or IBU, is a bot that scans Instagram for usernames that aren't taken and creates an account with said username

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modules.

```bash
pip install -r requirements.txt
```

## Google Apps Configuration

You will need to configure google apps to allow you to use the smtplib library to send emails.

Here is a link for a quick walkthrough - [app configuration](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637389282771474551-1804214934&rd=1)

## Environment Variable Configuration

You will need to create a .env file that stores your email and password from Google Apps above.

Feel free to name the variables as you wish

```python
EMAIL_ENV = os.getenv('EMAIL')
PASSWORD_ENV = os.getenv('PASSWORD')
```

## Usage

The below is the construction of the server. Feel free to use any port number as long as it is open

```python
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login(EMAIL_ENV, PASSWORD_ENV)
```

## Names Origin Source

Currently IBU is using the most popular boy names from 2018 to construct the search but eventually it will turn into a third party API.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
