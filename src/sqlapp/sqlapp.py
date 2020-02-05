from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class SqlApp():
    def __init__(self, db_uri=None):
        self.db_uri = db_uri
        self.Base = declarative_base()

    def connect(self, db_uri=None):
        """ Connect to database by default using self.db_uri
            :param db_uri: over ride db_uri
        """
        uri = self.db_uri or db_uri
        if uri is None:
            raise ValueError('db_uri not provided')
        self.engine = create_engine(uri, echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    @property
    def Base(self):
        return self.Base

    def populate(self, model, rows):
        self.session.add_all([model(**row) for row in rows])
        self.session.commit()

    def create(self, model):
        self.session.add(model)
        self.session.commit()

    def create_models(self):
        self.Base.metadata.create_all(self.engine)

    def drop_models(self):
        self.Base.metadata.drop_all(self.engine)
