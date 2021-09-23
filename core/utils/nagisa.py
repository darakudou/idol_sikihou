import nagisa

from core.models import Music


class Nagisa():

    def __init__(self, idol):

        self.musics = Music.objects.filter(artist=idol).values("id", "identifications_title")

        self.overide_nagisa = nagisa.Tagger(
            single_word_list=list(self.musics.values_list("identifications_title", flat=True))
        )

    def extract(self, text):
        return self.overide_nagisa.extract(text, extract_postags=["名詞", "英単語"])

    def hit_title_ids(self, text):
        # TODO: 馬鹿っぽいけどとりあえずこれで...
        text = text.replace("moon light", "moonlight")
        text = text.replace("in the Dark", "inthedark")
        token = self.extract(text)
        hit_title_ids = []
        identification_titles = [m["identifications_title"] for m in self.musics]

        for word in token.words:
            if word in identification_titles:
                hit_title_ids.append(Music.objects.get(identifications_title=word).id)
        return hit_title_ids
