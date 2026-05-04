import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Appointments")


def lambda_handler(event, context):
    print("Lambda started")
    print("Event received:", json.dumps(event))

    method = event.get("requestContext", {}).get("http", {}).get("method")

    if not method:
        method = event.get("httpMethod", "POST")

    print("HTTP method:", method)

    if method == "POST":
        return create_appointment(event)
    elif method == "GET":
        return view_appointments()
    elif method == "DELETE":
        return delete_appointment(event)
    elif method == "PUT":
        return accept_appointment(event)
    elif method == "OPTIONS":
        return response(200, {"message": "CORS OK"})
    else:
        return response(400, {"message": "Invalid request method"})


def create_appointment(event):
    body = get_body(event)

    appointment_id = str(uuid.uuid4())

    item = {
        "appointmentId": appointment_id,
        "patientName": body.get("patientName", "Test Patient"),
        "doctorName": body.get("doctorName", "Dr Smith"),
        "appointmentDate": body.get("appointmentDate", "2026-04-28"),
        "appointmentTime": body.get("appointmentTime", "10:00"),
        "status": "Waiting Confirmation",
        "createdAt": datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)
    print("Appointment saved:", item)

    return response(200, {
        "message": "Appointment saved successfully",
        "appointment": item
    })


def view_appointments():
    result = table.scan()

    return response(200, {
        "appointments": result.get("Items", [])
    })


def delete_appointment(event):
    appointment_id = get_appointment_id(event)

    if not appointment_id:
        return response(400, {"message": "appointmentId is required"})

    table.delete_item(Key={"appointmentId": appointment_id})

    print("Appointment deleted:", appointment_id)

    return response(200, {
        "message": "Appointment deleted successfully",
        "appointmentId": appointment_id
    })


def accept_appointment(event):
    appointment_id = get_appointment_id(event)

    if not appointment_id:
        return response(400, {"message": "appointmentId is required"})

    table.update_item(
        Key={"appointmentId": appointment_id},
        UpdateExpression="SET #s = :status",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":status": "Accepted"}
    )

    print("Appointment confirmed:", appointment_id)

    return response(200, {
        "message": "Appointment confirmed successfully",
        "appointmentId": appointment_id,
        "status": "Accepted"
    })


def get_body(event):
    body = event.get("body")

    if body:
        return json.loads(body)

    return event


def get_appointment_id(event):
    params = event.get("queryStringParameters") or {}

    if params.get("appointmentId"):
        return params.get("appointmentId")

    body = get_body(event)

    return body.get("appointmentId")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,PUT,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body)
    }
