import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class MetricsCalculator:
    """
    A class to compute basic financial metrics:
    - Simple daily returns
    - Logarithmic returns
    - Annualized volatility
    """

        
    
    def __init__(self,prices:pd.DataFrame):
        self.prices=prices.copy()
        self.validate_data()

    def validate_data(self):
        if self.prices.empty:
            raise ValueError("Price data is empty. Fetch before calculating metrics.")
        
        if not self.prices.index.is_monotonic_increasing:
            self.prices = self.prices.sort_index()
        
        if (self.prices <= 0).any().any():
            raise ValueError("Price data contains non-positive values, cannot compute log returns.")
        
        logger.info("Validation complete: %s rows, %s columns", *self.prices.shape)

    def simple_returns(self) -> pd.DataFrame:
        simple_ret = self.prices.pct_change(fill_method=None).dropna()

        logger.info(f"Computed simple returns shape: {simple_ret.shape}")
        return simple_ret
    
    def log_returns(self) -> pd.DataFrame:
        log_ret = np.log(self.prices / self.prices.shift(1)).dropna() # type: ignore
        logger.info(f"Computed log returns shape: {log_ret.shape}")
        return log_ret

    def annualized_volatility(self, log_returns: pd.DataFrame) -> pd.Series:
        daily_vol = log_returns.std()
        annual_vol = daily_vol * np.sqrt(252)
        logger.info("Computed annualized volatility for %d assets", len(annual_vol))
        return annual_vol
