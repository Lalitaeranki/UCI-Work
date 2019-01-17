# Instructions

In this activity, you will visit unspash.com and surfline.com to scrape the weather report for a location such as santa-barbara. 

## Steps:
1. Use splinter to visit `https://unsplash.com/search/photos/surfing` and then create a soup object from the page.
2. Find the image src and save that link.
3. Use splinter to visit `http://www.surfline.com/surf-forecasts/southern-california/santa-barbara_2141` and then create a soup object from the page. 
4. Find all of the paragraph tags for the articles and save those as a list.
5. From the scrape function, return the image src and the article paragraphs as a python dictionary.