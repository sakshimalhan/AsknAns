from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


from questions.models import Question

@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        
        instance.slug = slug 
