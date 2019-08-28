from django.db import models
import datetime as dt

# Create your models here.

class Editor(models.Model):
    
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['first_name']
        
    def save_editor(self):
        self.save()
        
    
    
class Tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    #ONE ARTICLE = MANY EDITORS
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(Tags)
    #PUBDATE IS DATE ARTICLE WAS PUBLISHED
    
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', default='')
    
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    
    @classmethod
    def days_news(cls, date):
        news=cls.objects.filter(pub_date__date=date)
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
    ''' def title (self):
        return self.title
    
    def save_article(self):
        self.save()
        
    def delete_Article(self):
        self.delete()
        '''
        
        
    
    
class NewsLetterRecipients(models.Model):
    name=models.CharField(max_length=30) 
    email=models.EmailField() 