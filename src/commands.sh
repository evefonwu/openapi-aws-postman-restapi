# commands 

# Example deployed API endpoint:
# https://16d7x3ric9.execute-api.us-east-1.amazonaws.com/dev

# GET /inventory:
curl -X GET "https://16d7x3ric9.execute-api.us-east-1.amazonaws.com/dev/inventory?productId=tshirt001"

# POST /inventory/reserve:
curl -X POST "https://16d7x3ric9.execute-api.us-east-1.amazonaws.com/dev/inventory/reserve" \
-H "Content-Type: application/json" \
-d '{"productId": "tshirt001", "quantity": 10}'

# POST /inventory/restock:
curl -X POST "https://16d7x3ric9.execute-api.us-east-1.amazonaws.com/dev/inventory/restock" \
-H "Content-Type: application/json"
