import pandas as pd

def rating_kpis(engine):
    query = """
    SELECT
        ROUND(AVG(customer_rating), 2) AS avg_customer_rating,
        ROUND(AVG(driver_rating), 2) AS avg_driver_rating
    FROM rides
    WHERE customer_rating IS NOT NULL
      AND driver_rating IS NOT NULL;
    """
    return pd.read_sql(query, engine)


def rating_distribution(engine):
    query = """
    SELECT customer_rating, driver_rating
    FROM rides
    WHERE customer_rating IS NOT NULL
      AND driver_rating IS NOT NULL;
    """
    return pd.read_sql(query, engine)


def ratings_by_vehicle(engine):
    query = """
    SELECT
        vehicle_type,
        ROUND(AVG(customer_rating), 2) AS avg_customer_rating,
        ROUND(AVG(driver_rating), 2) AS avg_driver_rating
    FROM rides
    GROUP BY vehicle_type;
    """
    return pd.read_sql(query, engine)
