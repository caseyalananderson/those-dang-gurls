# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.core.files import File  # you need this somewhere
import os

from django.test import TestCase

from food.models import FoodPost
from travel.models import TravelPost
from beauty.models import BeautyPost
from fitness.models import FitnessPost


# Create your tests here.


def populate_all_tables():
    for j in range(4):
        for i in range(8):

            if j == 0:
                db_item = TravelPost()
            elif j == 1:
                db_item = FitnessPost()
            elif j == 2:
                db_item = BeautyPost()
            elif j == 3:
                db_item = FoodPost()

            # Title
            db_item.published = True
            db_item.title = 'random_title_%s' % str(i)
            db_item.publish_date = datetime.datetime.today()

            # Get the image
            #image_url = 'file:///home/casey/baby_piglet.jpg'
            #result = urllib.urlretrieve(image_url) # image_url is a URL to an image
            #db_item.cover_photo.save(
            #    os.path.basename(image_url),
            #    File(open(result[0]))
            #    )

            db_item.summary = get_summary()
            db_item.content = get_content()
            db_item.youtube_link = 'https://www.youtube.com/watch?v=93hq0YU3Gqk'
            db_item.save()

    return

def get_summary():

    summary_str = r'''
    <h3>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</h3>
    
    '''

    return summary_str


def get_content():
    content_str = r'''
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    
    <img src="/media/uploads/beauty/IrananIronman/20140907_205946.jpg"  
    class="ui center large bordered rounded image">
    
       <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

    '''

    return content_str

