from bikerent.models import BikeDetail,AuthUser,TransactionDetail,VisitCount,TariffOneDay,TariffDiscount,ContactUs,BikeType
from django.db import connection
#from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
#from itertools import groupby
from calendar import HTMLCalendar, monthrange
from datetime import datetime
from bikerent.email_module import email_register,email_transaction,email_query
import smtplib

date_format = "%Y-%m-%d"

def bike_to_book():
    bikes = BikeType.objects.all()
    return bikes


def tariff_calc(bike_type,days):
    a = TariffOneDay.objects.get(bike_type_id = bike_type)
    daily_price = a.tariff_one_day
    b = TariffDiscount.objects.get(no_of_days = days)
    discount = b.discount
    tariff_val = (daily_price*days) - (daily_price*days*discount)/100
    discount_avail = (daily_price*days)*(discount/100)
    return float(tariff_val)
    
def valid_days_booking(start_date,end_date):
    global date_format
    a = datetime.strptime(start_date, date_format)
    b = datetime.strptime(end_date, date_format)

    if a > b :
	flag = 2	
    else:	
	    delta = b - a
	    days = int(delta.days) + 1
	    flag = 0
	    if days > 31 :
		print 'here 1'
		flag = 0
	    else:
		flag = 1
    return flag
    
def no_of_days(start_date,end_date):
    global date_format
    print 'in no of days'
    a = datetime.strptime(start_date, date_format)
    b = datetime.strptime(end_date, date_format)
    delta = b - a
    days = int(delta.days) + 1
    print delta.days # that's it
    print days
    return int(days)

    

def visit_count_func():
    a = VisitCount.objects.get(count_id=1)
    count = a.count
    count += 1
    a.count = count
    a.save()
    return count



def bike_avail_func(start_date,end_date):
    cursor = connection.cursor()
    cursor.execute("""select d.vehicle_name,if(d.bike_type_id = 1,d.avail_count,0) avail_count,d.bike_type_id,d.days,d.tariff_one_day,d.discount,(d.days*d.tariff_one_day)-(d.days*d.tariff_one_day)*(d.discount/100) tariff, d.veh_desc, d.img_name
from
(select c.vehicle_name vehicle_name,c.img_name img_name,c.veh_desc veh_desc, c.avail_count avail_count,c.bike_type_id bike_type_id,days,tod.tariff_one_day tariff_one_day,tdisc.discount discount 
from 
(select  vehicle_name, veh_desc, img_name,ifnull(total_count - used_count,0) avail_count,a.bike_type_id bike_type_id,datediff(%s,%s)+ 1  days from 
(select bt.vehicle_name,bt.bike_type_id,count(bd.bike_type_id) total_count, bt.veh_desc, bt.img_name
from vahaan.bikerent_bikedetail bd
right join vahaan.bike_type bt on bd.bike_type_id = bt.bike_type_id group by bt.bike_type_id,bt.vehicle_name) a
left join 
(
select ifnull(count(distinct td.bike_id),0) used_count,bd.bike_type_id from vahaan.bikerent_bikedetail bd
left join  
(select bike_id,start_date,end_date from vahaan.transaction_detail td 
where (%s between  td.start_date and  td.end_date) or (%s between  td.start_date and  td.end_date)) td 
on (bd.bike_id = td.bike_id)
group by bd.bike_type_id
 ) b 
on  a.bike_type_id = b.bike_type_id) c
left join vahaan.tariff_one_day tod on tod.bike_type_id = c.bike_type_id
left join vahaan.tariff_discount tdisc on tdisc.no_of_days = c.days) d;""",[end_date,start_date,start_date,end_date])
    
    keys = ['vehicle_name','avail_count','bike_type_id','no_of_days','tariff_one_day','discount','tariff','veh_desc','img_name']
    bike_available_tuple = cursor.fetchall()
    bike_available = [dict(zip(keys,row)) for row in bike_available_tuple]
    return bike_available

def avail_cal(): #working
    cur = connection.cursor()
    cur.execute("""select DATE_FORMAT(c.datefield, '%Y-%m-%d') datefield,c.bike_type_id,ifnull((c.total_count - ifnull(d.trans_count,0) ),0) avail_count from 
                (select a.datefield,a.bike_type_id,b.total_count from 
                (select distinct datefield,bike_type_id from vahaan.calendar,vahaan.bike_type) a
                left join 
                (select count(bike_id) total_count,bike_type_id from vahaan.bikerent_bikedetail group by bike_type_id )b
                on a.bike_type_id = b.bike_type_id )c 
                left join 
                (select  cal.datefield,bd.bike_type_id,count(td.bike_id) trans_count from vahaan.transaction_detail td
                right join vahaan.calendar cal ON (cal.datefield >= td.start_date) and (cal.datefield <= td.end_date)
                right join vahaan.bikerent_bikedetail bd on bd.bike_id = td.bike_id
                where td.start_date >= curdate() and td.end_date >= curdate()
                group by cal.datefield,bd.bike_type_id ) d on c.datefield = d.datefield and c.bike_type_id = d.bike_type_id ;""")
    
    avail_keys = ['datefield','bike_type_id','avail_count']
    date_avail_tuple = cur.fetchall()
    cur.close()
    date_avail = [dict(zip(avail_keys,row)) for row in date_avail_tuple]
    return date_avail

def get_bike_id(start_date,end_date,bike_type_id):
        cursor = connection.cursor()
        cursor.execute("""select bd.bike_id,bd.vehicle_number from vahaan.bikerent_bikedetail bd
                            where bd.bike_id not in (select bike_id from vahaan.transaction_detail
                            where start_date between %s and %s
                            or end_date between %s and %s) and bd.bike_type_id = %s limit 1;""",[start_date,end_date,start_date,end_date,bike_type_id])
        bike_id_tuple = cursor.fetchall()
        cursor.close()
        avail_keys = ['bike_id','vehicle_number']  
        return bike_id_tuple

def transaction_func(user_name,bike_type_id,visit_count,start_date,end_date,payment):
        print 'in trans func'
        days = no_of_days(start_date,end_date)    
        tariff = tariff_calc(bike_type_id,days) + 500
        bike_dict = get_bike_id(start_date,end_date,bike_type_id)
        bike_id = bike_dict[0][0]
        
        vehicle_no = bike_dict[0][1]
        cust_id = AuthUser.objects.get(username=user_name)
        customer = int(cust_id.id)
        email = str(cust_id.email)
        initial_data = {'start_date':start_date,'end_date':end_date,'cust_id':cust_id,'bike_id':bike_id,'username':user_name,'tariff':tariff}
        if payment == 1 : 
            t = TransactionDetail(bike_id=int(bike_id),customer_id=customer,start_date=start_date,end_date=end_date,tariff=tariff)
            t.save()
            email_transaction(user_name,email,start_date,end_date,tariff,vehicle_no)        
        return initial_data


def query_save(firstname,lastname,email,phone,message):
    t = ContactUs(first_name = firstname,last_name = lastname,email = email,phone = int(phone),message = message)
    t.save()
    email_query(firstname,lastname,email,phone,message)

def already_book(user_name,start_date,end_date):
    cust_id = AuthUser.objects.get(username=user_name)
    cursor = connection.cursor()
    cursor.execute("""select count(1) from vahaan.transaction_detail td
                    where td.customer_id = %s and    
                    ((%s between  td.start_date and  td.end_date) or (%s between  td.start_date and  td.end_date)) ;""",[cust_id,start_date,end_date])
    
    count_tuple =  cursor.fetchall()
    cursor.close()
    count = count_tuple[0][0]
    return count
    
