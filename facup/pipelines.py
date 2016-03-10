# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.exporters import CsvItemExporter


class FacupPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline


		#create files and instantiate exporter class
		#then run start_exporting() method, this is required for item exporter class
	def spider_opened(self, spider):
		self.results_csv = open('results_3.csv', 'wb') 
		self.missing_csv = open('results_miss_2.csv', 'wb') 
		self.results_exporter = CsvItemExporter(self.results_csv)
		self.missing_exporter = CsvItemExporter(self.missing_csv)
		self.results_exporter.start_exporting() 
		self.missing_exporter.start_exporting() 
		
    def process_item(self, item, spider):
		self.results_exporter = CsvItemExporter(self.results_csv)
		self.missing_exporter = CsvItemExporter(self.missing_csv)
        return item
		
    def spider_closed(self, spider):
		self.results_exporter.finish_exporting() 
		self.missing_exporter.finish_exporting() 
		self.results_csv.close()
		self.missing_csv.close()
