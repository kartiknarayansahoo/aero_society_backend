import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Alumn(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='alumns/')
    current_industry_position = models.CharField(max_length=255)
    hall_of_residence = models.CharField(max_length=255)
    year_of_graduation = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1950), max_value_current_year])

    def __str__(self):
        return self.name+'-'+self.year_of_graduation
