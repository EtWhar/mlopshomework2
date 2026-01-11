#!/bin/bash
set -e

echo "Starting Smoke Test..."

# Check health endpoint
HEALTH_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/health)
if [ "$HEALTH_STATUS" -eq 200 ]; then
    echo "Health check passed!"
else
    echo "Health check failed with status $HEALTH_STATUS"
    exit 1
fi

# Check prediction endpoint
PREDICT_RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d '{"feature": "smoke_test"}' http://localhost:5000/predict)
if echo "$PREDICT_RESPONSE" | grep -q "prediction"; then
    echo "Prediction test passed!"
else
    echo "Prediction test failed: $PREDICT_RESPONSE"
    exit 1
fi

echo "Smoke Test Completed Successfully!"
