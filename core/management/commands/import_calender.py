from datetime import datetime

import environ
import requests
from django.core.management import BaseCommand

from core.models import Calender, Idol


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        google calenderからlive予定を取得する
        """
        env = environ.Env()
        env.read_env(".env")
        google_api_key = env("GOOGLE_API_KEY")

        for idol in Idol.objects.filter(google_calender__isnull=False):
            url = f'https://www.googleapis.com/calendar/v3/calendars/{idol.google_calender}/events'

            time_min = datetime(2019, 3, 1, 0, 0, 0)
            time_max = datetime(2021, 12, 31, 23, 59, 59)

            payload = {
                'maxResults': 30 * 12 * 2,
                'order_by': 'startTime',
                'timeMin': time_min.strftime('%Y-%m-%dT00:00:00Z'),
                'timeMax': time_max.strftime('%Y-%m-%dT23:59:59Z'),
                'singleEvents': True,
                'key': google_api_key,
            }

            r = requests.get(url, params=payload)
            for item in r.json()["items"]:
                c = dict()
                c["summary"] = item["summary"]
                c["start"] = item["start"]["date"]
                c["end"] = item["end"]["date"]
                c["location"] = item.get("location", None)
                c["description"] = item.get("description", None)
                Calender.objects.get_or_create(
                    idol=idol, summary=c["summary"], start=c["start"], defaults=c)
