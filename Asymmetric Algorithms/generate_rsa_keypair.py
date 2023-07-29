from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(2048)


private_key_pem = key.export_key(format='PEM')
public_key_pem = key.publickey().export_key(format='PEM')


# Print the public and private keys
print("Public Key (PEM format):")
print(public_key_pem)
print("\nPrivate Key (PEM format):")
print(private_key_pem)
