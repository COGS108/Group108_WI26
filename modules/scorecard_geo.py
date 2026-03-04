import pandas as pd

def extract_geo(scorecard_csv_path: str) -> pd.DataFrame:
    """
    Extract geography identifiers from a College Scorecard MERGED file.

    Returns a deduplicated DataFrame with:
      - UNITID
      - STABBR
      - REGION
    """
    scorecard_raw = pd.read_csv(scorecard_csv_path, low_memory=False)

    geo = (
        scorecard_raw[["UNITID", "STABBR", "REGION"]]
        .dropna(subset=["UNITID"])
        .drop_duplicates(subset=["UNITID"])
        .reset_index(drop=True)
    )

    return geo