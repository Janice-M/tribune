from django.test import TestCase
from .models import Editor,Article,Tags
import datetime as dt
from django.test import TestCase
from .models import Editor,Article,Tags
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.grey=Editor(first_name='grey',last_name='worm',email='grey@gmail.com')

    def test_instance(self):
        '''
        Testing Instance
        '''
        self.assertTrue(isinstance(self.brian,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.brian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)  

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.janice= Editor(first_name = 'Janice', last_name ='Muthoni', email ='jmuthoni@moringaschool.com')
        self.janice.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
# Create your tests here.

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.golda=Editor(first_name='golda',last_name='nkirote',email='nkirote@gmail.com')

    def test_instance(self):
        '''
        Testing Instance
        '''
        self.assertTrue(isinstance(self.brian,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.golda.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)  

class ArticleTestClass(TestCase):

    ''' def setUp(self):
        # Creating a new editor and saving it
        self.salif= Editor(first_name = 'Salif', last_name ='Keita', email ='salifkey@moringaschool.com')
        self.salif.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.salif)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)  '''