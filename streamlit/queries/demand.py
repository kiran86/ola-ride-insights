import pandas as pd

def rides_by_hour(engine):
    query = """
    SELECT
        EXTRACT(HOUR FROM booking_datetime) AS hour,
        COUNT(*) AS rides
    FROM rides
    GROUP BY hour
    ORDER BY hour;
    """
    return pd.read_sql(query, engine)


def rides_by_day(engine):
    query = """
    SELECT
        TO_CHAR(booking_datetime, 'Day') AS day,
        EXTRACT(DOW FROM booking_datetime) AS dow,
        COUNT(*) AS rides
    FROM rides
    GROUP BY day, dow
    ORDER BY dow;
    """
    return pd.read_sql(query, engine)


def rides_heatmap(engine):
    query = """
    SELECT
        EXTRACT(DOW FROM booking_datetime) AS dow,
        EXTRACT(HOUR FROM booking_datetime) AS hour,
        COUNT(*) AS rides
    FROM rides
    GROUP BY dow, hour;
    """
    return pd.read_sql(query, engine)
