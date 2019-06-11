**-----------MetaCriticScraper-----------**

My first side project after Graduating. This was my first ever Python project, and the basis for a bot I made for use on Facebook. 
The purpose of this project was to create a script which would randomly return a review from the popular review site 'MetaCritic'.
Through the development of this bot, I learned some of the fundamentals of development in Python, as well as became more familiar with
the idea of Virtual environments for Python, 'Pip' and even gained some experience with AWS through the Facebook integrated version of the
program I have for personal use. This incarnation of the project posted to a Facebook page called 'MetaCriticReviewBot3'. As of 11/06/2019
you can still see the functionality of this bot firsthand without having to download by checking this page out.

The AWS experience I gained through the development of this side project was the setup of a Amazon Linux server using ES2. This allowed
me to set up the scheduled execution of the script using a crontab, ensuring regular content posts on the Facebook page. 

This incarnation of the bot requires the installation of BeautifulSoup, a popular web scraper. The Facebook incarnation also makes use
of the Facebook-SDK. The non-Facebook program consists of 6 methods, which execute linearly;

**Preface Notes:** 
 For each step of the process, a method will accept an 'output' field. This is simply a boolean which, if true, will enable the printing of the output of that stage. This is mainly for testing purposes. 

  1. genre_get:  
      This is the method which handles selection of a genre. The 'output' field passed to this method is a boolean which defines whether
      or not you want to print the list it creates. It creates an array of each hyperlink from the 'genre_nav' div on the                     'https://www.metacritic.com/game" page. With this array ready, it is then passed to the next method, genre_picker.
      
  2. genre_picker:
      This method again has an 'output' field as well as the array of links passed to it by genre_get. This is a simple method, which         makes use of the 'random' import to choose randomly from the link_list. This random choice, 'genre' is then passed to our next           method game_get.
      
  3. game_get:
      This method is functionality the same to genre_get. Instead of creating an array of hyperlinks for the genre, it creates an array       of hyperlinks extracted from the 'list_products' ordered list on the Metacritic page passed from genre_picker. Just as in               genre_get, this list is passed to its 'picker' class, game_picker. 
      
  4. game_picker:
      Mirroring the actions of genre_picker, this will select a list item at random from the 'game_list'. (game_picker and genre_picker       perform the same functionality. To optimise this script, I would condense game_picker and genre_picker into a simple                     'listitem_picker', however for the sake of showing the flow of the script, I've left it in.) Once the list item has been picked,         it is passed to the info_get method.
      
  5. info_get:    
      This method scrapes the product details from the game page provided by the game_picker. It gets the product title (Name of the           game), the platform (What console the game was released on) and the critic score (out of 100). It then formats this information         and passes it to the review_get method alongside the link for user reviews of the product.
      
  6. review_get:
      review_get is the most involved of the functions. It checks for reviews, and restarts the process if there are none. It also gets       an array of reviews and makes a random selection on which of these reviews to use. From the chosen review it strips the:
      
          a. Username of reviewer
          b. Score given by reviewer
          c. Contents of the review
          d. Date of review
          
      This information is then formatted as with 'info_string', then combined with 'info_string' to the 'post_string'. At which point         the review is printed. By default, only review_get is set to output. 
      
**General Information**

This program was not developed with any SOLID priciples in mind, or with the forethought to comment within the code (Hence the lengthy description of methods). Mainly carried out as a challenge for myself to tide off the exhaustion of being unemployed. This was my first Python project and I'm pretty happy with it. It's not perfect but it always outputs something. The errors it can encounter are covered, and it isn't really designed to be changed. 
      
      
      
      
      
