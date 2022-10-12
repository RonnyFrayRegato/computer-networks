# Requests 0: Basic Get Requests with Soup

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import sys

if __name__ == '__main__':

    wikipedia = "https://en.wikipedia.org/wiki"

    for term in sys.argv[1:]:
        # create the appropriate GET URL
        url = f'{wikipedia}/{term}_(disambiguation)'

        # gets website URL and provides response
        # if error - exits with exception
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as httperr:
            print(f'HTTP error: {httperr}')
            sys.exit(1)
        except Exception as err:
            print(f"Something went really wrong!: {err}")
            sys.exit(1)

        # if valid response, open our page with beautiful soup to parse it and find information
        soup = BeautifulSoup(response.text, 'html.parser')

        # the content we are looking for under a div tag
        # use the corresponding id to narrow down the results to the specific div tag
        for link in soup.find_all('div', id='mw-content-text'):
            print(link.getText())
