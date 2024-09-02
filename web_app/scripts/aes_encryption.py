from aes_cipher import DataEncrypter, DataDecrypter, ScryptDefault

def encrypter(data, encrypt_key):
    data_encrypter = DataEncrypter(ScryptDefault)
    data_encrypter.Encrypt(data, encrypt_key)
    enc_data = data_encrypter.GetEncryptedData()
    return enc_data

def decrypter(data, decrypt_key):
    data_decrypter = DataDecrypter(ScryptDefault)
    data_decrypter.Decrypt(data, decrypt_key)
    dec_data = data_decrypter.GetDecryptedData()
    return dec_data