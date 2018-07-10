from django.db import models

# Construct url model
class Url(models.Model):
    keyword = models.CharField("Short URL", max_length=20, unique=True)
    origin_url = models.URLField("Origin URL", max_length=200)
    title = models.CharField("Title", max_length=100, default="")
    clicks = models.PositiveIntegerField(default=0)
    creator_ip = models.GenericIPAddressField("IP", default="0.0.0.0")
    timestamp = models.DateTimeField("Created Time", auto_now_add=True)
    # def __str__(self):
    #     text = "{title:^10s}: {short:^5s} --> {url}".format(short=self.keyword[:5], url=self.origin_url[:20], title=self.title[:10])
    #     return text

# Construct url logs model
class Log(models.Model):
    url = models.CharField("Short URL", max_length=20)
    click_timestamp = models.DateTimeField("Click Time", auto_now_add=True)
    click_ip = models.GenericIPAddressField("Click IP", default="0.0.0.0")
    referrer = models.CharField(max_length=200, default="")
    user_agent = models.CharField(max_length=200, default="")

