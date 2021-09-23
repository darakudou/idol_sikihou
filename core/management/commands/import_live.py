import datetime
import re

from dateutil import parser
from django.core.management import BaseCommand
from pytz import timezone

from core.models import Calender, Live, Music, Tweet, TwitterAcount
from core.models.setlist import SetList
from core.utils.nagisa import Nagisa


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        calenderからlive情報を取り込む
        """
        for twitter_acount in TwitterAcount.objects.all():
            for t in twitter_acount.tweet_set.all().order_by("id"):
                try:
                    r = r"[0-9].*/[0-9].* setlist"
                    if re.match(r, t.text):
                        create_live(t)
                except Exception as e:
                    print(f"{e.args}", t.text)


def create_live(tweet):
    start_at = tweet.created_at.astimezone(timezone("Asia/Tokyo"))
    live = dict()
    """
    setlist 日付
    イベント情報
    1 曲名
    2 曲名
    """
    order = 1
    r = r"[0-9].*/[0-9].* setlist"
    titles = ""
    setlists = []
    is_eventname = []
    for i, t in enumerate(tweet.text.split("\n")):
        if i ==0:
            # 1行目はXX/XX setlist だと思われるので飛ばす
            continue
        set_list = {}
        if t[0].isdigit():





    return Live.objects.update_or_create(
        title=c.summary, start_at=start_at, defaults=live)


def create_setlist(music_ids, live):
    for i, m in enumerate(music_ids, start=1):
        # べき等性担保のため、update_or_createで何度流しても大丈夫にする
        if live:
            SetList.objects.update_or_create(
                live=live, order=i, defaults={"music_id": m})
