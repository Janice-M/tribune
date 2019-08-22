from django.test import TestCase
from .models import Editor, Article, tags
# Create your tests here.

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.grey= Editor(first_name = 'grey', last_name ='worm', email ='janiceink001@gmail.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.grey,Editor))
    # Testing Save Method
    def test_save_method(self):
        self.grey.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
