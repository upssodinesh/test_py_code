import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --- New function (recommended) ---
def get_users_v2():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }


# --- New function (recommended) ---
def get_users_v3():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "lol"}
        ]
    }


# --- Old function (to be removed in 2.0.0) ---
def get_users():
    logger.warning(
        "DEPRECATED: get_users() will be removed in version 2.0.0. "
        "Use get_users_v2() instead."
    )

    # Old response format
    return {
        "data": ["Alice", "Bob","lol"]
    }


# --- Sample usage ---
if __name__ == "__main__":
    print("Calling OLD function:")
    print(get_users())

    print("\nCalling NEW function:")
    print(get_users_v2())

    print("\nCalling NEW function:")
    print(get_users_v3())
