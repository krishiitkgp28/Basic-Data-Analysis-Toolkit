import yaml #To read config.yaml file
import os  #to create folders like data/raw if not present.
import logging #to print output instead of print 
from datetime import datetime #to add timestamps in the funtion  
from typing import List, Optional



import pandas as pd
import yfinance as yf


logger = logging.getLogger(__name__)


class DataFetcher:
    def __init__(self ,config_path: str="config.yaml"):
        with open(config_path,"r") as f:
            self.config=yaml.safe_load(f)
        
        self.tickers=self.config.get("tickers",[])
        self.start=self.config.get("start_date")
        self.end=self.config.get("end_date")

        self.raw_dir = self.config.get("data_dir", "data/raw")
        os.makedirs(self.raw_dir,exist_ok=True)

    def get_data(self, tickers: Optional[List[str]] = None) -> pd.DataFrame:
        tickers=tickers or self.tickers
        if not tickers:
            raise ValueError("No tickers provided in config or arguments.")
        
        logger.info(f"Fetching {tickers} from {self.start} to {self.end}")

        raw=yf.download(tickers, start=self.start,end=self.end,progress=False,threads=True)["Close"]

        if isinstance(raw,pd.Series):
            raw=raw.to_frame(name=tickers[0])
        
        raw.index=pd.to_datetime(raw.index)

        logger.info(f"Fetched data shape: {raw.shape}")

        return raw

    def save_raw(self,df: pd.DataFrame, name:Optional[str]=None) -> str:
        name = name or f"prices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        path = os.path.join(self.raw_dir,name)
        df.to_csv(path, index=True)
        logger.info(f"Saved raw data to {path}")
        return path

    def fetch_and_save(self, tickers: Optional[List[str]] = None, name: Optional[str] = None) -> pd.DataFrame:
        df = self.get_data(tickers=tickers)
        self.save_raw(df, name)
        return df

    
