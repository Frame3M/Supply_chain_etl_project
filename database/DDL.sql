-----------------------------------------------------------------------------------------

CREATE SCHEMA IF NOT EXISTS gold;

-----------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS gold.dim_customer(
	customer_id INT PRIMARY KEY,
	first_name VARCHAR(155),
	last_name VARCHAR(155),
	country VARCHAR(155),
	state_name VARCHAR(155),
	city VARCHAR(155),
	street VARCHAR(155),
	zipcode VARCHAR(15),
	longitude NUMERIC(9,6),
	latitude NUMERIC(9,6),
	segment VARCHAR(155)
);

CREATE TABLE IF NOT EXISTS gold.dim_product(
	product_id INT PRIMARY KEY,
	product_name VARCHAR(155),
	unit_price NUMERIC(10,2),
	category VARCHAR(155),
	department VARCHAR(155)
);

CREATE TABLE IF NOT EXISTS gold.dim_location(
	location_id INT PRIMARY KEY,
	market VARCHAR(15),
	country VARCHAR(155),
	region VARCHAR(155),
	state_name VARCHAR(155),
	city VARCHAR(155),
	zipcode VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS gold.dim_calendar(
	full_date DATE PRIMARY KEY,
	date_sk INT,
	year_num INT,
	quarter_num INT,
	month_num INT,
	weeknum_num INT,
	weekday_num INT,
	day_num INT,
	quarter_name CHAR(2),
	month_name VARCHAR(20),
	short_month VARCHAR(20),
	day_name VARCHAR(20),
	short_day VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS gold.fact_sales(
	order_id INT,
	order_detail_id INT,
	product_id INT,
	quantity INT,
	unit_price NUMERIC(10,2),
	discount NUMERIC(10,2),
	gross_amount NUMERIC(11,2),
	net_amount NUMERIC(11,2),
	profit NUMERIC(10,2),
	order_date DATE,
	customer_id INT,
	payment_type VARCHAR(155),
	order_status VARCHAR(155),
	location_id INT,
	shipping_mode VARCHAR(155),
	shipping_date DATE,
	late_delivery_risk BOOL,
	delivery_status VARCHAR(155),
	days_for_shipment_scheduled INT,
	days_for_shipping_real INT,

	CONSTRAINT PK_order_and_detail PRIMARY KEY (order_id, order_detail_id),
	CONSTRAINT FK_product_id FOREIGN KEY (product_id) REFERENCES gold.dim_product(product_id),
	CONSTRAINT FK_order_date FOREIGN KEY (order_date) REFERENCES gold.dim_calendar(full_date),
	CONSTRAINT FK_customer_id FOREIGN KEY (customer_id) REFERENCES gold.dim_customer(customer_id),
	CONSTRAINT FK_location_id FOREIGN KEY (location_id) REFERENCES gold.dim_location(location_id),
	CONSTRAINT FK_shipping_date FOREIGN KEY (shipping_date) REFERENCES gold.dim_calendar(full_date)
);

-----------------------------------------------------------------------------------------
