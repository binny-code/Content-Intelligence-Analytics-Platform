import pandas as pd
from django.db import connection
from scipy import stats

def run_complex_query():
    query = """
        WITH content_stats AS (
            SELECT category,
                   COUNT(*) AS total_items
            FROM content_contentitem
            GROUP BY category
        )
        SELECT * FROM content_stats;
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=["Category", "Total"])
    return df


def regression_analysis():
    df = run_complex_query()
    df["Index"] = range(len(df))

    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df["Index"], df["Total"]
    )

    return {
        "slope": slope,
        "p_value": p_value,
        "r_squared": r_value ** 2
    }
