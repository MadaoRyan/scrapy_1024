# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import json
#import codecs
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

class MyprojPipeline(ImagesPipeline):
#    def __init__(self):
#        self.file=codecs.open('test.json',mode='wb',encoding='utf-8')
#        
#    def process_item(self, item, spider):
#        line = json.dumps(dict(item)).decode("unicode-escape")+"\n"
#        self.file.write(line)
#        return item
#    def close_spider(self, spider):
#        self.file.close()
    #def file_path(self, request, response=None, info=None):
    #    item=request.meta['item']
    #    folder=item['name'].decode('unicode_escape')
    #    folder_strip=strip(folder)
    #    #image_guid =u'full/{0}/{1}'.format(folder_strip,request.url.split('/')[-1])
    #    image_guid=request.url.split('/')[-1]
    #    print image_guid + folder_strip
    #    return '%s/%s'%(folder_strip) %(image_guid)
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print image_url+'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            yield Request(image_url)
    #def item_completed(self, results, item, info):
    #    image_paths  = [x['path'] for ok, x in results if ok]
    #    if not image_paths :
    #        raise DropItem("Item containts no images")
    #    item['image_paths'] = image_paths
    #    return item
    def convert_image(self, image, size=None):
        buf = BytesIO()
        image.save(buf)
        return image, buf
    def strip(path):
        path = re.sub(r'[?\\*|"<>:/]','',str(path))
        return path
