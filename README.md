# ☀️ Morning Quotes

A cute quote on my phone every morning, one for each day of the year.

## Setup
1. Install the **ntfy** app (iOS / Android) and subscribe to a topic with a
   hard-to-guess name, e.g. `sunny-quotes-8f3k2x` (topics are public if guessed).
2. In this repo: **Settings → Secrets and variables → Actions → New secret**
   named `NTFY_TOPIC` with that topic name.
3. **Actions → Morning quote → Run workflow** to test. 🎉

## Adding quotes
Edit `quotes.txt`, one per line. Aim for 365 (366 for leap years; it wraps
around if you have fewer).

## Tweaks
- Change send time: edit the `cron` line (UTC) in `.github/workflows/morning-quote.yml`.
- Change timezone: set `QUOTE_TZ` in the workflow env.
