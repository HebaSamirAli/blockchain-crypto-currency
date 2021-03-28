import hashlib
import json

# def stringify(data):
#     return json.dumps(data)

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    # stringified_data =json.dumps(data)
    # stringified_args = map(stringify, args) 

    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one',1,[3]): {crypto_hash('one',1,[3])}")
    print(f"crypto_hash(1,'one',[3]): {crypto_hash(1,'one',[3])}")

if __name__ == '__main__':
    main()