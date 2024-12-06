import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Function to simulate a synthetic transaction
def generate_transaction():
    return {
        'size': random.choices(
            population=[random.randint(1, 400), random.randint(401, 700), random.randint(701, 1000)],
            weights=[0.5, 0.4, 0.1]  # Favor smaller sizes
        )[0],
        'value': random.choices(
            population=[random.uniform(10, 5000), random.uniform(5001, 20000), random.uniform(20001, 50000)],
            weights=[0.5, 0.4, 0.1]  # Favor lower values
        )[0],
        'participants': random.choices(
            population=[random.randint(1, 2), random.randint(3, 4), random.randint(5, 7)],
            weights=[0.5, 0.3, 0.2]  # Favor fewer participants
        )[0],
        'asset_type': random.choices(
            population=['stablecoin', 'volatile_token', 'NFT'],
            weights=[0.6, 0.3, 0.1]  # Favor stablecoins
        )[0]
    }

# Simple rule-based classifier for transaction risk level
def classify_transaction(transaction):
    size = transaction['size']
    value = transaction['value']
    participants = transaction['participants']
    asset_type = transaction['asset_type']

    # Extremely loose thresholds for low-risk transactions
    if size <= 900 and value <= 40000 and participants <= 6 and asset_type == 'stablecoin':
        return 'low-risk'
    elif size <= 950 and value <= 45000 and participants <= 7:
        return 'medium-risk'
    else:
        return 'high-risk'


# Function to calculate variable proof duration based on transaction attributes
def variable_proof_duration(base_time, transaction):
    size_factor = 0.00001 * transaction['size']  # Adjust factor as needed
    value_factor = 0.0000001 * transaction['value']  # Adjust factor as needed
    variability = random.uniform(-0.01, 0.01)  # Small random variation
    return base_time + size_factor + value_factor + variability

# Simulated ZKP functions with attribute-based variability
def lightweight_zkp_simulation(transaction):
    start = time.time()
    time.sleep(variable_proof_duration(0.05, transaction))
    end = time.time()
    return {"proof": "lightweight_zkp_proof", "duration": end - start}

def standard_zkp_simulation(transaction):
    start = time.time()
    time.sleep(variable_proof_duration(0.1, transaction))
    end = time.time()
    return {"proof": "standard_zkp_proof", "duration": end - start}

def heavy_duty_zkp_simulation(transaction):
    start = time.time()
    # Further increase duration for high-risk proofs
    time.sleep(variable_proof_duration(0.8, transaction))  # Base time increased to 0.5 seconds
    end = time.time()
    return {"proof": "heavy_duty_zkp_proof", "duration": end - start}

# Proof scheme selection based on risk level
def select_proof_scheme(risk_level, transaction):
    if risk_level == 'low-risk':
        return lightweight_zkp_simulation(transaction)
    elif risk_level == 'medium-risk':
        return standard_zkp_simulation(transaction)
    elif risk_level == 'high-risk':
        return heavy_duty_zkp_simulation(transaction)

# Generate a sample dataset of synthetic transactions
def generate_dataset(num_transactions=100):
    transactions = [generate_transaction() for _ in range(num_transactions)]
    return transactions

# Apply classifier and proof scheme selection to each transaction
def classify_dataset(transactions):
    classified_transactions = []
    for transaction in transactions:
        risk_level = classify_transaction(transaction)
        proof_data = select_proof_scheme(risk_level, transaction)
        classified_transactions.append({
            **transaction,
            'risk_level': risk_level,
            'proof_scheme': proof_data['proof'],
            'proof_duration': proof_data['duration']
        })
    return classified_transactions

# Data analysis function to summarize and visualize the results
def analyze_data(df):
    # 1. Risk Level Distribution
    risk_distribution = df['risk_level'].value_counts()
    print("\nRisk Level Distribution:")
    print(risk_distribution)

    # 2. Average Proof Duration per Proof Scheme
    avg_proof_duration = df.groupby('proof_scheme')['proof_duration'].mean()
    print("\nAverage Proof Duration per Proof Scheme:")
    print(avg_proof_duration)

    # 3. Total Proof Generation Time by Risk Level
    total_proof_time_by_risk = df.groupby('risk_level')['proof_duration'].sum()
    print("\nTotal Proof Generation Time by Risk Level:")
    print(total_proof_time_by_risk)

    # 4. Plot Risk Level Distribution
    plt.figure(figsize=(8, 5))
    risk_distribution.plot(kind='bar', title='Risk Level Distribution', rot=45)
    plt.xlabel('Risk Level')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # 5. Plot Average Proof Duration per Scheme
    plt.figure(figsize=(8, 5))
    avg_proof_duration.plot(kind='bar', title='Average Proof Duration per Proof Scheme', rot=45)
    plt.xlabel('Proof Scheme')
    plt.ylabel('Average Duration (s)')
    plt.tight_layout()
    plt.show()

    # 6. Plot Total Proof Time by Risk Level
    plt.figure(figsize=(8, 5))
    total_proof_time_by_risk.plot(kind='bar', title='Total Proof Generation Time by Risk Level', rot=45)
    plt.xlabel('Risk Level')
    plt.ylabel('Total Duration (s)')
    plt.tight_layout()
    plt.show()

# Main function to generate, classify, and analyze transactions
def main():
    # Generate and classify synthetic transactions
    transactions = generate_dataset(num_transactions=200)  # Generate 100 for faster execution
    classified_transactions = classify_dataset(transactions)

    # Convert to DataFrame for easier analysis
    df = pd.DataFrame(classified_transactions)
    print(df.head())  # Display the first few rows for quick inspection

    # Perform data analysis
    analyze_data(df)

if __name__ == "__main__":
    main()
