import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)

class Visualizer:

    def __init__(self, prices: pd.DataFrame, log_returns: pd.DataFrame, output_dir: str = "reports/figures"):
       
        self.prices = prices
        self.log_returns = log_returns
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        sns.set(style="whitegrid")  # Set a clean default theme

    def plot_prices(self, title="Asset Prices Over Time"):
        
        plt.figure(figsize=(12, 6))

        for col in self.prices.columns:
            plt.plot(self.prices.index, self.prices[col], label=col)
        
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()
        
        path = os.path.join(self.output_dir, "price_trends.png")
        plt.savefig(path)
        plt.close()
        logger.info("Saved price chart to %s", path)

    def plot_log_returns(self, title="Daily Log Returns"):
        
        plt.figure(figsize=(12, 6))

        for col in self.log_returns.columns:
            plt.plot(self.log_returns.index, self.log_returns[col], label=col)

        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Log Return")
        plt.legend()
        plt.tight_layout()

        path = os.path.join(self.output_dir, "log_returns.png")
        plt.savefig(path)
        plt.close()
        logger.info("Saved log return chart to %s", path)

    def plot_correlation_heatmap(self, title="Correlation Matrix of Log Returns"):
       
        plt.figure(figsize=(8, 6))

        corr_matrix = self.log_returns.corr()

        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")

        plt.title(title)
        plt.tight_layout()

        path = os.path.join(self.output_dir, "correlation_heatmap.png")
        plt.savefig(path)
        plt.close()
        
        logger.info("Saved correlation heatmap to %s", path)
