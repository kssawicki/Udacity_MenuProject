from os import environ

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

google_web = dict(
    client_id=environ.get("google_client_id", "822379949264-taq1cb3r1mq3n7qkqjb3marbtu9c8fko.apps.googleusercontent.com"),
    project_id=environ.get("google_project_id", "udacity-menuproject"),
    auth_uri=environ.get("google_auth_uri", "https://accounts.google.com/o/oauth2/auth"),
    token_uri=environ.get("google_token_uri", "https://accounts.google.com/o/oauth2/token"),
    auth_provider_x509_cert_url=environ.get("google_x509", "https://www.googleapis.com/oauth2/v1/certs"),
    client_secret=environ.get("google_client_secret", "ZzDdYkxWKFidw16aLKy0wM8q"),
    javascript_origins=[
        "http://localhost:5000"
    ],
    scope='',
    redirect_uris=[
        "https://localhost:5000/callback",
        "http://localhost:5000/callback"
    ]
)

facebook_web = dict(
    app_id=environ.get('facebook_app_id', '1601321699917905'),
    app_secret=environ.get('facebook_app_secret', '442f6fe82e2c550ceb966d52c9422f4c')
)

main_app = dict(
    secret_key=environ.get('app_secret_key', 'super secret key'),
    debug=environ.get('debug', True)
)
