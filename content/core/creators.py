'''
creators.py

This module provides all types of creation of different model objects such as: clients, products,
categories, review and more.

Classes:

    Creatoes: Base class for tests, providing methods for creating clients, addresses, categories, products, reviews, tags, orders, and order items.

Author:
    PyPeu (heronalfo)
'''

from typing import Optional, Dict
from django.test import TestCase
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from products.models import Product, Category, Review, Tag
from accounts.models import Costumer, Address
from orders.models import Order, OrderItem
from carts.models import Wishlist

class Creators:
    def create_client(
        self,
        username: str = 'user-for-testing',
        password: str = 'BlazU12X912',
        email: str = 'test@gmail.com',
        is_seller: bool = False
    ) -> [APIClient, Costumer]:
        '''
        Helper method to create an authenticated client.

        Args:
            username (str): The username of the client.
            password (str): The password of the client.
            email (str): The email of the client.
            is_seller (bool): Whether the client is a seller.

        Returns:
            APIClient: The authenticated client.
        '''
        client = APIClient()

        self.costumer = Costumer.objects.create_user(
            username=username,
            password=password,
            email=email,
            is_seller=is_seller
        )

        client.force_authenticate(self.costumer)
        refresh = RefreshToken.for_user(user=self.costumer)
        token = str(refresh.access_token)
        
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        return client
    
    def create_address(
        self,
        street: str = 'Aristides Fransico dos Santos',
        cep: str = '0000-000',
        number: int = 27,
        city: str = 'Euclides da Cunha',
        uf: str = 'BA',
        neighborhood: str = 'Dengo',
        complement: str = 'Vizinho da rita do bolo e o omarinho do carro pipa'
    ) -> Address:
        '''
        Helper method to create an address.

        Args:
            street (str): The street of the address.
            cep (str): The postal code of the address.
            number (int): The number of the address.
            city (str): The city of the address.
            uf (str): The state of the address.
            neighborhood (str): The neighborhood of the address.
            complement (str): The complement of the address.

        Returns:
            Address: The created address.
        '''
        address = Address.objects.create(
            street=street,
            cep=cep,
            number=number,
            city=city,
            uf=uf,
            neighborhood=neighborhood,
            complement=complement,
            costumer=self.costumer
        )

        return address

    def create_category(
        self, 
        name: str = 'category',
        description: str = 'description'
    ) -> Category:
        '''
        Helper method to create a category.

        Args:
            name (str): The name of the category.
            description (str): The description of the category.

        Returns:
            Category: The created category.
        '''
        category = Category.objects.create(
            name=name,
            description=description,
        )

        return category

    def create_product(
        self,
        seller: Optional[Costumer] = None,
        name: str = 'Product Name',         
        description: str = 'Description', 
        category: Optional[Category] = None, 
        price: float = 19.99, 
        brand: str = 'Brand', 
        stock: int = 99
    ) -> Product:

        '''
        Helper method to create a product.

        Args:
            seller (Costumer, optional): The seller of the product.
            name (str): The name of the product.
        description (str): The description of the product.
        category (Category, optional): The category of the product.
        price (float): The price of the product.
        brand (str): The brand of the product.
        stock (int): The stock of the product.

    Returns:
        Product: The created product.
    '''
        if seller is None:
            seller = self.costumer
        if category is None:
            category = self.create_category()
    
        product = Product.objects.create(
            seller=seller,
            name=name,
            description=description,        
            category=category,
            price=price,
            brand=brand,
            stock=stock,
        )
    
        return product

    def create_review(
        self,
        comment: str = 'Product perfect!',
        rating: int = 4,
    ) -> Review:
        '''
        Helper method to create a review.
    
        Args:
            comment (str): The comment of the review.
            rating (int): The rating of the review.
    
        Returns:
            Review: The created review.
        '''
        review = Review.objects.create(
            product_id=self.create_product().id,
            costumer=self.costumer,
            comment=comment,
            rating=rating,
        )
    
        return review
    
    def create_tag(self, name: str = 'Product') -> Tag:
        '''
        Helper method to create a tag.
    
        Args:
            name (str): The name of the tag.
    
        Returns:
            Tag: The created tag.
        '''
        tag = Tag.objects.create(name=name)
    
        return tag
    
    def create_order(self) -> Order:
        '''
        Helper method to create an order.
    
        Returns:
            Order: The created order.
        '''
        order = Order.objects.create(costumer=self.costumer)
    
        return order
    
    def create_item(self, product: Optional[Product] = None, quantity: int = 12) -> OrderItem:
        '''
        Helper method to create an order item.
    
        Args:
            product (Product, optional): The product of the order item.
            quantity (int): The quantity of the order item.
    
        Returns:
            OrderItem: The created order item.
        '''
        if product is None:
            product = self.create_product()
        
        item = OrderItem.objects.create(
            product=product,
            quantity=quantity
        )
    
        return item
    
    def create_wishlist(self):
        '''
        Helper method to create an wishlist item.
        
        Returns:
            The wishlist product created.
        '''
    
        wishlist = Wishlist.objects.create(
            costumer=self.costumer,
            product=self.create_product(),
        )
    
        return wishlist
