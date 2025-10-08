# Project Car Price Analysis by Team MADKen

**Project Car Price Analysis** is a comprehensive data analysis dashboard for car price analysis, enabling users to explore, analyze, and visualize car price data interactively. The dashboard is built with Streamlit and supports CSV data input, providing an intuitive interface.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Content
* The dataset contains car listings with features such as brand, model, engine size, and price. It is sourced from Kaggle and is well within the repository's maximum size of 100Gb.

## Business Requirements
* Enable users to compare average car prices by brand.
* Allow exploration of price distributions for individual brands.
* Provide insights into how engine size affects car price.
* Support interactive data exploration for business decision-making.

## Hypothesis and how to validate?
* Hypothesis 1: Certain car brands have consistently higher average prices.
  * Validation: Visualize average price by brand using horizontal bar charts.
* Hypothesis 2: Engine size is positively correlated with car price.
  * Validation: Scatter plot and regression analysis of engine size vs. price.
* Hypothesis 3: Price distributions vary significantly between brands.
  * Validation: Display histograms for selected brands.

## Project Plan
* Data collection from Kaggle.
* Data cleaning and preprocessing in Jupyter notebooks.
* Exploratory analysis and feature engineering.
* Dashboard development in Streamlit.
* Iterative testing and refinement based on feedback.

## The rationale to map the business requirements to the Data Visualisations
* Average price by brand → Horizontal bar chart for clear comparison.
* Price distribution per brand → Histogram for selected brand.
* Engine size vs. price → Scatter plot for correlation analysis.

## Analysis techniques used
* Groupby and aggregation for summary statistics.
* Value counts and histograms for distribution analysis.
* Scatter plots and regression for correlation.
* Used generative AI tools (GitHub Copilot) for code suggestions, design thinking, and optimization.

## Ethical considerations
* The dataset does not contain personal or sensitive information.
* Bias may exist in the dataset due to market representation; addressed by transparent reporting.
* No legal or societal issues identified.

## Dashboard Design
* **Home Page:** Project overview and navigation.
* **Price vs Brand:** Horizontal bar chart of average price by brand; dropdown to select brand for histogram.
* **Price vs Engine Size:** Scatter plot and regression line.
* **Additional Pages:** Team member analysis pages.
* Data insights are communicated using clear visualizations and concise text, suitable for both technical and non-technical audiences.

## Unfixed Bugs
* No major unfixed bugs. Minor limitations include:
  * Streamlit does not support direct click events on Plotly charts.
  * Some brand names may be truncated if the chart height is not sufficiently increased.
* Feedback from peers led to improved chart sizing and widget selection.

## Development Roadmap
* Challenges included handling categorical data and ensuring consistent visualization sizing.
* Strategies: Used session state for data sharing, standardized histogram bins/range, and increased chart height.
* Next steps: Explore advanced interactivity (e.g., Dash callbacks), learn more about deployment and scaling Streamlit apps.

## Main Data Analysis Libraries
* **pandas:** Data loading, cleaning, and aggregation.
  * Example: `df = pd.read_csv('CarPrice_Working.csv')`
* **numpy:** Numerical operations.
* **plotly:** Interactive visualizations.
  * Example: `px.bar(df_byBrand, x='price', y='carBrand', orientation='h')`
* **streamlit:** Dashboard interface and widgets.

## Credits 

### Content 
- Data cleaning steps adapted from Kaggle tutorials.
- Widget usage and dashboard layout inspired by Streamlit documentation.

### Media
- CI logo from Code Institute.
- Example images from open-source image repositories.

## Acknowledgements (optional)
* Thanks to Code Institute instructors and peers for feedback and support.