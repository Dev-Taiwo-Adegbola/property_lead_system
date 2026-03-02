from django.db import models
from django.utils.text import slugify


class Property(models.Model):
    FOR_SALE = 'FOR SALE'
    TO_LET = 'TO LET'
    SOLD = 'SOLD'
    DEFAULT = ''
    STATUS_CHOICES = (
        (DEFAULT, ''),
        (FOR_SALE, 'For sale'),
        (TO_LET, 'To let'),
        (SOLD, 'Sold'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.CharField(choices=STATUS_CHOICES, default=DEFAULT)
    no_of_bedroom = models.SmallIntegerField()
    no_of_bathroom = models.SmallIntegerField()
    property_land_size = models.SmallIntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self):
        if  self.slug is None:
            base_slug = slugify(self.title)
            slug = base_slug

            count = 1
            while Property.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug
        return super().save()
    
    class Meta:
        verbose_name_plural = 'Properties'


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=160)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} sent you a message'
    

    # email = 'demo@demo.com'
    # username = 'demo'
    # password = 'demo'