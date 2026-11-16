import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "system": "Natupende Computer Vision Webhook"}), 200

@app.route('/webhook/audit', methods=['POST'])
def process_audit():
    try:
        payload = request.get_json()

        if not payload or "Data" not in payload:
            return jsonify({"error": "Invalid payload format"}), 400

        audit_data = payload["Data"]
        stack_id = audit_data.get("Stack_ID")
        expected_units = audit_data.get("Expected_Units")
        photo_url = audit_data.get("Audit_Photo_URL")

        print(f"--> Processing Stack ID: {stack_id} | Expected: {expected_units}")

        # Computer Vision stub: In production, your CV model processes `photo_url` here.
        detected_units = 24  

        return jsonify({
            "status": "success",
            "Stack_ID": stack_id,
            "Detected_Units": detected_units
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

