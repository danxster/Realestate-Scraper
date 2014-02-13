import MySQLdb
import sys
from datetime import datetime

# SCRAPY SETTING
BOT_NAME = 'realestate_com_au'
BOT_VERSION = '1.0'
DOWNLOAD_DELAY = 3
SPIDER_MODULES = ['realestate_com_au.spiders']
NEWSPIDER_MODULE = 'realestate_com_au.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# SQL DATABASE SETTING
SQL_DB = 'python'

time = 'buy_' + str(datetime.now().date())
SQL_TABLE = time.replace("-", "_")

SQL_HOST = 'localhost'
SQL_USER = 'root'
SQL_PASSWD = ‘password’

# connect to the MySQL server
try:
    CONN = MySQLdb.connect(host=SQL_HOST,
                         user=SQL_USER,
                         passwd=SQL_PASSWD,
                         db=SQL_DB)

except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

cursor = CONN.cursor()  # important MySQLdb Cursor object

#Create new table with todays date
cursor.execute('CREATE TABLE %s ( \
                                      realestate_id int(11) NOT NULL AUTO_INCREMENT, \
                                      propertyType tinytext NOT NULL, \
                                      siteid  VARCHAR(255) NOT NULL, \
                                      address tinytext NOT NULL, \
                                      price tinytext NOT NULL, \
                                      propertyType1 tinytext NOT NULL, \
                                      Bedrooms tinytext NOT NULL, \
                                      Bathrooms tinytext NOT NULL, \
                                      CarSpaces tinytext NOT NULL, \
                                      time_capt timestamp NOT NULL DEFAULT "0000-00-00 00:00:00" ON UPDATE CURRENT_TIMESTAMP, \
                                      PRIMARY KEY (realestate_id), \
                                      UNIQUE INDEX idx_name (siteid ) \
                                     ) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT="utf8_general_ci"' % (SQL_TABLE) \
               ) 
