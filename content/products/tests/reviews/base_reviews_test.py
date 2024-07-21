from django.urls import reverse
from core.tests import UniversalBaseTests

class BaseReviewsTest(UniversalBaseTests):
    def setUp(self):
        super().setUp()
        self.client = self.create_client(is_seller=True)
        self.review = self.create_review()
        self.api_url = reverse('products:reviews-list')
        self.api_url_detail = reverse('products:reviews-detail', kwargs={'pk': self.review.id})
           
        self.data = {      
          'comment': 'Product arrived in good condition and preserved, great product.',
          'rating': 4,
          'product': self.review.product.id,
        }
        
        self.payload = self.data.copy()
