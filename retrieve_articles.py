# Dependencies
import requests
import time
from pprint import pprint

def retrieve_articles(query):
        url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

        # Store a search term
        #query = "groups may white reform immigration federation american trump including nation"
        #fq = "money"

        # Search for articles published between a begin and end date
        begin_date = "20190101"
        end_date = "20190818"

        #filter
        query_url = f"{url}api-key=db1Vnm2AtlDDvNGJwu5izccRSafP0DGl&q={query}&begin_date={begin_date}&end_date={end_date}"


        # Empty list for articles
        articles_list = []
        ignore_terms =["marriage","wedding","pregnancy",'adventure']


        # loop through pages for more results.
        for page in range(0, 4):
                query_url = f"{url}api-key=db1Vnm2AtlDDvNGJwu5izccRSafP0DGl&q={query}&begin_date={begin_date}&end_date={end_date}"

    
        # create query with page number
        query_url = f"{query_url}&page={str(page)}"
        articles = requests.get(query_url).json()
        
        # Add a one second interval between queries to stay within API query limits
        time.sleep(1)
        # loop through the response and append each article to the list

        for article in articles["response"]["docs"]:
                x = f'{article["snippet"]} {article["web_url"]}'
                articles_list.append(x)
                
                #get rid of terms in articles irrelevant to what you are searching.
                for element in ignore_terms:
                        if element in x:
                                articles_list.pop()
        



        string_articles_list = ''        
        for x,y in enumerate(articles_list):
                print(f'{x+1}. {y} \n')
                string_articles_list += f'{x+1}. {y} \n'

        return string_articles_list


'''
# Retrieve articles
articles = requests.get(query_url).json()

articles_list = [article for article in articles["response"]["docs"]]

#print(articles_list)

for article in articles_list:
        print(f'{article["snippet"]} {article["web_url"]} \n')
'''
