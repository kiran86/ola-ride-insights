import pandas as pd

def total_kpis(engine):
    query = """
    SELECT
        COUNT(*) AS total_rides,
        SUM(CASE WHEN booking_status = 'Success' THEN 1 ELSE 0 END) AS successful_rides,
        SUM(CASE WHEN booking_status = 'Success' THEN booking_value ELSE 0 END) AS revenue
    FROM rides;
    """
    return pd.read_sql(query, engine)


def rides_by_vehicle(engine):
    query = """
    SELECT vehicle_type,
           COUNT(*) AS rides,
           SUM(booking_value) AS revenue
    FROM rides
    WHERE booking_status = 'Success'
    GROUP BY vehicle_type
    ORDER BY revenue DESC;
    """
    return pd.read_sql(query, engine)
