from django.db import models

class Dashboard(models.Model):
    pagename = models.CharField(max_length = 200,blank = False,unique = True)
    companyheaderlogo = models.CharField(max_length = 200)
    navigationheaderslink1 = models.CharField(max_length = 200)
    navigationheaderslink2 = models.CharField(max_length = 200)
    personlogo = models.CharField(max_length = 200)

    pagecontentlefttitle = models.CharField(max_length = 200)
    pagecontentlefttitleearn = models.CharField(max_length = 200)
    profileprogresslabel = models.CharField(max_length = 200)
    profileprogressvalue = models.IntegerField()

    pagerightimage = models.CharField(max_length = 200)
    pagerighttitle = models.CharField(max_length = 200)
    pagerightlogo = models.CharField(max_length = 200)
    pagerightcompany = models.CharField(max_length = 200)
    pagerightlogocaption = models.CharField(max_length = 200)

    pagerightdescription = models.CharField(max_length = 200)
    pagerightbuttonlabel = models.CharField(max_length = 200)

    pagebottomtitle = models.CharField(max_length = 200)
    pagebottomfilter = models.CharField(max_length = 200)

    pagebottomimagefirst = models.CharField(max_length = 200)
    pagebottombrandfirst = models.CharField(max_length = 200)
    pagebottombuttondescription = models.CharField(max_length = 200)
    pagebottombuttonlabel = models.CharField(max_length = 200)

    pagebottomimagesecond = models.CharField(max_length = 200)
    pagebottombrandsecond = models.CharField(max_length = 200)
    pagebottombuttonbranddescription = models.CharField(max_length = 200)
    pagebottombuttonbrandlabel = models.CharField(max_length = 200)

    personearn = models.IntegerField()

    def __str__(self):
        return self.pagename



