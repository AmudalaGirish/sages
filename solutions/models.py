from django.db import models

# Create your models here.
from django.db import models

class GasStorageSolution(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add any additional fields specific to the Gas Storage Solution model

    def __str__(self):
        return self.title


class GasPipeline(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add any additional fields specific to the Gas Pipeline model

    def __str__(self):
        return self.title


class GasApplicationSolution(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add any additional fields specific to the Gas Application Solution model

    def __str__(self):
        return self.title


class GasFuelConversion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add any additional fields specific to the Gas Fuel Conversion model

    def __str__(self):
        return self.title


class ValueAddedService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add any additional fields specific to the Value Added Service model

    def __str__(self):
        return self.title


class GasProduct(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add any additional fields specific to the Gas Product model

    def __str__(self):
        return self.title
