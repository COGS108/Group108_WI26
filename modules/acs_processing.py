import pandas as pd

STATE_MAP = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
    "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
    "New York": "NY", "North Carolina": "NC", "North Dakota": "ND",
    "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
    "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD",
    "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
    "Wisconsin": "WI", "Wyoming": "WY",
    "District of Columbia": "DC",
    "Puerto Rico": "PR",
}

def build_income_long(acs_csv_path: str) -> pd.DataFrame:
    """
    Convert ACS B19013 wide export (data.census.gov) into a long table:
      STABBR, median_household_income
    """
    acs_raw = pd.read_csv(acs_csv_path)

    estimate_cols = [c for c in acs_raw.columns if "!!Estimate" in c]
    acs_row = acs_raw.loc[0, estimate_cols]

    acs_long = acs_row.reset_index()
    acs_long.columns = ["state_full", "median_household_income"]

    acs_long["state_full"] = acs_long["state_full"].str.replace("!!Estimate", "", regex=False)

    acs_long["median_household_income"] = (
        acs_long["median_household_income"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    acs_long["STABBR"] = acs_long["state_full"].map(STATE_MAP)

    acs_clean = (
        acs_long[["STABBR", "median_household_income"]]
        .dropna()
        .reset_index(drop=True)
    )

    return acs_clean