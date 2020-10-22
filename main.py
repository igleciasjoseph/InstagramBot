import aiohttp
import asyncio
import time
import smtplib
import os
from handles import handles
from dotenv import load_dotenv

load_dotenv()

EMAIL_ENV = os.getenv("EMAIL")
PASSWORD_ENV = os.getenv("PASSWORD")
INSTAGRAM_URL = "https://instagram.com/"

available_handles = []


async def fetch(session, url, name):
    response = await session.get(url)
    if response.status != 200:
        available_handles.append(name)


def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_ENV, PASSWORD_ENV)

    subject = "Latest: Instagram Bot"
    body = f"{available_handles}"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(EMAIL_ENV, EMAIL_ENV, msg)
    print("Email sent")
    server.quit()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch(session, f"{INSTAGRAM_URL}{handle}/", handle))
            for handle in handles
            if len(handle) >= 4
        ]
        await asyncio.gather(*tasks)
        available_handles.sort()
        send_email()


if __name__ == "__main__":
    asyncio.run(main())
