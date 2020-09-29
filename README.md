# crawlertestamazon
An amazon scraper that lets you enter the item you want to scrape and saves the resulting data to a CSV file.

# Amazon Product Scraper
This is an `Amazon Product Scraper` built using `scapy` module of `python`

# Features
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
scrapy crawl amazon_scraper -o ./data/data.csv or specify path
```




# Troubleshooting
If csv file doesn't generate in proper format then just delete `data.csv` file .  
Now you good to go ;)

# Preresuisites
- you have to install `scrapy`
- you have to install `pillow`


