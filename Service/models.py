from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    home = models.IntegerField()
    time_open = models.TimeField()
    time_close = models.TimeField()

    def __str__(self):
        return self.name
