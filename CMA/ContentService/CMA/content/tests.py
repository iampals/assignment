from django.test import TestCase
from .models import Dashboard

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):

    def setUp(self):
        self.dashboard_pagename = "Test_Page"
        self.dashboard_companyheaderlogo = "test.png"
        self.dashboard_navigationheaderslink1 = "Contact"
        self.dashboard_navigationheaderslink2 = "Career"
        self.dashboard_personlogo = "test.png"

        self.dashboard_pagecontentlefttitle = "test.png"
        self.dashboard_pagecontentlefttitleearn = "test.png"
        self.dashboard_profileprogresslabel = "progress"
        self.dashboard_profileprogressvalue = 20
        self.dashboard_pagerightimage = "test.png"
        self.dashboard_pagerighttitle = "profile complete"
        self.dashboard_pagerightlogo = "test.png"
        self.dashboard_pagerightcompany = "Mannar and Mannar"
        self.dashboard_pagerightlogocaption = "Healthy"
        self.dashboard_pagerightdescription = "Check your health"
        self.dashboard_pagerightbuttonlabel = "button"
        self.dashboard_pagebottomtitle = "Juice"
        self.dashboard_pagebottomfilter = "Order"
        self.dashboard_pagebottomimagefirst = "test.png"
        self.dashboard_pagebottombrandfirst = "K and K"
        self.dashboard_pagebottombuttondescription = "Let live"
        self.dashboard_pagebottombuttonlabel = "test"
        self.dashboard_pagebottomimagesecond = "test.png"
        self.dashboard_pagebottombrandsecond = "Mck"
        self.dashboard_pagebottombuttonbranddescription = "test test test code"
        self.dashboard_pagebottombuttonbrandlabel = "Click"
        self.dashboard_personearn = 1

        self.dashboard = Dashboard(
            pagename = self.dashboard_pagename,
            companyheaderlogo = self.dashboard_companyheaderlogo,
            navigationheaderslink1 = self.dashboard_navigationheaderslink1,
            navigationheaderslink2 = self.dashboard_navigationheaderslink2,
            personlogo = self.dashboard_personlogo,

            pagecontentlefttitle = self.dashboard_pagecontentlefttitle,
            pagecontentlefttitleearn = self.dashboard_pagecontentlefttitleearn,

            profileprogresslabel = self.dashboard_profileprogresslabel,
            profileprogressvalue = self.dashboard_profileprogressvalue,

            pagerightimage = self.dashboard_pagerightimage,
            pagerighttitle = self.dashboard_pagerighttitle,

            pagerightlogo = self.dashboard_pagerightlogo,
            pagerightcompany = self.dashboard_pagerightcompany,

            pagerightlogocaption = self.dashboard_pagerightlogocaption,
            pagerightdescription = self.dashboard_pagerightdescription,

            pagerightbuttonlabel = self.dashboard_pagerightbuttonlabel,
            pagebottomtitle = self.dashboard_pagebottomtitle,

            pagebottomfilter = self.dashboard_pagebottomfilter,
            pagebottomimagefirst = self.dashboard_pagebottomimagefirst,

            pagebottombrandfirst = self.dashboard_pagebottombrandfirst,
            pagebottombuttondescription = self.dashboard_pagebottombuttondescription,

            pagebottombuttonlabel = self.dashboard_pagebottombuttonlabel,
            pagebottomimagesecond = self.dashboard_pagebottomimagesecond,

            pagebottombrandsecond =self.dashboard_pagebottombrandsecond,
            pagebottombuttonbranddescription =self.dashboard_pagebottombuttonbranddescription,
            pagebottombuttonbrandlabel = self.dashboard_pagebottombuttonbrandlabel,
            personearn = self.dashboard_personearn,

        )


    def test_model_can_create_a_dashboard(self):
        old_count = Dashboard.objects.count()
        self.dashboard.save()
        new_count = Dashboard.objects.count()
        self.assertNotEqual(old_count, new_count)

"""
class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.dashboard_data = {
            'pagename':'Test_Page',
            'companyheaderlogo' : 'test.png',
            'navigationheaderslink1' : "Contact",
            'navigationheaderslink2' : "Career",
            'personlogo' :"test.png",

            'pagecontentlefttitle' : 'test.png',
            'pagecontentlefttitleearn' : 'test.png',
            'profileprogresslabel' : 'progress',
            'profileprogressvalue' : 20,
            'pagerightimage': 'test.png',
            'pagerighttitle' : 'profile complete',
            'pagerightlogo' :'test.png',
            'pagerightcompany' : 'Mannar and Mannar',
            'pagerightlogocaption' : 'Healthy',
            'pagerightdescription' : 'Check your health',
            'pagerightbuttonlabel' : 'button',
            'pagebottomtitle' : 'Juice',
            'pagebottomfilter' : 'Order',
            'pagebottomimagefirst' : 'test.png',
            'pagebottombrandfirst' : 'K and K',
            'pagebottombuttondescription' : 'Let live',
            'pagebottombuttonlabel' : 'test',
            'pagebottomimagesecond' : 'test.png',
            'pagebottombrandsecond' :'Mck',
            'pagebottombuttonbranddescription' : 'test test test code',
            'pagebottombuttonbrandlabel' : 'Click',
            'personearn' : 1

        }
        self.response = self.client.post(
            reverse('create'),
            self.dashboard_data,
            format="json"
        )

    def test_api_can_create_a_dashboard(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_dashboard(self):
        dashboard = Dashboard.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': dashboard.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, dashboard)

    def test_api_can_update_dashboard(self):
        # dashboard.id = 1;
        change_dashboard = {'pagename': 'Test_Page'}
        res = self.client.put(
            reverse('details', kwargs={'pk': 1}),
            change_dashboard, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_dashboard(self):
        dashboard = Dashboard.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': dashboard.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
"""

