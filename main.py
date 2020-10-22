import aiohttp
import asyncio
import time
import smtplib
import os
from names import names
from email.message import EmailMessage
from dotenv import load_dotenv

failures = []

load_dotenv()

EMAIL_ENV = os.getenv('EMAIL')
PASSWORD_ENV = os.getenv('PASSWORD')


async def fetch(session, url, name):

    async with session.get(url) as response:

        if response.status != 200:
            failures.append(name)


async def fetch_all(session, usernames):
    url = 'https://instagram.com/'

    tasks = []

    for name in usernames:

        # Instagram has a minimum character limit of 4 so this will exclude names shorter than
        if (len(name) < 4):
            continue

        task = asyncio.create_task(fetch(session, f'{url}{name}/', name))

        tasks.append(task)

    results = await asyncio.gather(*tasks)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ENV, PASSWORD_ENV)

    subject = 'Latest: Instagram Bot'
    body = f'{failures}'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        EMAIL_ENV,
        EMAIL_ENV,
        msg
    )
    print('EMAIL HAS BEEN SENT')
    server.quit()


async def main():

    async with aiohttp.ClientSession() as session:
        response = await fetch_all(session, names)

        failures.sort()

        send_mail()

        print(EMAIL_ENV)

        print(failures)

if __name__ == '__main__':
    asyncio.run(main())
