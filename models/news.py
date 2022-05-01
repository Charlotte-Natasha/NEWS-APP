class News:
    '''
    Class to define news 
    '''

    def __init__(self, id, author, title, description, urlToImage, link, published, content ):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.link = link
        self.content = content
        self.published = published
        