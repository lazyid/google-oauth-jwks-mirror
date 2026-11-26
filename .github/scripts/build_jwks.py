import datetime
import json

with open("/tmp/certs.json", encoding="utf-8") as fp:
    data = json.load(fp)

keys = [
    k for k in data.get("keys", [])
    if k.get("kty") == "RSA" and k.get("kid") and k.get("n") and k.get("e")
]

if not keys:
    raise SystemExit("no usable keys in google certs")

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open("jwks.json", "w", encoding="utf-8") as fp:
    json.dump({"generated_at": now, "keys": keys}, fp, indent=2)
    fp.write("\n")
print("keys:", len(keys))
