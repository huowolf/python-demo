import hmac

#HMAC(散列消息身份验证码: Hashed Message Authentication Code)
message = b'Hello, world!'
key = b'secret'
h=hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())