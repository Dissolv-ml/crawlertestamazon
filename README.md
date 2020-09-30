# crawlertestamazon
An amazon data scraper for marketers that lets you enter the item you want to scrape and saves the resulting data to a CSV file.

# Amazon Product Scraper
This is an `Amazon Crawler` built using `scapy` module of `python`

# Features
Lets you enter any product you want to datamine. 
it scrape various things
- Product Title
- Product Price
- Product Rating
- Product Description
- Product Reviews
- Product Brand
- Product Colour




# Execute Amazon Scraper
there are two ways to execute scraper
### First one
you can directly execute `run.sh` file using shell but **please change the path to save the file #veryimportant
```sh
sh ./run.sh

### Second one
you can execute the following command
```bash
scrapy crawl amazoncrawler -o ./data/data.csv or specify path
```




# Troubleshooting
If csv file doesn't generate in proper format then just delete `data.csv` file .  
Now you good to go ;)

# Preresuisites
-  install `scrapy`
- install `pillow`



# WINDOWS
pip install scrapy
# LINUX
pip3 install scrapy
