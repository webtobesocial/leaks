#!/usr/bin/env python3

import hashlib


def hash_password(password):
    password_string_utf8 = password.encode('utf-8')
    password_string_utf16 = password.encode('utf-16le')

    hash_md5 = hashlib.md5(password_string_utf8).hexdigest()
    hash_sha1 = hashlib.sha1(password_string_utf8).hexdigest()
    hash_sha224 = hashlib.sha224(password_string_utf8).hexdigest()
    hash_sha256 = hashlib.sha256(password_string_utf8).hexdigest()
    hash_sha384 = hashlib.sha384(password_string_utf8).hexdigest()
    hash_sha512 = hashlib.sha512(password_string_utf8).hexdigest()
    hash_ntlm = hashlib.new('md4', password_string_utf16).hexdigest()

    return {
        'md5': hash_md5,
        'sha1': hash_sha1,
        'sha224': hash_sha224,
        'sha256': hash_sha256,
        'sha384': hash_sha384,
        'sha512': hash_sha512,
        'ntlm': hash_ntlm
    }
