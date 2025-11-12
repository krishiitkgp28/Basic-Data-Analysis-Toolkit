import logging
import sys
import os

# Add project root to the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.data_fetcher import DataFetcher
from src.metrics_calculator import MetricsCalculator
from src.visualizer import Visualizer

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_pipeline():
    logging.info("🚀 Starting Financial Data Pipeline")

    config_path = os.path.join(PROJECT_ROOT, "config.yaml")

    # Step 1: Fetch Data
    fetcher = DataFetcher(config_path)
    prices = fetcher.get_data()

    # Step 2: Compute Metrics
    metrics = MetricsCalculator(prices)
    log_ret = metrics.log_returns()
    simple_ret = metrics.simple_returns()
    vol = metrics.annualized_volatility(log_ret)
    logging.info("✅ Computed annualized volatility:\n%s", vol)

    # Step 3: Visualize
    output_dir = os.path.join(PROJECT_ROOT, "reports", "figures")
    viz = Visualizer(prices, log_ret, output_dir=output_dir)
    viz.plot_prices()
    viz.plot_log_returns()
    viz.plot_correlation_heatmap()

    logging.info("🎯 Pipeline execution complete")

if __name__ == "__main__":
    run_pipeline()
