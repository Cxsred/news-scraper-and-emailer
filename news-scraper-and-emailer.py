import requests
from bs4 import BeautifulSoup
import smtplib

def fetch_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    news_headlines = soup.find_all("h3", class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text")

    headlines_list = []
    for headline in news_headlines:
        headlines_list.append(headline.text)

    return headlines_list

def send_email(subject, body):
    sender_email = "your-email@example.com"
    sender_password = "your-email-password"
    receiver_email = "recipient-email@example.com"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, receiver_email, message)

news_headlines = fetch_news()
news_subject = "Latest News Headlines"
news_body = "\n".join(news_headlines)

send_email(news_subject, news_body)
