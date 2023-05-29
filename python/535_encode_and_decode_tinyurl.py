import hashlib


class Codec:
    def __init__(self):
        self.url_map = {}
        self.base_url = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""

        hash_md5 = hashlib.md5(longUrl.encode())
        hash_hex = hash_md5.hexdigest()
        key = hash_hex[:6]

        self.url_map[key] = longUrl

        return self.base_url + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""

        long_url = shortUrl.split('/')[-1]
        return self.url_map.get(long_url)
