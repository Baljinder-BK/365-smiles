"""Pick today's quote and send it to your phone via ntfy."""
import os
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

TOPIC = os.environ["NTFY_TOPIC"]
TZ = os.environ.get("QUOTE_TZ", "America/Toronto")


def load_quotes(path="quotes.txt"):
    with open(path, encoding="utf-8") as f:
        lines = [l.strip() for l in f]
    return [l for l in lines if l and not l.startswith("#")]


def todays_quote(quotes):
    day = datetime.now(ZoneInfo(TZ)).timetuple().tm_yday  # 1..366
    return quotes[(day - 1) % len(quotes)], day


def send(message, day):
    req = urllib.request.Request(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers={"Title": f"Good morning! Day {day}", "Tags": "sunny,sparkles"},
    )
    urllib.request.urlopen(req, timeout=15)


if __name__ == "__main__":
    quotes = load_quotes()
    quote, day = todays_quote(quotes)
    send(quote, day)
    print(f"Sent day {day}: {quote}")
