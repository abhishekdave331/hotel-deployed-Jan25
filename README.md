# Hotel Booking Cancellation Prediction

## Project Overview
INN Hotels Group faces significant revenue losses due to last-minute booking cancellations. This project aims to build a predictive model that identifies bookings likely to be canceled, enabling the hotel chain to take proactive actions to reduce financial impact and optimize booking management.

## Dataset
- **Historical Data:** Past booking records including cancellation status and booking details.
- **Future Data:** New bookings data where cancellation predictions are applied.

## Workflow

### 1. Data Overview
- Load and inspect datasets (shape, summary statistics).
- Initial understanding of cancellation distribution.

### 2. Exploratory Data Analysis (EDA)
- Visualize cancellation rates (Cancelled vs Not Cancelled).
- Analyze key categorical features such as room type, market segment, and booking channel.
- Explore numerical features including lead time and average daily rate.
- Investigate cancellation patterns across time intervals and customer types.

### 3. Data Preprocessing
- Remove redundant features (e.g., booking ID).
- Handle missing values.
- Encode categorical variables using label encoding and one-hot encoding.
- Apply PowerTransformer for skewness correction.
- Scale features to prepare data for modeling.

### 4. Model Development
- Define classification target: `booking_status`.
- Train machine learning models (logistic regression, decision trees, etc.).
- Evaluate models using accuracy, precision, recall, and other relevant metrics.
- Address class imbalance if applicable.

### 5. Predictions on New Data
- Apply the trained model on new bookings.
- Save prediction results for business use.

## Key Features Analyzed
- Lead time before booking date
- Booking channel
- Rebooking status
- Average daily rate (ADR)
- Market segment
- Customer nationality

## Tools & Technologies
- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
- Jupyter Notebook

## Future Work
- Explore advanced algorithms like ensemble methods and XGBoost.
- Incorporate time series analysis for booking trends.
- Build an interactive dashboard for real-time cancellation risk monitoring.
