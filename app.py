# Flask-basierter Webhook-Simulator (ohne Web3)
# Ziel: Webhook testen ohne Smart Contract Verbindung

"""
Flask Webhook Simulator for Smart Contract Testing
Simulates contract triggers without actual Web3 integration
"""

# Standard library imports
import json
import os
import logging
from datetime import datetime
from functools import wraps
from time import time
from collections import defaultdict

# Third-party imports
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional, Dict, Any

# Create Flask app instance
app = Flask(__name__)

# Constants
VALID_TRIGGER_TYPE = "follower_target_reached"
DEFAULT_RATE_LIMIT = 10
DEFAULT_RATE_WINDOW = 60  # seconds

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Config:
    """Configuration management for the application"""
    LOG_FILE = "contract_trigger_log.json"
    PORT = 5000
    DEBUG = True
    RATE_LIMIT = DEFAULT_RATE_LIMIT
    RATE_WINDOW = DEFAULT_RATE_WINDOW
    
    @classmethod
    def load_env(cls) -> None:
        """Load and validate environment variables"""
        load_dotenv()
        required_vars = ["OPENAI_API_KEY", "WEB3_PROVIDER", "CONTRACT_ADDRESS"]
        
        # Validate required environment variables
        missing = [var for var in required_vars if not os.getenv(var)]
        if missing:
            raise ValueError(f"Missing environment variables: {', '.join(missing)}")
        
        # Load environment variables
        cls.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        cls.WEB3_PROVIDER = os.getenv("WEB3_PROVIDER")
        cls.CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
        
        logger.info("Environment variables loaded successfully")

# Rate Limiting Decorator
from flask import request, jsonify

def rate_limit(limit=10, window=60):  # 10 requests per minute
    requests = defaultdict(list)
    
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            now = time()
            requests[request.remote_addr] = [t for t in requests[request.remote_addr] 
                                          if now - t < window]
            
            if len(requests[request.remote_addr]) >= limit:
                return jsonify({"error": "rate limit exceeded"}), 429
                 
            requests[request.remote_addr].append(now)
            return f(*args, **kwargs)
        return wrapped
    return decorator

@app.route("/api/trigger-contract", methods=["POST"])
@rate_limit()
def trigger_contract():
    data = request.get_json()
    trigger_request = TriggerRequest.from_request(data)
    
    if not trigger_request or not trigger_request.is_valid():
        logger.warning(f"Invalid trigger request: {data}")
        return jsonify({"error": "invalid trigger"}), 400

    try:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "Contract trigger simulated",
            "payload": data
        }
        with open(Config.LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        logger.info(f"Contract trigger simulated: {log_entry}")
        return jsonify({
            "status": "simulated success", 
            "info": "Smart contract logic not executed in local mode."
        })

    except Exception as e:
        logger.error(f"Error simulating contract trigger: {e}")
        return jsonify({"error": str(e)}), 500

@dataclass
class TriggerRequest:
    """Validates and processes incoming trigger requests"""
    trigger: str
    payload: Dict[str, Any]

    @classmethod
    def from_request(cls, data: Optional[Dict]) -> Optional['TriggerRequest']:
        """Create a TriggerRequest instance from request data"""
        if not data:
            logger.error("Empty request data")
            return None
        if not isinstance(data.get('trigger'), str):
            logger.error(f"Invalid trigger format: {data.get('trigger')}")
            return None
        return cls(trigger=data['trigger'], payload=data)
        
    def is_valid(self) -> bool:
        """Validate the trigger type"""
        valid = self.trigger == VALID_TRIGGER_TYPE
        if not valid:
            logger.warning(f"Invalid trigger type: {self.trigger}")
        return valid

def rate_limit(limit: int = DEFAULT_RATE_LIMIT, window: int = DEFAULT_RATE_WINDOW):
    """
    Rate limiting decorator
    Args:
        limit: Maximum number of requests
        window: Time window in seconds
    """
    requests = defaultdict(list)
    
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            now = time()
            client_ip = request.remote_addr
            
            # Clean old requests
            requests[client_ip] = [
                t for t in requests[client_ip] 
                if now - t < window
            ]
            
            # Check rate limit
            if len(requests[client_ip]) >= limit:
                logger.warning(f"Rate limit exceeded for IP: {client_ip}")
                return jsonify({
                    "error": "rate limit exceeded",
                    "retry_after": int(window - (now - requests[client_ip][0]))
                }), 429
                 
            requests[client_ip].append(now)
            return f(*args, **kwargs)
        return wrapped
    return decorator

@app.route("/api/trigger-contract", methods=["POST"])
@rate_limit()
def trigger_contract():
    """Handle contract trigger requests"""
    try:
        data = request.get_json()
        trigger_request = TriggerRequest.from_request(data)
        
        if not trigger_request or not trigger_request.is_valid():
            return jsonify({"error": "invalid trigger"}), 400

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "Contract trigger simulated",
            "payload": data
        }
        
        # Log to file
        try:
            with open(Config.LOG_FILE, "a") as f:
                json.dump(log_entry, f)
                f.write("\n")
        except IOError as e:
            logger.error(f"Failed to write to log file: {e}")
            
        logger.info(f"Contract trigger simulated: {log_entry}")
        return jsonify({
            "status": "success",
            "message": "Smart contract trigger simulated",
            "timestamp": log_entry["timestamp"]
        })

    except Exception as e:
        logger.error(f"Error processing trigger: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    Config.load_env()
    app.run(port=Config.PORT, debug=Config.DEBUG)

# Hinweis: Dieser Code simuliert nur die Logik eines Webhooks
# und führt keine echten Smart Contract Transaktionen durch.