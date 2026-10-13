from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker, scoped_session, Query, Mapper


def _get_query_cls(mapper, session):
    if mapper:
        m = mapper
        if isinstance(m, tuple):
            m = mapper[0]
        if isinstance(m, Mapper):
            m = m.entity

        try:
            return m.__query_cls__(mapper, session)
        except AttributeError:
            pass

    return Query(mapper, session)


Session = sessionmaker(query_cls=_get_query_cls)
engine = create_engine('sqlite:///smart_warehouse.db', echo = True)
metadata = MetaData(bind= engine)
current_session = scoped_session(Session)


@as_declarative(metadata=metadata)
class Base:
    pass

#Экзмепляр - это объект кокого-то класса
# Класс некоторого объекта это шаблон по его созданию