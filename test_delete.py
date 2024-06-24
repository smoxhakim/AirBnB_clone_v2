    def all(self, cls=None):
        """query on the current database session"""
        obj_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                obj_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                obj_list.extend(self.__session.query(subclass).all())

        obj_dict = dict()
        for obj in obj_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj.to_dict()
        return obj_dict
