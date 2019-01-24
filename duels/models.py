from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

ROUNDS = (
    (0, 'Not started'),
    (1, 'Round 1'),
    (2, 'Round 2'),
    (3, 'Round 3'),
    (4, 'Finished')
)



class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title


class Duel(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    rounds = models.ManyToManyField('Algorithm')
    dataset = models.ForeignKey('Dataset', on_delete=models.CASCADE)
    user1_percentage = ArrayField(
        models.DecimalField(decimal_places=4, max_digits=6, validators=[MinValueValidator(0), MaxValueValidator(100)]),
        size=3,
        null=True)
    user2_percentage = ArrayField(
        models.DecimalField(decimal_places=4, max_digits=6, validators=[MinValueValidator(0), MaxValueValidator(100)]),
        size=3,
        null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Dataset(models.Model):
    name = models.CharField(max_length=64)
    dataset = models.FileField(upload_to='datasets', default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    ALGORITHM_NAME = (
        ('0', 'KNeighborsClassifier'),
        ('1', 'LogisticRegression'),
        ('2', 'LinearSVC'),
        ('3', 'GaussianNB'),
        ('4', 'DecisionTreeClassifier'),
        ('5', 'RandomForestClassifier'),
        ('6', 'GradientBoostingClassifier'),
        ('7', 'MLPClassifier'),
    )

    name = models.CharField(max_length=64, choices=ALGORITHM_NAME)
    parameters = JSONField()

    def __str__(self):
        field = self._meta.get_field('name')
        value = self._get_FIELD_display(field)
        return f'{value}'
