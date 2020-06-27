from django.db import models
from django.utils.text import slugify
# Create your models here.

JOP_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_uplaod(instance,filename):
    imagename , extension = filename.split('.')
    return 'jobs/%s.%s'%(instance.id,extension)


class Job(models.Model):

    title        = models.CharField(max_length=100)
    # location
    job_type     = models.CharField(max_length=15 , choices=JOP_TYPE)
    description  = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy      = models.IntegerField(default=1)
    salary       = models.IntegerField(default=0)
    experience   = models.IntegerField(default=1)
    categories   = models.ForeignKey('Category' , on_delete=models.CASCADE )
    image        = models.ImageField(upload_to=image_uplaod)

    slug         = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):

    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name


class Apply(models.Model):

    job          = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=100)
    website      = models.URLField(blank=True, null=True)
    cv           = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=200)
    created_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
