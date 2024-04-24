

INTRINSIC_RATE = 10 # unit / distance 

def calculate_dynamic_pricing( distance, time_of_day, partners ):
    dynamic_price = 0 
    dynamic_price = distance * INTRINSIC_RATE
    return dynamic_price 


if __name__ == '__main__':
    distance = 10 
    dp = calculate_dynamic_pricing( distance, 'mornig' , '') 
    print( dp ) 
