# from colorama import Fore
from .base import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, UniqueConstraint
from datetime import datetime

# class AppleHealthKit(Base):
class AppleHealthQuantityCategory(Base):
    __tablename__ = 'apple_health_quantity_category'
    id = Column(Integer,primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sampleType = Column(String(255))
    startDate = Column(String(30))
    endDate = Column(Text)
    metadataAppleHealth = Column(Text)
    sourceName = Column(Text)
    sourceVersion = Column(Text)
    sourceProductType = Column(Text)
    device = Column(Text)
    UUID = Column(String(36))
    quantity = Column(String(50))
    value = Column(String(50))
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'AppleHealthQuantityCategory(id: {self.id}, user_id: {self.user_id},' \
            f'sampleType: {self.sampleType}, startDate: {self.startDate}, quantity: {self.quantity},' \
            f'time_stamp_utc: {self.time_stamp_utc}, UUID: {self.UUID})'
    
    # Add a UniqueConstraint to the table definition
    # __table_args__ = (
    #     UniqueConstraint('user_id', 'sampleType', 'UUID','startDate', 'quantity','value', \
    #         name='_user_sample_uuid_uc'),
    # )
    __table_args__ = (
        UniqueConstraint('user_id', 'sampleType', 'UUID','startDate',  \
            name='_user_sample_uuid_start_date'),
    )

class AppleHealthWorkout(Base):
    __tablename__ = 'apple_health_workout'
    id = Column(Integer,primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sampleType = Column(String(255))
    startDate = Column(String(30))
    endDate = Column(Text)
    duration = Column(String(30))# seconds (Polar is minutes)
    totalEnergyBurned = Column(String(30))
    totalDistance = Column(String(30))
    sourceName = Column(Text)
    sourceVersion = Column(Text)
    device = Column(Text)
    UUID = Column(String(36))
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'AppleHealthWorkout(id: {self.id}, user_id: {self.user_id},' \
            f'sampleType: {self.sampleType}, startDate: {self.startDate}, duration: {self.duration},' \
            f'time_stamp_utc: {self.time_stamp_utc}, UUID: {self.UUID})'
    
    # Add a UniqueConstraint to the table definition
    # __table_args__ = (
    #     UniqueConstraint('user_id', 'sampleType', 'UUID','duration', 'startDate',\
    #         'totalEnergyBurned','totalDistance', name='_user_sample_uuid_uc'),
    # )
    __table_args__ = (
        UniqueConstraint('user_id', 'sampleType', 'UUID', 'startDate',\
             name='_user_sample_uuid_start_date'),
    )





