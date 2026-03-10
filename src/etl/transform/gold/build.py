import pandas as pd

#########################################################################################

def build_dim_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creation of the Gold Customer table
    
    :param df: DataFrame
    """
    
    dim_customer = df[[
        'customer_id',
        'customer_fname',
        'customer_lname',
        'customer_country',
        'customer_state',
        'customer_city',
        'customer_street',
        'customer_zipcode',
        'longitude',
        'latitude',
        'customer_segment'
    ]]\
    .drop_duplicates()\
    .reset_index(drop=True)\
    .rename(columns={
        'customer_fname': 'first_name',
        'customer_lname': 'last_name',
        'customer_state': 'state_name'
    })\
    .copy()
    
    dim_customer.columns = [col.replace('customer_id', '') if col != 'customer_id' else col for col in dim_customer.columns]
    
    return dim_customer

#########################################################################################

def build_dim_product(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creation of the Gold Product table
    
    :param df: DataFrame
    """
    
    dim_product = df[[
        'product_card_id',
        'product_name',
        'product_price',
        'category_name',
        'department_name'
    ]]\
    .drop_duplicates()\
    .reset_index(drop=True)\
    .rename(columns={
        'product_card_id' : 'product_id',
        'product_price': 'unit_price',
        'category_name': 'category',
        'department_name': 'department'
    })\
    .copy()
    
    return dim_product

#########################################################################################

def build_dim_location(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creation of the Gold Location table
    
    :param df: DataFrame
    """
    
    dim_location = df[[
        'market',
        'order_country',
        'order_region',
        'order_state',
        'order_city',
        'order_zipcode'
    ]]\
    .drop_duplicates()\
    .reset_index(drop=True)\
    .rename(columns={
       'order_state': 'state_name' 
    })\
    .copy()
    
    dim_location.columns = dim_location.columns.str.replace('order_', '')
    dim_location.insert(0, 'location_id', dim_location.index + 1)
    
    return dim_location
    

#########################################################################################

def build_dim_calendar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creation of the Gold Calendar table
    
    :param df: DataFrame
    """
    
    dates = df['order_date_dateorders']
    
    min_year = dates.dt.year.min()
    max_year = dates.dt.year.max()
    
    start_date = f'{min_year}-01-01'
    end_date = f'{max_year}-12-31'

    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    dim_calendar = pd.DataFrame({'full_date': date_range})
    
    dim_calendar['date_sk'] = dim_calendar['full_date'].dt.strftime('%Y%m%d').astype('int')
    dim_calendar['year_num'] = dim_calendar['full_date'].dt.year
    dim_calendar['quarter_num'] = dim_calendar['full_date'].dt.quarter
    dim_calendar['month_num'] = dim_calendar['full_date'].dt.month
    dim_calendar['weeknum_num'] = dim_calendar['full_date'].dt.isocalendar().week.astype('int')
    dim_calendar['weekday_num'] = dim_calendar['full_date'].dt.dayofweek + 1
    dim_calendar['day_num'] = dim_calendar['full_date'].dt.day
    
    dim_calendar['quarter_name'] = 'Q' + dim_calendar['full_date'].dt.quarter.astype('str')
    dim_calendar['month_name'] = dim_calendar['full_date'].dt.strftime('%B')
    dim_calendar['short_month'] = dim_calendar['full_date'].dt.strftime('%b')
    dim_calendar['day_name'] = dim_calendar['full_date'].dt.strftime('%A')
    dim_calendar['short_day'] = dim_calendar['full_date'].dt.strftime('%a')
    
    dim_calendar['full_date'] = dim_calendar['full_date'].dt.date
    
    return dim_calendar
    
#########################################################################################

def build_fact_sales(df: pd.DataFrame, dim_location: pd.DataFrame) -> pd.DataFrame:
    """
    Creation of the Gold Sales table
    
    :param df: DataFrame
    :param dim_location: Location DataFrame for obtaining location
    """
    
    fact_sales = df[[
        'order_id',
        'order_item_id',
        'order_item_cardprod_id',
        'order_item_quantity',
        'order_item_product_price',
        'order_item_discount',
        'sales',
        'order_item_total',
        'order_profit_per_order',
        'order_date_dateorders',
        'order_customer_id',
        'type',
        'order_status',
        'shipping_mode',
        'shipping_date_dateorders',
        'late_delivery_risk',
        'delivery_status',
        'days_for_shipment_scheduled',
        'days_for_shipping_real',
        
        'market',
        'order_country',
        'order_region',
        'order_state',
        'order_city',
        'order_zipcode'
    ]]\
    .drop_duplicates()\
    .reset_index(drop=True)\
    .rename(columns={
       'order_item_id': 'order_detail_id',
       'order_item_cardprod_id': 'product_id',
       'order_item_quantity': 'quantity',
       'order_item_product_price': 'unit_price',
       'order_item_discount': 'discount',
       'sales': 'gross_amount',
       'order_item_total': 'net_amount',
       'order_profit_per_order': 'profit',
       'order_date_dateorders': 'order_date',
       'order_customer_id': 'customer_id',
       'type': 'payment_type',
       'shipping_date_dateorders': 'shipping_date',
    })\
    .copy()
    
    fact_sales_col = ['market', 'order_country', 'order_region', 'order_state', 'order_city', 'order_zipcode']
    dim_loc_col = ['market', 'country', 'region', 'state', 'city', 'zipcode']
    
    fact_sales = fact_sales.merge(
        dim_location,
        left_on=fact_sales_col,
        right_on=dim_loc_col,
        how='left'
    )
    
    fact_sales['order_date'] = pd.to_datetime(fact_sales['order_date']).dt.date
    fact_sales['shipping_date'] = pd.to_datetime(fact_sales['shipping_date']).dt.date
    
    final_cols = ['order_id', 'order_detail_id', 'product_id', 'quantity', 'unit_price', 'discount', 'gross_amount', 'net_amount', 'profit',
                  'order_date', 'customer_id', 'payment_type', 'order_status', 'location_id', 'shipping_mode', 'shipping_date', 'late_delivery_risk',
                  'delivery_status', 'days_for_shipment_scheduled', 'days_for_shipping_real']
    
    return fact_sales[final_cols]
    

#########################################################################################

def build_gold_layer(df: pd.DataFrame) -> dict:
    """
    Creation of all Gold-layer tables
    
    :param df: DataFrame
    """
    
    dim_customer = build_dim_customer(df)
    dim_product = build_dim_product(df)
    dim_location = build_dim_location(df)
    dim_calendar = build_dim_calendar(df)
    
    fact_sales = build_fact_sales(df, dim_location)
    
    gold_tables = {
        'dim_customer': dim_customer,
        'dim_product': dim_product,
        'dim_location': dim_location,
        'dim_calendar': dim_calendar,
        'fact_sales': fact_sales
    }
    
    return gold_tables

#########################################################################################