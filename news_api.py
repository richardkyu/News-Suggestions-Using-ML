from newsapi import NewsApiClient

# Init
def retrieve_articles_newsapi():
    newsapi = NewsApiClient(api_key='2050df7a6a014501a04c5f42fa6eef54')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='sector OR big OR corporate OR product OR investor OR pointed OR gavekal OR sovereign OR vincent OR louis',
                                            sources='bbc-news,the-verge',
                                            language='en')

    # /v2/everything
    all_articles = newsapi.get_everything(q='reality OR long OR central OR capital OR political OR dollars OR trading OR algorithmic OR banks OR released',
                                        sources='bbc-news, the-verge, the-wall-street-journal, the-washington-post, the-hill',
                                        domains='bbc.co.uk, techcrunch.com, ft.com, economist.com, wsj.com, thewashingtonpost.com',
                                        from_param='2019-07-18',
                                        to='2019-08-12',
                                        language='en',
                                        sort_by='relevancy')

    # /v2/sources
    sources = newsapi.get_sources()


    for article in all_articles['articles']:
        print(article)
        print('\n')


retrieve_articles_newsapi()