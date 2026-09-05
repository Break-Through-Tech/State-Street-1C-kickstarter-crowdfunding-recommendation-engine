import os
from flask import Flask, request, redirect
from dotenv import load_dotenv #https://pypi.org/project/python-dotenv/

# python OAuth 2.0 Auth integration for box, persistent file storage is used
from box_sdk_gen import BoxOAuth, BoxClient, OAuthConfig, FileTokenStorage, GetAuthorizeUrlOptions

load_dotenv()

app = Flask(__name__)

# https://github.com/box/box-python-sdk/blob/main/docs/authentication.md#file-token-storage

auth = BoxOAuth(OAuthConfig(
        client_id=os.environ["BOX_CLIENT_ID"], # os.environ for immediate fail instead of fallback
        client_secret=os.environ["BOX_CLIENT_SECRET"],
        token_storage=FileTokenStorage(),
    )
)

# https://github.com/box/box-python-sdk/blob/main/docs/authentication.md#authentication-with-oauth2
@app.route("/")
def get_auth():
    auth_url = auth.get_authorize_url(
            options=GetAuthorizeUrlOptions(
                redirect_uri="http://localhost:3000/callback"
            )
    )
    return redirect(auth_url, code=302) #else if url is removed then it returns with 302 status code

@app.route("/callback")
def callback():
    auth.get_tokens_authorization_code_grant(request.args.get("code"))
    client = BoxClient(auth=auth)
    success = "Box authentication success"
    return success

if __name__ == "__main__":
    app.run(port=3000)
