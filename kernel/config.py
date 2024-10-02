# https://jupyter-server.readthedocs.io/en/latest/other/full-config.html
# https://jupyter-server.readthedocs.io/en/latest/operators/public-server.html

c.ServerApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$UIXCxD6DoSx7j8JWKpNK+w$D8UxfSJ+HaRXALnjjVydpA9vtD/Livc1+bqM2XB3HNc'
c.PasswordIdentityProvider.hashed_password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$UIXCxD6DoSx7j8JWKpNK+w$D8UxfSJ+HaRXALnjjVydpA9vtD/Livc1+bqM2XB3HNc'

c.ServerApp.tornado_settings = {
    "headers": {
        "Content-Security-Policy": "frame-ancestors 'self' https://umbrecore.com http://localhost:5500"
    }
}
