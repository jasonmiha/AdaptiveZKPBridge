import random

# Function to simulate a synthetic transaction
def generate_transaction():
    return {
        'size': random.randint(1, 1000),  # Transaction size in tokens
        'value': random.uniform(10, 100000),  # Transaction value in USD
        'participants': random.randint(1, 10),  # Number of participants
        'asset_type': random.choice(['stablecoin', 'volatile_token', 'NFT'])  # Type of asset
    }

# Simple rule-based classifier
def classify_transaction(transaction):
    size = transaction['size']
    value = transaction['value']
    participants = transaction['participants']
    asset_type = transaction['asset_type']

    # Rule-based classification based on transaction attributes
    if size <= 100 and value <= 1000 and participants <= 2 and asset_type == 'stablecoin':
        return 'low-risk'
    elif size <= 500 and value <= 10000 and participants <= 5:
        return 'medium-risk'
    else:
        return 'high-risk'

# Generate a sample dataset of synthetic transactions
def generate_dataset(num_transactions=100):
    transactions = [generate_transaction() for _ in range(num_transactions)]
    return transactions

# Apply classifier to each transaction and print results
def classify_dataset(transactions):
    classified_transactions = []
    for transaction in transactions:
        risk_level = classify_transaction(transaction)
        classified_transactions.append({
            **transaction,
            'risk_level': risk_level
        })
    return classified_transactions

# Main function to generate and classify transactions
def main():
    # Generate synthetic transactions
    transactions = generate_dataset(num_transactions=100)

    # Classify transactions and print results
    classified_transactions = classify_dataset(transactions)
    for i, txn in enumerate(classified_transactions):
        print(f"Transaction {i+1}: {txn}")

if __name__ == "__main__":
    main()
