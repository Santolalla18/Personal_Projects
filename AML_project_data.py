import pandas as pd
import numpy as np

np.random.seed(42)
n_customers = 1000
customers = pd.DataFrame({"customer_id": range(n_customers), 
                          "customer_type": np.random.choice(["Retail", "SME"],n_customers, p=[0.7,0.3])
                            })
transactions = []

for customer in customers["customer_id"]:
    n_tx = np.random.randint(20,50)
    for _ in range(n_tx):
        transactions.append({
            "customer_id": customer,
            "amount": np.random.exponential(scale=2000),
            "date": pd.Timestamp("2024-01-01") + pd.Timedelta(days=np.random.randint(0, 60))
        })
transactions = pd.DataFrame(transactions)
print(transactions.head())