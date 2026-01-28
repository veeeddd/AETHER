import flwr as fl

# AETHER AI Architect - Federated Server Logic
# This script initializes the central aggregation point for the VLM updates.

def main():
    print("--- AETHER: Starting Federated Server Handshake ---")
    
    # Define a simple strategy for model aggregation
    # FedAvg (Federated Averaging) is the industry standard for decentralized AI
    strategy = fl.server.strategy.FedAvg(
        min_fit_clients=2,       # Minimum hospitals required to start training
        min_available_clients=2, # Wait for at least 2 clients before starting
    )

    # Start the server to listen for "Hospital" clients
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(num_rounds=3), # We'll start with 3 training rounds
        strategy=strategy,
    )

if __name__ == "__main__":
    main()