from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .spprint import spprint

class SqlApp():
    """ SqlApp class provide helpers method to easily interact
        with sqlalchemy ORM in Jupyter Notebook.
    """
    def __init__(self, db_uri=None, echo=True):
        self.db_uri = db_uri
        self.session = None
        self.engine = None
        self._sql = None
        if db_uri:
            self.connect(db_uri=db_uri, echo=echo)

    @property
    def sql(self):
        if self._sql:
            return self._sql
        else:
            self.connect()
            return self._sql

    @property
    def Base(self):
        return declarative_base()

    def connect(self, db_uri=None, echo=True):
        """ Connect to database by default using self.db_uri
            :param db_uri: overwrite self.db_uri
            :param echo: default True, log sqlalchemy
        """
        uri = db_uri or self.db_uri
        if uri is None:
            raise ValueError('db_uri not provided')
        self.engine = create_engine(uri, echo=echo)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self._sql = sql(session=self.session)

    def populate(self, model, rows):
        """ add a list of rows in db
            :param model: SQLAlchemy Model
            :rows: list[dict]
        """
        try:
            self.session.add_all([model(**row) for row in rows])
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def create(self, model):
        """ Create a model in db
            :param model: SQLAlchemy Model
        """
        try:
            self.session.add(model)
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def delete(self, model):
        """ Delete a model in db
            :param model: SQLAlchemy Model
        """
        try:
            self.session.delete(model)
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def create_models(self, Base):
        """ create all models linked to Base
        """
        Base.metadata.create_all(self.engine)

    def drop_models(self, Base):
        """ drop all models linked to Base
        """
        Base.metadata.drop_all(self.engine)

class sql:
    """ SqlApp class provide helpers method to easily interact
        with SQL Tables in Jupyter Notebook.
    """
    def __init__(self, session):
        self.session = session

    @property
    def tables(self):
        """ List all tables in db.
        """
        return self.list_tables()


    def drop_all_tables(self, show=True):
        """ Drop all tables in db.
            :param show: boolean | Print droped tables | default : True
        """
        map(self.drop_table, self.list_tables(show=show))

    def list_tables(self, show=False):
        """ List all tables in db
            :param show: boolean | Print tables | default : False
        """
        tables = []
        try:
            rows = self.session.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """)
        except Exception as e:
            self.session.rollback()
            spprint('Failed to list tables\n{message}'.format(message=e.message), ['WARNING', 'BOLD'])

        if rows:
            tables = [ r[0] for r in rows ]
        if show:
            spprint(tables, style=['BOLD', 'BLUE'])
        return tables


    def drop_table(self, table):
        """ Drop a table in db
            :param table: str | table name
        """
        try:
            self.session.execute(
                """DROP TABLE IF EXISTS "{table}" CASCADE;""".format(
                    table=table
                )
            )
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            spprint("""
                failed to drop table : {table}
                {message}
            """.format(table=table, message=e.message), ['WARNING', 'BOLD'])
            pass
