# coffee-quality-data-CQI
This repo consists of CQI coffee quality data and web scraping codes in python 

# Coffee Quality Institute 
The Coffee Quality Institute (CQI) is a non-profit organization that works to improve the quality and value of coffee worldwide. It was founded in 1996 and has its headquarters in California, USA.

CQI's mission is to promote coffee quality through a range of activities that include research, training, and certification programs. The organization works with coffee growers, processors, roasters, and other stakeholders to improve coffee quality standards, promote sustainability, and support the development of the specialty coffee industry.

# Data
CQI maintains a web database that serves as a resource for coffee professionals and enthusiasts who are interested in learning about coffee quality and sustainability. The database includes a range of information on coffee production, processing, and sensory evaluation. It also contains data on coffee genetics, soil types, and other factors that can affect coffee quality.

## Sensory evaluations (coffee quality scores)
* *Aroma:* Refers to the scent or fragrance of the coffee.
* *Flavor:* The flavor of coffee is evaluated based on the taste, including any sweetness, bitterness, acidity, and other flavor notes.
* *Aftertaste:* Refers to the lingering taste that remains in the mouth after swallowing the coffee.
* *Acidity:* Acidity in coffee refers to the brightness or liveliness of the taste.
* *Body:* The body of coffee refers to the thickness or viscosity of the coffee in the mouth.
* *Balance:* Balance refers to how well the different flavor components of the coffee work together.
* *Uniformity:* Uniformity refers to the consistency of the coffee from cup to cup.
* *Clean Cup:* A clean cup refers to a coffee that is free of any off-flavors or defects, such as sourness, mustiness, or staleness.
* *Sweetness:* It can be described as caramel-like, fruity, or floral, and is a desirable quality in coffee.

## Defects
Defects are undesirable qualities that can occur in coffee beans during processing or storage. Defects can be categorized into two categories: Category One and Category Two defects.

Category One defects are primary defects that can be perceived through visual inspection of the coffee beans. These defects include: Black beans, sour beans, insect-damaged beans, fungus-damaged beans etc.

Category Two defects are secondary defects that are more subtle and can only be detected through tasting. These defects include: Over-fermentation, staleness, rancidness, chemical taste etc.

## Data Scraping
On this part, great thanks to [James LeDoux](https://github.com/jldbc). His repo [coffee-quality-database](https://github.com/jldbc/coffee-quality-database) from 2018 is efficiently written and well documented. To scrape the data, I used most of his code, but due to some changes on the website, I modified some of the lines. Also, some practices on modules deprecated and deleted so I updated those codes also. Therefore, on May-2023 we can use this updated python program to scrape data from this database.

In this repo, you can find the python file for scraping -> [scraper_bot.py](https://github.com/fatih-boyar/coffee-quality-data-CQI/blob/main/scraper_bot.py)

After collecting the tables, some processing needed to construct a tabular data -> [process_tables_f.py](https://github.com/fatih-boyar/coffee-quality-data-CQI/blob/main/process_tables_f.py)

The raw table after processing can be found on -> [df_1_arabica.csv](https://github.com/fatih-boyar/coffee-quality-data-CQI/blob/main/df_1_arabica.csv)

Tabular data is not so dirty but a bit cleaning was usefull -> [data_cleaning.py](https://github.com/fatih-boyar/coffee-quality-data-CQI/blob/main/data_cleaning.py)

Finally, clean data can be found as a .csv file in this repo -> [df_arabica_clean.csv](https://github.com/fatih-boyar/coffee-quality-data-CQI/blob/main/df_arabica_clean.csv)


Only data collected for the arabica type. With a few modification in [scraper_bot.py](https://github.com/fatih-boyar/coffee-quality-data-CQI/blob/main/scraper_bot.py), scraping can be easily replicated for robusta types also.
