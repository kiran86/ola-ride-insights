import pandas as pd

def revenue_kpis(engine):
    query = """
    SELECT
        SUM(CASE WHEN booking_status = 'Success' THEN booking_value ELSE 0 END) AS total_revenue,
        AVG(CASE WHEN booking_status = 'Success' THEN booking_value END) AS avg_booking_value
    FROM rides;
    """
    return pd.read_sql(query, engine)


def revenue_by_payment(engine):
    query = """
    SELECT
        payment_method,
        SUM(booking_value) AS revenue,
        COUNT(*) AS rides
    FROM rides
    WHERE payment_method IS NOT NULL
    GROUP BY payment_method
    ORDER BY revenue DESC;
    """
    return pd.read_sql(query, engine)


def booking_value_distribution(engine):
    query = """
    SELECT
        payment_method,
        booking_value
    FROM rides;
    """
    return pd.read_sql(query, engine)
