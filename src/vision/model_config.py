# AETHER AI Architect - Vision-Language Model Configuration
# This file defines the 'Brain' parameters for medical image analysis.

VLM_CONFIG = {
    "model_name": "moondream2",  # A tiny but powerful VLM perfect for our initial tests
    "revision": "2024-05-20",
    "device": "auto",            # Automatically uses GPU if available
    "trust_remote_code": True,
}

# Image processing parameters for X-rays
IMAGE_PARAMS = {
    "resize": (384, 384),
    "normalize": True
}

def get_model_info():
    return f"AETHER Brain initialized with: {VLM_CONFIG['model_name']}"

if __name__ == "__main__":
    print(get_model_info())