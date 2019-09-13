from django.test import TestCase
from django.urls import reverse,resolve
from .models import Article
from .forms import CommentForm
from . import views

# fixtures = ['fixtures1.json','fixtures2.json', 'articles.json', 'fixturesqoutes.json']

#models tests

class ArticleTestCase(TestCase):
    fixtures = ['fixtures1.json','fixture2.json', 'articles.json','fixturesqoutes.json']

    def setUp(self):
        super(ArticleTestCase, self).setUp()
        self.article_1 = Article.objects.get(pk="a7acd8c8-c5ce-11e7-9fa6-0050569d4be0")
        self.article_2 = Article.objects.get(pk="f52c15f2-c5a9-11e7-8889-0050569d4be0")



#views tests
class HomePageTest(TestCase):
    fixtures = ['fixtures1.json','fixture2.json', 'articles.json','fixturesqoutes.json']

    def test_home_page_view(self):
        response = self.client.get("/articles/home")
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_template(self):
        response = self.client.get("/articles/home")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/home.html')

    def test_home_page_view_context(self):
        response = self.client.get("/articles/home")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('latest_article_list' in response.context)


class StocksPageTest(TestCase):
    fixtures = ['fixtures1.json','fixture2.json', 'articles.json','fixturesqoutes.json']

    def test_stocks_view(self):
        response = self.client.get("/articles/stocks")
        self.assertEqual(response.status_code, 200)


    def test_stocks_view_template(self):
        response = self.client.get("/articles/stocks")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/stocks.html')

    def test_stocks_view_context(self):
        response = self.client.get("/articles/stocks")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('stocks' in response.context)


class AuthorsPageTest(TestCase):
    fixtures = ['fixtures1.json','fixture2.json', 'articles.json','fixturesqoutes.json']

    def test_authors_view(self):
        response = self.client.get("/articles/authors")
        self.assertEqual(response.status_code, 200)

    def test_authors_view_template(self):
        response = self.client.get("/articles/authors")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/authors.html')

    def test_authors_view_template(self):
        response = self.client.get("/articles/authors")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('authors' in response.context)


class ArticlePageTest(TestCase):
    fixtures = ['fixtures1.json','fixture2.json', 'articles.json','fixturesqoutes.json']

    def test_article_view(self):
        response = self.client.get("/articles/a7acd8c8-c5ce-11e7-9fa6-0050569d4be0/")
        self.assertEqual(response.status_code, 200)

    def test_article_template(self):
        response = self.client.get("/articles/a7acd8c8-c5ce-11e7-9fa6-0050569d4be0/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article.html')

    def test_article_context(self):
        response = self.client.get("/articles/a7acd8c8-c5ce-11e7-9fa6-0050569d4be0/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('article' in response.context)
        self.assertTrue('suggested_articles' in response.context)
        self.assertTrue('stock_list' in response.context)
        self.assertTrue('comments' in response.context)


    def test_article_bad(self):
        response = self.client.get("/articles/56/")
        self.assertEqual(response.status_code, 404)


class AuthorPageTest(TestCase):
    fixtures = ['fixtures1.json','fixture2.json', 'articles.json','fixturesqoutes.json']

    def test_author_view(self):
        response = self.client.get("/articles/authors/4c6ec3e0-0a8e-11e3-b1dc-0050569d4333/")
        self.assertEqual(response.status_code, 200)

    def test_author_template(self):
        response = self.client.get("/articles/authors/4c6ec3e0-0a8e-11e3-b1dc-0050569d4333/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/author.html')

    def test_author_context(self):
        response = self.client.get("/articles/authors/4c6ec3e0-0a8e-11e3-b1dc-0050569d4333/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('author' in response.context)
        self.assertTrue('recent_article' in response.context)


    def test_article_bad(self):
        response = self.client.get("/articles/authors/3/")
        self.assertEqual(response.status_code, 404)



# Testing the forms
class TestCommentForm(TestCase):

  def test_comment_form(self):
    # test invalid data
    invalid_data = {
      "body": "",
    }
    form = CommentForm(data=invalid_data)
    form.is_valid()
    self.assertTrue(form.errors)

    # test valid data
    valid_data = {
      "body": "comment test",
    }
    form = CommentForm(data=valid_data)
    form.is_valid()
    self.assertFalse(form.errors)
