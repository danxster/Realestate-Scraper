# Spider Requirements
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from realestate_com_au.settings import *
from realestate_com_au.items import *
from MySQLdb import escape_string

#Encode problematic string
def encode(str):
    return str.encode('utf8', 'ignore')

#Insert Data  into MySQL
def insert_table(datas):
    sql = "INSERT IGNORE INTO %s (propertyType, siteid, address, price, propertyType1, Bedrooms, Bathrooms, CarSpaces, time_capt) \
values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', NOW())" % (SQL_TABLE,
    escape_string(datas['item_propertyType']),
    escape_string(datas['item_siteid']),    
    escape_string(datas['item_address']),
    escape_string(datas['item_price']),
    escape_string(datas['item_propertyType1']),
    escape_string(datas['item_Bedrooms']),
    escape_string(datas['item_Bathrooms']),
    escape_string(datas['item_CarSpaces'])
    )
    # print sql
    if cursor.execute(sql):
        print "Inserted"
    else:
        print "Duplicate"

class RealestateSpider(CrawlSpider):
    #Name of program to call
    name = 'real'
    #--------Start URL
    #1. Select Mysql table with postcodes
    cursor.execute('SELECT postcode FROM postcodes')
    #2. Fill "postcodes" with Mysql data
    postcodes = cursor.fetchall()
    begin_url = 'http://www.realestate.com.au/buy/in-qld+'
    end_url = '%3b+/list-1'
    start_urls = []
    for i in postcodes:
        #3. make the url
        url = begin_url + i[0] + end_url
        #4. append all urls into a list
        start_urls.append(url)

        #Rule to follow Next Button
        rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//li[@class="nextLink"]',))
        , callback="parse_start_url",  follow=True),
        )

        def parse_start_url(self, response):
            hxs = Selector(response)
            #Scan Listings
            items = hxs.xpath('//div[@data-content-type]')
            #For each listing found display: propertyType, siteid, address, price, propertyType1, Bedrooms, Bathrooms, CarSpaces
            for item in items:
                realestate = RealestateItem()
                #List item_propertyType
                realestate['item_propertyType'] = item.xpath('@data-content-type').extract()[0] \
                                                  if len(item.xpath('@data-content-type').extract()) > 0 else 'NULL'
                #List item_siteid
                realestate['item_siteid'] = item.xpath('@id').extract()[0] \
                                            if len(item.xpath('@id').extract()) > 0 else 'NULL'
                #List item_address
                realestate['item_address'] = item.xpath('div/div/div/h2/a/text()|div/div/h2/a/text()|div/h2/a/text()').extract()[0] \
                                             if len(item.xpath('div/div/div/h2/a/text()|div/div/h2/a/text()|div/h2/a/text()').extract()) > 0 else 'NULL'
                #List item_price
                realestate['item_price'] = encode(item.xpath('div/div/div/div/p/span/text()|div/div/div/p/span/text()|div/div/p/span/text()|div/p/span/text()').extract()[0] \
                                           if len(item.xpath('div/div/div/div/p/span/text()|div/div/div/p/span/text()|div/div/p/span/text()|div/p/span/text()').extract()) > 0 else 'NULL')
                #List item_propertyType1
                realestate['item_propertyType1'] = item.xpath('div/div/div/span/text()|div/div/span/text()|div/span/text()').extract()[0] \
                                                   if len(item.xpath('div/div/div/span/text()|div/div/span/text()|div/span/text()').extract()) > 0 else 'NULL'
                #List item_Bedrooms
                realestate['item_Bedrooms'] = item.xpath('div/div/div/ul/li[1]/span/text()|div/div/ul/li[1]/span/text()|div/ul/li[1]/span/text()').extract()[0] \
                                              if len(item.xpath('div/div/div/ul/li[1]/span/text()|div/div/ul/li[1]/span/text()|div/ul/li[1]/span/text()').extract()) > 0 else 'NULL'
                #List item_Bathrooms
                realestate['item_Bathrooms'] = item.xpath('div/div/div/ul/li[2]/span/text()|div/div/ul/li[2]/span/text()|div/ul/li[2]/span/text()').extract()[0] \
                                               if len(item.xpath('div/div/div/ul/li[2]/span/text()|div/div/ul/li[2]/span/text()|div/ul/li[2]/span/text()').extract()) > 0 else 'NULL'
                #List item_CarSpaces
                realestate['item_CarSpaces'] = item.xpath('div/div/div/ul/li[3]/span/text()|div/div/ul/li[3]/span/text()|div/ul/li[3]/span/text()').extract()[0] \
                                               if len(item.xpath('div/div/div/ul/li[3]/span/text()|div/div/ul/li[3]/span/text()|div/ul/li[3]/span/text()').extract()) > 0 else 'NULL'
                #Insert into MySQL
                insert_table(realestate)
