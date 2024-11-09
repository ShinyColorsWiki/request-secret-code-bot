import hashlib
import hmac
from config import config


def generate_secret(key: str, seed: str) -> str:
    key = key.strip()

    if not (
        len(key) == config.key_length
        and all(c in "0123456789abcdefABCDEF" for c in key)
    ):
        return (
            f"❌ Please provide a valid {config.key_length}-character hexadecimal key."
        )

    hash_bytes = hmac.new(
        config.secret_seed.encode(), key.lower().encode(), hashlib.sha256
    ).hexdigest()

    answer = hash_bytes[: config.answer_length]

    return f"Your secret key is **`{answer}`**."
