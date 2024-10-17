import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "______YOUR_STOCK_API_KEY_____"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = "______YOUR_NEWS_API_KEY_____"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_NUMBER = ""
MY_NUMBER = ""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
yesterday_close = float(data_list[1]["4. close"])
day_before_yesterday_close = float(data_list[2]["4. close"])

percentage_change = round((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100)
up_down = None
if percentage_change > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

print(yesterday_close, day_before_yesterday_close, percentage_change)

if abs(percentage_change) > 1:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_params = {
        "q": COMPANY_NAME,
        "from": "2024-09-23",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(NEWS_ENDPOINT, news_params)
    articles = response.json()["articles"]
    first_3_news = articles[:3]
    print(response.json())

    formatted_articles = [f"{STOCK}: {up_down}{percentage_change}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_3_news]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# MESSAGE_API_KEY = "3BXRWNB2CDFLZFPCRCLRY241"


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

