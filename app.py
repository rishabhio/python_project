

INTRINSIC_RATE = 10 # unit / distance 
HOUR_OF_DAY_PRICING = {
    (0 , 6 ): 1.75, 
    (6, 12): 1, 
    (12, 18): 1.5, 
    (18, 24): 1.6 
}

def apply_hour_of_day_pricing( hour_of_day, price ):
    for k, v in HOUR_OF_DAY_PRICING.items():
        if k[0] <= hour_of_day < k[1]:
            price = price * v 
            break
    return price  

def calculate_dynamic_pricing( distance, hour_of_day, partners ):
    dynamic_price = 0 
    dynamic_price = distance * INTRINSIC_RATE
    dynamic_price = apply_hour_of_day_pricing( hour_of_day, dynamic_price ) 
    return dynamic_price 


if __name__ == '__main__':

    distance = input('Please enter the distance: \n') 
    distance = float( distance ) 
    hour_of_day = input('Please enter the hour of the day: \n')
    hour_of_day = int( hour_of_day )
    price = calculate_dynamic_pricing( distance, hour_of_day, 'partners' )
    print( 'The price is: ', price )