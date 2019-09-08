from django.db import models
import uuid




class TagType(models.Model):
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class Link(models.Model):
    content = models.URLField(max_length=200)
    self = models.URLField(max_length=200)

class ArticleLink(models.Model):
    self = models.URLField(max_length=100)
    presentation = models.URLField(max_length=100)
    content_sequence = models.URLField(max_length=100)

class Pitch(models.Model):
    text = models.TextField()
    id = models.IntegerField(primary_key=True,editable=False)

class Image(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()
    url = models.URLField(max_length=100)
    image = models.URLField(max_length=100)
    modified = models.DateTimeField()
    featured = models.BooleanField(default=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Instrument(models.Model):
    instrument_id = models.IntegerField(primary_key=True,editable=False)
    asset_class = models.CharField(max_length=100)
    exchange = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    primary = models.BooleanField(default=True)
    seo_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    syndicate = models.BooleanField(default=True)
    valid = models.BooleanField(default=True)
    links = models.OneToOneField(Link,on_delete=models.CASCADE)

class Author(models.Model):
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    links = models.OneToOneField(Link,on_delete=models.CASCADE)
    fool_uid = models.IntegerField()
    primary = models.BooleanField(default=True)
    twitter_username = models.CharField(max_length=100)
    small_avatar_url = models.CharField(max_length=100)
    long_bio = models.TextField()
    first_name = models.CharField(max_length=100)
    byline = models.CharField(max_length=100)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contributor_type = models.CharField(max_length=100)
    large_avatar_url =  models.CharField(max_length=200)
    short_bio =  models.TextField()
    author_id = models.IntegerField()
    email = models.EmailField(max_length=100)

class Bureau(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    links = models.OneToOneField(Link,on_delete=models.CASCADE)

class Collection(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    links = models.OneToOneField(Link,on_delete=models.CASCADE)

class Tag(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tag_type = models.OneToOneField(TagType,on_delete=models.CASCADE)
    links = models.OneToOneField(Link,on_delete=models.CASCADE)

class Article(models.Model):
    disclosure = models.TextField()
    promo = models.CharField(max_length=200)
    body = models.TextField()
    visibility = models.IntegerField(default=0) # not sure what this is
    article_type = models.CharField(max_length=100)
    publish_at = models.DateTimeField()
    path = models.CharField(max_length=100)
    static_page = models.BooleanField(default=False)
    author_override = models.CharField(max_length=100) # not sure either
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField()
    headline = models.CharField(max_length=100)
    modified = models.DateTimeField()
    product_id = models.IntegerField(default=0)
    video = models.CharField(max_length=100)
    byline = models.CharField(max_length=100)
    insturments = models.ManyToManyField(Instrument)
    authors = models.ManyToManyField(Author)
    bureau = models.OneToOneField(Bureau,on_delete=models.CASCADE)
    collection = models.OneToOneField(Collection,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pitch = models.OneToOneField(Pitch,on_delete=models.CASCADE)
    links = models.OneToOneField(ArticleLink,on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)


#
#
# class Quotes(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
