class News:
    '''
    Class to define news 
    '''

    def __init__(self, author, title, description, urlToImage, published, content ):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.published = published
        