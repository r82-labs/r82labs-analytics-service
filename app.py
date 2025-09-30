import polars as pl
from r82labs_analytics import default_empty_cells
from datetime import date

if __name__ == "__main__":
    
    df = pl.DataFrame(
        {
            "a": [1, None, 3, None],
            "b": ["x", "y", None, "y"],
            "c": [True, None, False, False],
            "d": [date(2020, 1, 1), None, date(2020, 1, 3), date(2020, 1, 4)],
        }
    )
    
    df_transformed = default_empty_cells(df)

    print(df_transformed)