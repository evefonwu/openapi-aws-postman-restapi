# SeedInventoryFn,RestockFn

The fn event input object can be empty object because the function does not require any input values.

This is the event object for testing:

```json
{}
```

# GetInventoryFn

```py
def lambda_handler(event, context):
    try:
        # Extract the productId from query parameters
        product_id = event['queryStringParameters'].get('productId')
```

The fn event input object is expected to have a queryStringParameters key, which itself is an object to query for the productId.

This is the event object for testing:

```json
{
  "resource": "/{proxy+}",
  "path": "/inventory",
  "httpMethod": "GET",
  "headers": {
    "Accept": "application/json",
    "Content-Type": "application/json"
  },
  "queryStringParameters": {
    "productId": "tshirt001"
  }
}
```

# ReserveInventoryFn

```py
def lambda_handler(event, context):
    try:
        # Parse the input
        body = json.loads(event['body'])
        product_id = body.get('productId')
        quantity_to_reserve = body.get('quantity')
```

The fn event input object should contain a body key, which is a stringified JSON object - should include the productId and quantity fields.

This is the event object for testing:

```json
{
  "body": "{\"productId\": \"tshirt001\", \"quantity\": 10}",
  "resource": "/{proxy+}",
  "path": "/inventory/reserve",
  "httpMethod": "POST",
  "headers": {
    "Accept": "application/json",
    "Content-Type": "application/json"
  },
  "queryStringParameters": null
}
```
