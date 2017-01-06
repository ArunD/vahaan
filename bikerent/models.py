from django.db import models

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.IntegerField(default=0)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return str(self.id)


class BikeType(models.Model):
    bike_type_id = models.IntegerField(primary_key=True)
    vehicle_name = models.CharField(max_length=50)
    veh_desc = models.CharField(max_length=2048, blank=True)
    img_name = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'bike_type'
    
    def __str__(self):
        return str(self.vehicle_name)


class BikeDetail(models.Model):
    bike_id = models.IntegerField(primary_key=True)
    #bike_type_id = models.IntegerField()
    bike_type = models.ForeignKey(BikeType,blank = False,null = False)
    vehicle_number = models.CharField(unique=True, max_length=20)
    year_of_reg = models.IntegerField()
    passing = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    image = models.CharField(max_length=100,null=True)
    daily_rate = models.IntegerField()
    isactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bikerent_bikedetail'

    def __str__(self):
        return str(self.bike_type) +' ' +   str(self.vehicle_number)

     

   
class VisitCount(models.Model):
    count_id = models.IntegerField(primary_key=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'visit_count'
    


class TransactionDetail(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    bike_id = models.IntegerField()
    customer_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    tariff = models.DecimalField(max_digits=11, decimal_places=2)
    transaction_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transaction_detail'
        





class ContactUs(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'contact_us'


class TariffOneDay(models.Model):
    bike_type_id = models.IntegerField(db_column='Bike_Type_ID', primary_key=True)  # Field name made lowercase.
    tariff_one_day = models.IntegerField(db_column='Tariff_One_Day', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tariff_one_day'


class TariffDiscount(models.Model):
    no_of_days = models.IntegerField(db_column='No_of_Days',primary_key=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tariff_discount'
