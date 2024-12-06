# Adaptive Zero-Knowledge Proof Bridge Simulation

## Overview
This project demonstrates an **Adaptive Zero-Knowledge Proof (ZKP) Bridge** concept, which optimizes cross-chain transaction verification by dynamically categorizing transactions into different risk levels and selecting the most efficient proof mechanism. The simulation uses synthetic transaction data to showcase the system's ability to balance computational efficiency and security.

---

## Features
1. **Synthetic Transaction Generation**:
   - Transactions are generated with attributes like size, value, participants, and asset type, favoring realistic distributions.
   
2. **Risk Classification**:
   - A rule-based classifier determines the risk level (`low-risk`, `medium-risk`, or `high-risk`) based on transaction attributes.

3. **Proof Mechanism Selection**:
   - Dynamically selects one of three ZKP mechanisms:
     - **Lightweight ZKP** for low-risk transactions.
     - **Standard ZKP** for medium-risk transactions.
     - **Heavy-Duty ZKP** for high-risk transactions.

4. **Performance Simulation**:
   - Simulates proof generation times, accounting for variability in transaction attributes.

5. **Data Analysis and Visualization**:
   - Summarizes transaction classifications and proof durations.
   - Generates visualizations for better insights.

---

## Requirements
- Python 3.8+
- Libraries:
  - `random`
  - `time`
  - `pandas`
  - `matplotlib`

Install required libraries using:
```bash
pip install pandas matplotlib
```

---

## How to Use
1. **Run the Script**:
   - Execute `main()` to generate, classify, and analyze 200 synthetic transactions:
     ```bash
     python <script_name>.py
     ```
   - Modify `num_transactions` in `main()` to adjust the number of transactions.

2. **Inspect Outputs**:
   - **Transaction Data**: The first few rows of the classified dataset are printed for inspection.
   - **Analysis Summary**: Includes:
     - Risk level distribution.
     - Average proof duration per scheme.
     - Total proof generation time by risk level.
   - **Visualizations**:
     - Bar charts for each of the above metrics.

---

## Key Functions
### **Transaction Simulation**
- `generate_transaction()`:
  - Generates synthetic transactions with attributes like size, value, participants, and asset type.
  
### **Risk Classification**
- `classify_transaction(transaction)`:
  - Classifies transactions into `low-risk`, `medium-risk`, or `high-risk` categories.

### **Proof Generation**
- `select_proof_scheme(risk_level, transaction)`:
  - Dynamically selects and executes a proof scheme based on transaction risk level:
    - `lightweight_zkp_simulation`
    - `standard_zkp_simulation`
    - `heavy_duty_zkp_simulation`

### **Data Analysis**
- `analyze_data(df)`:
  - Summarizes and visualizes:
    - Risk level distribution.
    - Proof duration statistics.
    - Total proof time by risk level.

---

## Example Outputs
1. **Sample Transaction Data**:
   ```
       size   value  participants    asset_type    risk_level        proof_scheme    proof_duration
    0   620  2000.5            3    stablecoin    low-risk     lightweight_zkp    0.0512
   ```

2. **Risk Level Distribution**:
   ```
   low-risk       120
   medium-risk     50
   high-risk       30
   ```

3. **Visualizations**:
   - Risk Level Distribution
   - Average Proof Duration
   - Total Proof Time by Risk Level

---

## Customization
- Modify transaction generation probabilities and weights in `generate_transaction()`.
- Adjust classification thresholds in `classify_transaction()`.
- Update proof duration factors in `variable_proof_duration()`.

---

## Contribution
Feel free to contribute by:
- Improving transaction classification with machine learning models.
- Extending the range of proof mechanisms.
- Testing with real blockchain datasets.
