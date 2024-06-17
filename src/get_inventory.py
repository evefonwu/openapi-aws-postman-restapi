import json
import boto3

from decimal import Decimal


def convert_decimal_to_python(obj):
    """
    DynamoDB returns numeric values as Decimal objects.
    Converts Decimal to int if the value is an integer, otherwise to float.
    """
    if isinstance(obj, list):
        return [convert_decimal_to_python(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimal_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    else:
        return obj


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Inventory")


def lambda_handler(event, context):
    """Function to get an inventory item"""
    try:
        # Extract the productId from query parameters
        product_id = event["queryStringParameters"].get("productId")

        if not product_id:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing productId"}),
            }

        # Get the item from DynamoDB
        response = table.get_item(Key={"productId": product_id})

        if "Item" not in response:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Product not found"}),
            }

        item = response["Item"]
        product_details = convert_decimal_to_python(item)
        return {"statusCode": 200, "body": json.dumps(product_details)}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
