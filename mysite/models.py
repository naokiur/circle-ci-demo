from django.db import models


class Page(models.Model):

    title = models.CharField("タイトル", max_length=128)
    contents = models.TextField("内容")

    def to_dict(self):

        return {
            "title": self.title,
            "contents": self.contents
        }

    class Meta:
        db_table = "page"
