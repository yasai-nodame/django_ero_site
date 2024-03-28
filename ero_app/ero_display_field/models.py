from django.db import models

class Ero_title(models.Model):
    title = models.CharField('',max_length=100)
    img = models.CharField('',max_length=150,null=False)
    
    def __str__(self):
        return self.title


#<input type="text" name="name" size=30 placeholder="キーワードを入力" class="example">