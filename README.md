# Web Scraping - Mission to Mars :ringed_planet: :woman_astronaut:

Built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a HTML page.

<img src="https://blogs.nasa.gov/redplanetdispatch/wp-content/uploads/sites/279/2018/03/Mars-Website-banner-1024x309.jpg" width="100%">

## Part  1: Scraping

Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. Assigned the text to variables to reference later.

<img src="https://github.com/blancacarretero/web-scraping/blob/main/images/NASA_news.png?raw=true" width="80%">

### JPL Mars Space Images—Featured Image

* Visited the URL for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assigned the URL string to a variable called `featured_image_url`.

<img src="https://github.com/blancacarretero/web-scraping/blob/main/images/mars_featured_img.jpg?raw=true" width="60%">

### Mars Facts

* Visited the [Mars Facts webpage](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including diameter, mass, etc.

<img src="https://github.com/blancacarretero/web-scraping/blob/main/images/mars_info_table.png?raw=true">

* Used Pandas to convert the data to a HTML table string:
```HTML
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mars</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Diameter:</td>
      <td>6,779 km</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mass:</td>
      <td>6.39 × 10^23 kg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Moons:</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Distance from Sun:</td>
      <td>227,943,824 km</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Length of Year:</td>
      <td>687 Earth days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Temperature:</td>
      <td>-87 to -5 °C</td>
    </tr>
  </tbody>
</table>
```

### Mars Hemispheres

* Visited the [astrogeology site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars.

* Saved the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image URL string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
{'title': 'Valles Marineris Hemisphere', 'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}
{'title': 'Cerberus Hemisphere', 'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'}
{'title': 'Schiaparelli Hemisphere', 'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'}
{'title': 'Syrtis Major Hemisphere', 'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'}
```

## Part 2: MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` by using a function called `scrape`. This function should  execute all your scraping code from above and return one Python dictionary containing all the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.

* Create a template HTML file called `index.html` that will take the Mars data dictionary and display all the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

![final_app_part1.png](Images/final_app.png)

- - -




