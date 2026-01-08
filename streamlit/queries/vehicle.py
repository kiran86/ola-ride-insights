import pandas as pd

def vehicle_kpis(engine):
    query = """
    SELECT
        vehicle_type,
        COUNT(*) AS total_rides,
        SUM(CASE WHEN booking_status = 'Success' THEN booking_value ELSE 0 END) AS revenue,
        ROUND(AVG(ride_distance_km), 2) AS avg_distance,
        ROUND(AVG(customer_rating), 2) AS avg_rating
    FROM rides
    GROUP BY vehicle_type
    ORDER BY revenue DESC;
    """
    return pd.read_sql(query, engine)