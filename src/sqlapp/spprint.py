import pprint

class spprint:
    """ Styled Pretty Print
    """
    def __init__(self, element=None, style=None, **kwargs):
        """ :param element: any : element to print : default:  None
            :param style: str or lst or tple : style(s) to apply
            :param kwargs: dict : pprint kwargs
        """
        # Available styles
        self.HEADER = '\033[95m'
        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        #param
        self.element = element
        self.style = style
        self.kwargs = kwargs
        #exec
        self._print(self.element, self.style, **self.kwargs)

    def _print(self, element, style, **kwargs):
        """ Private _print method.
            :param element: any : element to print : default:  None
            :param style: str or lst or tple : style(s) to apply
            :param kwargs: dict : pprint kwargs
        """
        if isinstance(style, (list, tuple)):
            styles = filter(None, map(self.__dict__.get, style))
        elif isinstance(style, str):
            styles = filter(None, [self.__dict__.get(style)])
        else:
            styles = []
        for s in styles:
            print(s)
        pprint.pprint(element, **kwargs)
        print(self.ENDC)
