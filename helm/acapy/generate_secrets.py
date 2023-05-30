#! /usr/bin/env python
import base58, secrets, jinja2, nacl.signing

def generate_seed(seed=None):
    if seed: pass
    else: seed = secrets.token_hex(16)
    vk = bytes(nacl.signing.SigningKey(seed.encode("ascii")).verify_key)
    did = base58.b58encode(vk[:16]).decode("ascii")
    verkey = base58.b58encode(vk).decode("ascii")
    return seed, did, verkey

endorser = {
    "api_key": secrets.token_hex(16),
    "wallet_key": secrets.token_hex(16)
}
endorser['seed'], endorser['did'], endorser['verkey'] = generate_seed(seed=None)
author = {
    "api_key": secrets.token_hex(16),
    "wallet_key": secrets.token_hex(16)
}
author['seed'], author['did'], author['verkey'] = generate_seed(seed=None)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "secret_values.jinja"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(
    endorser=endorser,
    author=author
    )

with open("secret_values.yaml", "w") as f:
    f.write(outputText)