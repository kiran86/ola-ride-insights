-- Table: public.rides

-- DROP TABLE IF EXISTS public.rides;

-- SQL schema for rides table
CREATE TABLE public.rides (
    booking_datetime	TIMESTAMP,
    booking_id			VARCHAR PRIMARY KEY,
	booking_status		VARCHAR,
    customer_id       	VARCHAR,
    vehicle_type      	VARCHAR,
	v_tat				NUMERIC,
	c_tat				NUMERIC,
    customer_cancellation_reason VARCHAR,
    driver_cancellation_reason   VARCHAR,
	is_incomplete_ride	BOOLEAN,
	incomplete_ride_reason	VARCHAR,
    booking_value     NUMERIC,
    payment_method    VARCHAR,
    ride_distance_km  NUMERIC,
    driver_rating     NUMERIC,
    customer_rating   NUMERIC
);
-- Set ownership to root user
ALTER TABLE IF EXISTS public.rides
    OWNER to root;
-- Copy data from CSV file into rides table
\copy public.rides(
    booking_datetime,
    booking_id,
    booking_status,
    customer_id,
    vehicle_type,
    v_tat,
    c_tat,
    customer_cancellation_reason,
    driver_cancellation_reason,
    is_incomplete_ride,
    incomplete_ride_reason,
    booking_value,
    payment_method,
    ride_distance_km,
    driver_rating,
    customer_rating
)
FROM '/home/kiran/Documents/ola-ride-insights/data/OLA_DataSet.csv'
WITH (
    FORMAT csv,
    DELIMITER ',',
    HEADER,
    ENCODING 'UTF8',
    NULL 'null'
);

-- Table: public.car_icons

-- DROP TABLE IF EXISTS public.car_icons;

-- SQL schema for car_icons table
CREATE TABLE IF NOT EXISTS public.car_icons
(
    vehicle_type text COLLATE pg_catalog."default" NOT NULL,
    icon_url text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT car_icons_pkey PRIMARY KEY (vehicle_type)
)

-- Set ownership to root user
ALTER TABLE IF EXISTS public.car_icons
    OWNER to root;