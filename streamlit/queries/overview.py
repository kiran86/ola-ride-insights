import pandas as pd

def fetch_overview_kpis(engine):
    query = """
    SELECT
        COUNT(*) AS total_rides,
        SUM(CASE WHEN booking_status = 'Success' THEN 1 ELSE 0 END) AS completed_rides,
        SUM(CASE WHEN booking_status <> 'Success' THEN 1 ELSE 0 END) AS cancelled_rides,
        SUM(CASE WHEN booking_status = 'Success' THEN booking_value ELSE 0 END) AS revenue,
        ROUND(AVG(customer_rating), 2) AS avg_customer_rating
    FROM rides;
    """
    return pd.read_sql(query, engine)


def fetch_rides_over_time(engine):
    query = """
    SELECT
        DATE(booking_datetime) AS ride_date,
        COUNT(*) AS rides
    FROM rides
    GROUP BY ride_date
    ORDER BY ride_date;
    """
    return pd.read_sql(query, engine)


def fetch_booking_status(engine):
    query = """
    SELECT
        booking_status,
        COUNT(*) AS rides
    FROM rides
    GROUP BY booking_status;
    """
    return pd.read_sql(query, engine)