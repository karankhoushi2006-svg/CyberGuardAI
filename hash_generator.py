import hashlib


class HashGenerator:

    def generate_hashes(self, text):

        md5_hash = hashlib.md5(text.encode()).hexdigest()

        sha1_hash = hashlib.sha1(text.encode()).hexdigest()

        sha256_hash = hashlib.sha256(text.encode()).hexdigest()

        sha512_hash = hashlib.sha512(text.encode()).hexdigest()

        print("\n" + "=" * 50)
        print("🔐 HASH GENERATOR")
        print("=" * 50)

        print(f"\nOriginal Text : {text}")

        print("\nMD5")
        print(md5_hash)

        print("\nSHA1")
        print(sha1_hash)

        print("\nSHA256")
        print(sha256_hash)

        print("\nSHA512")
        print(sha512_hash)

        print("=" * 50)

        return {
            "MD5": md5_hash,
            "SHA1": sha1_hash,
            "SHA256": sha256_hash,
            "SHA512": sha512_hash,
        }