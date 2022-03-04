# в этом файле мы сможем отслещивать различные сигналы(действия), которые происходят внутри проекта
# например при рег. пользователя в табл. user, мы сможем отследить это д-е
# и в этот же момент мы будем рег-ть польз-ля в табл-це profile
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
