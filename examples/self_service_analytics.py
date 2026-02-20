"""Example: Self-service analytics."""
from src.query.nl_to_sql import NLToSQL

def main():
    engine = NLToSQL("postgresql://localhost/analytics")
    results = engine.query("Show me sales by region")
    print(f"Found {len(results)} records")

if __name__ == "__main__":
    main()
