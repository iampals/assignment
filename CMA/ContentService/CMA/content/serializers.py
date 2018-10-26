from rest_framework import serializers
from .models import Dashboard

class DashboardSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'pagename',
            'companyheaderlogo',
            'navigationheaderslink1',
            'navigationheaderslink2',
            'personlogo',

            'pagecontentlefttitle',
            'pagecontentlefttitleearn',
            'profileprogresslabel',
            'profileprogressvalue',

            'pagerightimage',
            'pagerighttitle',
            'pagerightlogo',
            'pagerightcompany',
            'pagerightlogocaption',

            'pagerightdescription',
            'pagerightbuttonlabel',

            'pagebottomtitle',
            'pagebottomfilter',

            'pagebottomimagefirst',
            'pagebottombrandfirst',
            'pagebottombuttondescription',
            'pagebottombuttonlabel',

            'pagebottomimagesecond',
            'pagebottombrandsecond',
            'pagebottombuttonbranddescription',
            'pagebottombuttonbrandlabel',

            'personearn',
        )
        model=Dashboard