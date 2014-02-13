Realestate-Scraper
==================

This is a scraper designed to crawl realestate.com.au

The scraper crawls all listings on the website and outputs the data into mysql.

The scraper is designed to run once a day.



How it Works
==================

A cron job should be setup to execute the getdata.sh script.

From there the properties for sales and the properties for rent are scraped from a list of postcodes stored in mysql.

Features
==================

realestate.com.au generates a unique id for each listing. As I export the listings in mysql the id is checked and skiped if the id already exists.

