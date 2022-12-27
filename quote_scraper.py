from bs4 import BeautifulSoup
import requests, string, random
import numpy as np

def scrape_and_clean(search_prompt):
  div_quotes = []
  pages = np.arange(1, 6, 1)
  for page in pages:
    page = requests.get("http://www.goodreads.com/quotes/search?commit=Search&page=" + str(page) + "&q=" + search_prompt + "&utf8=%E2%9C%93)")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # https://www.goodreads.com/quotes/search?commit=Search&page=4&q=rc+sproul&utf8=%E2%9C%93
    div_quotes += soup.find_all("div", attrs={"class":"quoteText"})
  quotes = ''
  for q in div_quotes:
    source = ""
    author = ""
    try:
      author = q.find('span', href=False).get_text() + "\n"
      source = q.find("a").get_text() + "\n"
    except:
      continue
    quote = ""
    for i in range(len(q.contents)):
      line = q.contents[i].encode("ascii", errors = "ignore").decode("utf-8")
      if (line[0]=='<'):
        break
      else:
        quote += line
      quote = q.contents[0].encode("ascii", errors = "ignore").decode("utf-8")
      quote = "\"" + quote.strip() + "\""
      author_and_source = author + source
      quotes += quote + "\n" + '-' + " ".join(author_and_source.split()) + "#"
  quotes_to_return = filter(lambda x: x in string.printable, quotes) #clean
  return quotes_to_return
  # return quotes_to_return

def main():
  search_string = ''
  prompt = input("What subject would you like to find a quote about: ").split()
  search_string = "+".join(prompt)
  # if len(prompt) > 1:
  #   search_string = prompt.join("+")
  # else:
  #   search_string = prompt
  
  quotes = "".join(scrape_and_clean(search_string)).split("#")

  if len(quotes) == 1:
    quote = quotes.pop()
  elif len(quotes) == 0:
    quote = "No quotes found, try another prompt"
  else:
    quote = random.choice(quotes)

  return quote
# scrape_and_clean('https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=hello&commit=Search')