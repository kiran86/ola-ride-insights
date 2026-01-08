import pandas as pd

def cancellation_kpis(engine):
    query = """
    SELECT
        COUNT(*) AS total_rides,
        SUM(CASE WHEN booking_status <> 'Success' THEN 1 ELSE 0 END) AS cancelled_rides
    FROM rides;
    """
    return pd.read_sql(query, engine)


def cancellation_by_type(engine):
    query = """
    SELECT
        CASE
            WHEN customer_cancellation_reason IS NOT NULL THEN 'Customer'
            WHEN driver_cancellation_reason IS NOT NULL THEN 'Driver'
            ELSE 'Driver not found'
        END AS cancelled_by,
        COUNT(*) AS rides
    FROM rides
    WHERE booking_status <> 'Success'
    GROUP BY cancelled_by;
    """
    return pd.read_sql(query, engine)


def cancellation_reasons(engine, cancel_type):
    if cancel_type == "Customer":
        condition = "customer_cancellation_reason IS NOT NULL"
        column = "customer_cancellation_reason"
    else:
        condition = "driver_cancellation_reason IS NOT NULL"
        column = "driver_cancellation_reason"

    query = f"""
    SELECT
        {column} AS reason,
        COUNT(*) AS rides
    FROM rides
    WHERE {condition}
    GROUP BY reason
    ORDER BY rides DESC;
    """
    return pd.read_sql(query, engine)


def vehicle_cancellations(engine):
    query = """
    SELECT
        vehicle_type,
        COUNT(*) AS cancelled_rides
    FROM rides
    WHERE booking_status <> 'Success'
    GROUP BY vehicle_type
    ORDER BY cancelled_rides DESC;
    """
    return pd.read_sql(query, engine)
