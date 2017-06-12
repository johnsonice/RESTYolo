import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

import django 
django.setup()

## FAKE POP SCRIPT 
import random 
from yolo.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker() ## generate faker instance 
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name = random.choice(topics))[0] ## pick random word from topics 
    t.save()                                                           ## save it 
    return t 

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry 
        top = add_topic()
        
        # Create the fake data for that entry 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # Create the new webpage entry 
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0] # topic is the foreign key here
        
        #Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]  #name is the foreign key here

if __name__=='__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')
        