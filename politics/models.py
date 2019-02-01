from django.db import models
from django.urls import reverse

class Debate(models.Model):
    username = models.CharField(max_length =20 , blank=True, default='')
    title = models.CharField(max_length = 200, blank=True, default='')
    date = models.CharField(max_length =10, blank=True, default='')
    #maybe add tags or hashtags
    genre = models.CharField(max_length = 20, blank=True, default='')
    #background
    picture = models.FileField()
    #profile picture
    pfp = models.CharField(max_length =12, blank=True, default='')
    
    def __str__(self):
        return self.title + ' - ' + self.username
    
    def get_absolute_url(self):
        return reverse('politics:detail', kwargs={'pk': self.pk})
        
    
    
class Comments(models.Model):
    debate = models.ForeignKey(Debate, on_delete= models.CASCADE)
    username = models.CharField(max_length =20, blank=True, default='')
    comment = models.CharField(max_length =1000, blank=True, default='')
    date = models.CharField(max_length =10, blank=True, default='DEFAULT VALUE')
    side = models.BooleanField(default = True)
    #profile picture
    pfp = models.CharField(max_length =12, blank=True, default='DEFAULT VALUE')
    #like or dislike
    like = models.BooleanField(default = True)
    
    def __str__(self):
        return self.comment + '-' + self.username
 
    
class Voting(models.Model):
    debate2 = models.ForeignKey(Debate, on_delete= models.CASCADE)
    pro = models.IntegerField()
    con = models.IntegerField()
    
class Likes(models.Model):
    comments = models.ForeignKey(Comments, on_delete= models.CASCADE)
    like = models.IntegerField()
    dislike = models.IntegerField()