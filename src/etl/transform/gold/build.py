import pandas as pd
import numpy as np

#########################################################################################

def build_category(df):
    """
    Docstring for build_category
    
    :param df: Description
    """
    
    category = df[[
        'category_id',
        'category_name'
    ]].drop_duplicates().copy()
    
    return category

#########################################################################################

def build_department(df):
    """
    Docstring for build_department
    
    :param df: Description
    """
    
    department = df[[
        'department_id',
        'department_name'
    ]].drop_duplicates().copy()
    
    return department

#########################################################################################

def build_product(df):
    """
    Docstring for build_product
    
    :param df: Description
    """
    
    product = df[[
        'product_card_id',
        'product_name',
        'product_price',
        'category_id',
        'department_id'
    ]]\
    .drop_duplicates()\
    .rename(columns={
        'product_card_id': 'product_id'
    })\
    .copy()
    
    return product

#########################################################################################

def build_segment(df):
    """
    Docstring for build_segment
    
    :param df: Description
    """
    
    segment = df[[
        'customer_segment'
    ]]\
    .drop_duplicates()\
    .reset_index(drop=True)\
    .rename(columns={
        'customer_segment': 'segment'
    })\
    .copy()
    
    segment['segment_id'] = segment.index + 1
    
    return segment

#########################################################################################

def build_customer(df, segment):
    """
    Docstring for build_customer
    
    :param df: Description
    :param segment: Description
    """
    
    customer = df[[
        'customer_id',
        'customer_fname',
        'customer_lname',
        'customer_segment',
        'customer_city',
        'customer_state',
        'customer_country',
        'customer_zipcode'
    ]]\
    .drop_duplicates()\
    .copy()
    
    customer = customer.merge(segment, on='segment', how='left')
    
    customer = customer.drop(columns=['customer_segment'])
    
    return customer

#########################################################################################