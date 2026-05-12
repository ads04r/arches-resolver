from django.db import models
from arches.app.models import models as arches_models

class ExternalReference(models.Model):

    external_reference = models.CharField(max_length=254)
    external_reference_type = models.SlugField(max_length=128)
    related_resourceinstance = models.ForeignKey(arches_models.ResourceInstance, on_delete=models.CASCADE, related_name='external_references')
    class Meta:
        unique_together = ('external_reference', 'external_reference_type')
