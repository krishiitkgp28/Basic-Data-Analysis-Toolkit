# 🧠 Foundational Data Acquisition and Volatility Analysis Toolkit

A standardized, reusable Python toolkit for financial data analysis.  
It provides automated data fetching, cleaning, core statistical metrics, and visualizations.

---

## 📁 Project Structure



src/
├── data_fetcher.py → Fetches and validates historical price data
├── metrics_calculator.py → Computes returns and volatility
└── visualizer.py → Plots prices, returns, and correlation heatmap

data/
├── raw/ → Stores raw data downloaded from APIs
├── processed/ → Stores cleaned data ready for analysis

notebooks/
├── 01_data_fetching.ipynb → Test and visualize raw data
├── 02_metrics_analysis.ipynb → Compute and analyze returns
└── 03_visualization.ipynb → Generate correlation plots and charts


---

## ⚙️ Configuration (`config.yaml`)

You can configure your tickers and date ranges easily:

```yaml
tickers:
  - AAPL
  - MSFT
  - SPY
  - BTC-USD
start_date: "2022-01-01"
end_date: "2025-01-01"
data_dir: "data/raw"
```

🚀 How to Run
1️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate        # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Test Pipeline
python tests/test_pipeline.py

4️⃣ (Optional) Open in Jupyter
jupyter notebook notebooks/

🧮 Features
Module	Description
DataFetcher	Downloads and validates price data
MetricsCalculator	Computes returns & annualized volatility
Visualizer	Plots prices, returns, and correlation matrix
📊 Example Output

📈 Asset price trends

🔁 Log return time series

🔥 Correlation heatmap (diversification insight)

🧑‍💻 Author

Krish Agarwal
Data Science & Quantitative Finance Enthusiast
LinkedIn
 | GitHub
