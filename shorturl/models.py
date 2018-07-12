from django.db import models

# Construct url model
class Url(models.Model):
    keyword = models.CharField("Short URL", max_length=20, unique=True)
    origin_url = models.URLField("Origin URL", max_length=200)
    title = models.CharField("Title", max_length=100, default="")
    clicks = models.PositiveIntegerField(default=0)
    tags = models.CharField("Tags", max_length=200, blank=True)
    category = models.CharField(max_length=100, default='Default')
    timestamp = models.DateTimeField("Created Time", auto_now_add=True)
    permanent = models.BooleanField("HTTP 301", default=False)
    #
    def __str__(self):
        text = "{title:_^10s}: \n{short:<5s} --> {url}".format(short=self.keyword, url=self.origin_url, title=self.title)
        return text
    #
    def clicked(self):
        self.clicks = models.F('clicks') + 1
        super().save()

# Construct url log model
class Log(models.Model):
    url = models.CharField("Short URL", max_length=20)
    click_timestamp = models.DateTimeField("Click Time", auto_now_add=True)
    click_ip = models.GenericIPAddressField("Click IP", default="0.0.0.0")
    referrer = models.CharField(max_length=200, default="")
    user_agent = models.CharField(max_length=200, default="")
    #
    def __str__(self):
        text = f"url:{self.url} ip:{self.click_ip:<15} time:{self.click_timestamp}"
        return text