# Web Scrapping and Analysing the data
In our research, we have chosen many web-sites for data parsing. But we found the Alser store better. Obviously this website, which we choose, is the biggest electronic online shop in Kazakhstan. Most people in Kazakhstan use these websites for buying smartphones. Data in these web-sites is very important and this data needs to be analyzed. We used this webpage to scrap:
 - https://alser.kz/c/vse-smartfony

And collected data from one categorie(Smartphones). During the project we used the following libraries:
```python
import urllib.request
import requests
import urllib.parse
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
```

Before starting analyze our dataset, we stored all our data in CSV file. For instance:
![alt text](https://github.com/toolbassy/alser/blob/main/csv.png?raw=true)

Then after cleaning and transformating our dataset using data visualization modules made such kind of plots. This one demonstrates the density of smartphone with such kind of phone memories and prices:
![alt text](https://github.com/toolbassy/alser/blob/main/plot1.png?raw=true)

For instance, here you can see the feature correlation of our data, we can easily notice which attribute has a great relation between ‘price’ which is a key attribute of the project.
![alt text](https://github.com/toolbassy/alser/blob/main/plot2.png?raw=true)

Additionally, the iOS operating system is a key reason for the fact that iPhones are widely developed and sold phones in the world. Let’s look at the graph below:
![alt text](https://github.com/toolbassy/alser/blob/main/plot3.png?raw=true)

As it can be seen in the results, most of the big companies are more interested in
Android platform while Apple prefers to use its own operating system. In addition, the average price of iOS gadgets is twice as expensive as that of the second. 
Summing up the results of the work done, we can say that we have answered the research questions that we extracted at the beginning of the project.Taking the various electronics websites, we created a dataset with one of them that was analyzed using Python libraries (NumPy, Pandas, BeautifulSoup) and provided us with the necessary information. 
