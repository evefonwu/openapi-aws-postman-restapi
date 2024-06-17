import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Inventory")

INVENTORY_DATA = [
    {
        "productId": "tshirt001",
        "location": "Warehouse A",
        "quantity": 100,
        "description": "T-shirt A",
    },
    {
        "productId": "tshirt002",
        "location": "Warehouse A",
        "quantity": 100,
        "description": "T-shirt B",
    },
    {
        "productId": "tshirt003",
        "location": "Warehouse A",
        "quantity": 100,
        "description": "T-shirt C",
    },
]


def lambda_handler(event, context):
    """Populate initial DynamoDB table for inventory stock"""
    for item in INVENTORY_DATA:
        table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps("Initial database populated successfully."),
    }
