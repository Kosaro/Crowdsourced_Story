from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PlotPoint(models.Model):
    pptext = models.CharField(max_length=1000)
    uv = models.IntegerField(default=0)
    dv = models.IntegerField(default=0)
    isEnd = models.BooleanField(default=False)
    writtenby = models.CharField(max_length=20)
    def __str__(self):
        return self.pptext


class Choice(models.Model):
    plotpoint = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)
    destination = models.OneToOneField(PlotPoint, related_name='+', on_delete=models.CASCADE, default=None)
    text = models.CharField(max_length=100)
    uv = models.IntegerField(default=0)
    dv = models.IntegerField(default=0)
    writtenby = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class Bookmark(models.Model):
    user = models.CharField(max_length=30)
    plot_point = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)


class Edits(models.Model):
    user = models.CharField(max_length=30)
    plot_point = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)
    request_status = models.BooleanField(default=True)


class Choice_Edits(models.Model):
    user = models.CharField(max_length=30)
    plot_point = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    request_status = models.BooleanField(default=True)


class Upvotes(models.Model):
    user = models.CharField(max_length=30)
    plot_point = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)


class Downvotes(models.Model):
    user = models.CharField(max_length=30)
    plot_point = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)


class Choice_Upvotes(models.Model):
    user = models.CharField(max_length=30)
    plot_point = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


class Choice_Downvotes(models.Model):
    user = models.CharField(max_length=30)
    plot_point = models.ForeignKey(PlotPoint, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
