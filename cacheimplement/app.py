class SimpleCache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        """Returns the cached value if it exists, else None."""
        return self.cache.get(key, None)

    def set(self, key, value):
        """Sets the value in the cache."""
        self.cache[key] = value

    def clear(self):
        """Clears the entire cache."""
        self.cache.clear()


def get_product_details(product_id):
    cached_data = cache.get(product_id)
    if cached_data:
        print("Cache hit! Returning cached data.")
        return cached_data
    else:
        print("Cache miss. Fetching from database...")
        product_data = f"Product details for product {product_id}"
        
        cache.set(product_id, product_data)
        return product_data

cache = SimpleCache()

print(get_product_details(101))  
print(get_product_details(101))
