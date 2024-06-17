import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Inventory")


PRODUCT_IDS_TO_RESTOCK = ["tshirt001", "tshirt002", "tshirt003"]
FULL_STOCK_QUANTITY = 100


def lambda_handler(event, context):
    """Function to restock initial products"""
    try:
        # Iterate through the list of product IDs and update their quantity
        for product_id in PRODUCT_IDS_TO_RESTOCK:
            table.update_item(
                Key={"productId": product_id},
                UpdateExpression="SET quantity = :new_quantity",
                ExpressionAttributeValues={":new_quantity": FULL_STOCK_QUANTITY},
            )

        return {"statusCode": 200, "body": json.dumps({"success": True})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
