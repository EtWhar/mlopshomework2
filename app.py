import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

def hash_feature(feature_string, num_buckets=100):
    """
    Hashes a feature string into a bucket index.
    """
    if not isinstance(feature_string, str):
        raise ValueError("Input must be a string")

    hash_object = hashlib.md5(feature_string.encode())
    hash_hex = hash_object.hexdigest()
    return int(hash_hex, 16) % num_buckets

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'feature' not in data:
        return jsonify({'error': 'Missing feature in request'}), 400

    feature = data['feature']
    try:
        bucket = hash_feature(feature)
        # Mock prediction logic
        prediction = 1 if bucket % 2 == 0 else 0
        return jsonify({'feature': feature, 'bucket': bucket, 'prediction': prediction})
    except (ValueError, TypeError) as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
