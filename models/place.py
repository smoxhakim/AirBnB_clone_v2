#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
        ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
        )
                    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all,delete-orphan"
            )
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            back_populates="place_amenities",
            viewonly=False
            )

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """amenities getter"""
            from models import storage
            amenities_dict = storage.all(Amenity).values()
            place_amenities_json = list()
            for amenity in amenities_dict:
                if amenity.id in self.amenity_ids:
                    place_amenities_json.append(amenity)
            return place_amenities_json

        @property
        def reviews(self):
            """returns the list of Review instances with
            place_id equals to the current Place.id"""
            from models import storage
            file_reviews = storage.all(Review).values()
            return [review for review in file_reviews
                    if review.place_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            """amenities setter"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
