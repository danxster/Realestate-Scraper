# Define here the models for your scraped items

from scrapy.item import Item, Field

class RealestateItem(Item):
     item_propertyType = Field()
     item_siteid = Field()
     item_address = Field()
     item_price = Field()
     item_propertyType1 = Field()
     item_Bedrooms = Field()
     item_Bathrooms = Field()
     item_CarSpaces = Field()
