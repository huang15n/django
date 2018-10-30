from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from enum import Enum
from datetime import date, timedelta


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Property_Category(ChoiceEnum):
    SINGLE = 'Single House'
    ATTACHE = 'Attached House'
    MEMBER = 'memberName'
    TOWN = 'Town House'
    APARTMENT = 'Apartment'
    STORE = 'Store'
    FARM = 'Farm'
    MALL = 'Mall'
    BUILDING = 'Building'
    OTHER = 'Other'

    @classmethod
    def all(self):
        return [Property_Category.APARTMENT, Property_Category.ATTACHE, Property_Category.BUILDING,
                Property_Category.FARM, Property_Category.MALL, Property_Category.MEMBER, Property_Category.SINGLE,
                Property_Category.STORE, Property_Category.OTHER, Property_Category.TOWN]


class Property_Sector(ChoiceEnum):
    PRIVATE = 'Private'
    RESIDENTIAL = 'Residential'
    COMMERCIAL = 'Commercial'
    GOVERNMENT = 'Government'
    RURAL = 'Rural'
    OTHER = 'Other'

    @classmethod
    def all(self):
        return [Property_Sector.OTHER, Property_Sector.RESIDENTIAL, Property_Sector.COMMERCIAL,
                Property_Sector.GOVERNMENT, Property_Sector.PRIVATE, Property_Sector.RURAL]


class Property_Facing(ChoiceEnum):
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'
    OTHER = 'Other'

    @classmethod
    def all(self):
        return [Property_Facing.OTHER, Property_Facing.WEST, Property_Facing.EAST, Property_Facing.NORTH,
                Property_Facing.SOUTH]


class Country(models.Model):
    countryName = models.CharField(max_length=50)

    def __str__(self):
        return "Country Name:" + self.countryName


class Province(models.Model):
    countryName = models.CharField(max_length=50)
    provinceName = models.CharField(max_length=50)

    def __str__(self):
        return "Province Name:" + self.countryName + "\nCountry Name :" + self.provinceName


class City(models.Model):
    cityName = models.CharField(max_length=50)
    provinceName = models.CharField(max_length=50)
    countryName = models.CharField(max_length=50)

    def __str__(self):
        return "City Name:" + self.cityName + "Province Name:" + self.countryName + "\nCountry Name :" + self.provinceName


class Property(models.Model):
    propertyId = models.IntegerField(primary_key=True)
    propertyTitle = models.CharField(max_length=50)
    propertyCategory = models.CharField(max_length=30, choices=[(category.value, category.name) for category in
                                                                Property_Category.all()],
                                        default=Property_Category.APARTMENT, )
    propertySector = models.CharField(max_length=30,
                                      choices=[(sector.value, sector.name) for sector in Property_Sector.all()],
                                      default=Property_Sector.RESIDENTIAL)
    propertyFacing = models.CharField(max_length=30,
                                      choices=[(facing.value, facing.name) for facing in Property_Facing.all()],
                                      default=Property_Facing.WEST)
    propertyCountry = models.CharField(max_length=50)
    propertyProvince = models.CharField(max_length=50)
    propertyCity = models.CharField(max_length=50)
    propertyStreet = models.CharField(max_length=50)
    propertyPostalCode = models.CharField(max_length=50)
    propertyStreetNumber = models.CharField(max_length=50)
    propertyConstrunctionDate = models.DateField()
    propertyRegistrationDate = models.DateField()
    propertyNoofHalls = models.IntegerField()
    propertyNumberofRooms = models.IntegerField()
    propertyNoofBathrooms = models.IntegerField()
    propertyNoofFloor = models.IntegerField()
    propertyTotalArea = models.IntegerField()
    propertyAskingPrice = models.FloatField()
    propertySellingPrice = models.FloatField(default=99.0)


class Property_Images(models.Model):
    propertyId = models.ForeignKey(Property, related_name="images", on_delete=models.CASCADE)
    memberName = models.CharField(max_length=50)
    propertyImageID = models.IntegerField(primary_key=True, blank=True, null=False)
    propertyImageDescription = models.CharField(max_length=1000)
    propertyImages = models.ImageField(blank=True, null=False)
    def __str__(self):
        return str(self.propertyImages.url)




class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()


class Password(models.Model):
    userId = models.OneToOneField(User, related_name="password", on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    encryptedPassword = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    userAccountExpiryDate = models.DateField()
    passwordMustChanged = models.DateField()
    passwordReset= models.DateField()
    def __str__(self):
        return "User Id:" + str(self.userId) + "\n User Name :" + self.username + "\n user acccount expiratory date :" + str(self.userAccountExpiryDate)



class RoleCode(models.Model):
    name = models.CharField(max_length=50)
    roleId = models.IntegerField(primary_key=True)
    def __str__(self):
        return "Role Id:" + str(self.roleId) + "\n Role Name :" + self.name


class RolePermission(models.Model):
    roleId = models.ForeignKey(RoleCode,on_delete=models.CASCADE)
    sysFeature = models.CharField(max_length=250)

    def __str__(self):
        return "role Id:" + str(self.roleId) + "\n system feature:" + self.sysFeature


class UserRole(models.Model):
    userId = models.ForeignKey(User,related_name="role",on_delete=models.CASCADE)
    roleId = models.ForeignKey(RoleCode, on_delete=models.CASCADE, name="role")
    dateAssigned = models.DateField()

    def __str__(self):
        return "User Id:" + str(self.userId) + "\n Date Assigned :" + str(self.dateAssigned)




class PermissionType(models.Model):
    typeId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

# class PermissionType(models.Model):
#     roleId = models.ManyToManyField(RoleCode, name = "permissiontype" )
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return "code Id:" + str(self.roleId) + "\n Code Permission Name :" + self.name


