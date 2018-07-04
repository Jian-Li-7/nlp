import spacy
from spacy import displacy

class ServerOptions:
    """
    The options to nlp server, it holds control parameters to start the server.
    """
    CGI_MODEL_NAME = 'm'

    def __init__(self):
        self.model_name = 'en'
        pass

    @staticmethod
    def FromUrlParams(url):
        assert isinstance(url, str)

    @staticmethod
    def ToUrlParams():
        pass

class Server:
    """
    The nlp server.
    """
    def __init__(self, options):
        assert isinstance(options, ServerOptions)
        self.nlp = spacy.load(options.model_name)
        pass

    def