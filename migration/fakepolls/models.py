from django.db import models

class Magic(models.Model):
    name_text = models.CharField(max_length=200)
    type_text = models.CharField(max_length=200)
    color_text = models.CharField(max_length=200)
    cmc_num = models.IntegerField(default=0)
    rarity_text = models.CharField(max_length=200)
    price_num = models.FloatField(default=0)
    artist_text = models.CharField(max_length=200)
    cardset_text = models.CharField(max_length=200)
