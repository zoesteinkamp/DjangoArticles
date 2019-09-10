from django.db import models
import uuid


class Tagtype(models.Model):
    slug = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)

class Link(models.Model):
    content = models.URLField(max_length=200)
    linkself = models.URLField(max_length=200)

class ArticleLink(models.Model):
    articlelinkself = models.URLField(max_length=100)
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
    twitter_username = models.CharField(max_length=100,null=True, blank=True)
    small_avatar_url = models.CharField(max_length=100)
    long_bio = models.TextField(null=True, blank=True)
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
    tag_type = models.ManyToManyField(Tagtype)
    links = models.OneToOneField(Link,on_delete=models.CASCADE, null=True, blank=True)

class Comments(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=100)
    created = models.DateTimeField()


class Article(models.Model):
    disclosure = models.TextField()
    promo = models.CharField(max_length=200)
    body = models.TextField()
    visibility = models.IntegerField(default=0) # not sure what this is
    article_type = models.CharField(max_length=100)
    publish_at = models.DateTimeField()
    path = models.CharField(max_length=100)
    static_page = models.BooleanField(default=False)
    author_override = models.CharField(max_length=100,null=True, blank=True) # not sure either
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField()
    headline = models.CharField(max_length=100)
    modified = models.DateTimeField()
    product_id = models.IntegerField(default=0)
    video = models.CharField(max_length=100,null=True, blank=True)
    byline = models.CharField(max_length=100)
    insturments = models.ManyToManyField(Instrument)
    authors = models.ManyToManyField(Author)
    bureau = models.OneToOneField(Bureau,null=True,on_delete=models.CASCADE)
    collection = models.OneToOneField(Collection,null=True,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pitch = models.OneToOneField(Pitch,null=True,on_delete=models.CASCADE)
    links = models.OneToOneField(ArticleLink,null=True,on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)
    comments = models.ForeignKey('Comments',blank=True,null=True, on_delete=models.CASCADE)


class Quotes(models.Model):
    company_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    exchange = models.CharField(max_length=100)
    exchange_name = models.CharField(max_length=100)
    isoalpha2countrycode = models.CharField(max_length=100)
    isoalpha3countrycode = models.CharField(max_length=100)
    sector = models.CharField(max_length=100,null=True, blank=True)
    industry = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField()
    currency_code = models.CharField(max_length=100)
    year1ForwardEPSEstimateAmount = models.FloatField()
    year1ForwardEPSEstimateCurrency = models.IntegerField(default=1)
    year2ForwardEPSEstimateAmount = models.FloatField()
    year2ForwardEPSEstimateCurrency = models.IntegerField(default=1)
    instrument_id = models.IntegerField(default=1)
    short_interest = models.IntegerField(default=1)
    volume = models.IntegerField(default=1)
    shares_outstanding = models.IntegerField(default=1)
    average_volume = models.IntegerField(default=1)
    pricetoearningsratio = models.FloatField()
    returnonequity = models.IntegerField(default=0)
    lasttradedate = models.DateTimeField()
    exdivdate  = models.DateTimeField()
    divpaydate = models.DateTimeField()
    change_amount = models.FloatField()
    change_currency = models.IntegerField(default=1)
    closepriceamount = models.FloatField()
    closepricecurrency = models.IntegerField(default=1)
    currentpriceamount = models.FloatField()
    currentpricecurrency = models.IntegerField(default=1)
    openpriceamount = models.FloatField()
    openpricecurrency = models.IntegerField(default=1)
    marketcapamount = models.FloatField()
    marketcapcurrency = models.IntegerField(default=1)
    marketcapchangeamount = models.FloatField()
    marketcapchangecurrency = models.IntegerField(default=1)
    earningspershareamount = models.FloatField()
    earningspersharecurrency = models.IntegerField(default=1)
    percent_change = models.FloatField()
    fiftytwoweek_minimumamount = models.FloatField()
    fiftytwoweek_minimumcurrency = models.IntegerField(default=1)
    fiftytwoweek_maximumamount = models.FloatField()
    fiftytwoweek_maximumcurrency = models.IntegerField(default=1)
    dailyrange_minimumamount = models.FloatField()
    dailyrange_minimumcurrency = models.IntegerField(default=1)
    dailyrange_maximumamount = models.FloatField()
    dailyrange_maximumcurrency = models.IntegerField(default=1)
    annual_dividendamount = models.IntegerField(default=1)
    annual_dividendcurrency = models.IntegerField(default=1)
    dividend_yield = models.FloatField()
    percentofsharestraded = models.FloatField()
    asset_class = models.IntegerField(default=1)
    chart_url = models.CharField(max_length=100,null=True, blank=True)
    isrealtime = models.BooleanField(default=False)
    bid_amount =  models.FloatField()
    bid_currency = models.IntegerField(default=1)
    ask_amount =  models.FloatField()
    ask_currency = models.IntegerField(default=1)
    ask_yield = models.IntegerField(default=1)
    bid_yield = models.IntegerField(default=1)
    maturity_date = models.DateTimeField()
    open_yield = models.IntegerField(default=1)
    previous_yield = models.IntegerField(default=1)
    open_interest = models.IntegerField(default=0)
    seo_name = models.CharField(max_length=100,null=True, blank=True)
    idc_mdgid = models.IntegerField(null=True)
    website = models.CharField(max_length=100,null=True, blank=True)
    beta3y = models.FloatField()
    home_countrycode = models.CharField(max_length=100,null=True, blank=True)
    gross_margin =  models.FloatField()
    revenue_growth = models.FloatField()
