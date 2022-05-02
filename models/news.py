class News:
    '''
    Class to define news 
    '''

    def __init__(self, author, title, description, urlToImage, content, publishedAt ):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt
        