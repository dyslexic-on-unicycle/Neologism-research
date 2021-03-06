# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import items
import re
import csv
class CsvPipeline(object):

####This will all change to something similar to what is in format data except it will be item['key'] not tuple and will use .format() method
    def __init__(self):
        self.item_count= 0

    def process_item(self, item, spider):
      
        if self.item_count < 1000000:
       		self.file_name="one"
       	elif self.item_count < 2000000:
       		self.file_name="two"
       	elif self.item_count < 3000000:
       		self.file_name="three"
       	elif self.item_count < 4000000:
       		self.file_name="four"
       	elif self.item_count < 5000000:
       		self.file_name="five"
       	elif self.item_count < 6000000:
       		self.file_name="six"
       	elif self.item_count < 7000000:
       		self.file_name="seven"
       	else:
       		self.file_name= "eight"

        with open('/home/dyslexicon/badger2/files/'+ self.file_name +'.txt','a+b') as csvfile:
        	csvfile.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(item['date'],item['post_numbers'],item['path'],item['author'],item['number'],item['post']))
        self.item_count += 1
### This produces a file with each row as: 'date \t uniqe post id \t forum title \t forum# \t thread title \t thread# \t author \t post # in thread \t the post'