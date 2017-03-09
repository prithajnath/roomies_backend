# roomies_backend
Main backend for roomies

##API Endpoints
1. `get_auth_token` : Returns a token when passed a valid username and password

```
curl --data "username=jessicajones&password=biliejoe" https://roomies-backend-prithajnath.c9users.io/get_auth_token/ 

```

2. `get_profile` : Returns user details when passed a valid token

```
curl -X GET https://roomies-backend-prithajnath.c9users.io/get_profile -H 'Authorization: Token c37a94ff17f65dcae6e4f925682bf5cf39d75cf7'

```

3. `sign_up` : Registers the new user and returns the newly generated token for that user

```
curl --data "username=${USERNAME}&password=${PASSWORD}" https://roomies-backend-prithajnath.c9users.io/sign_up/

```

##URL 
https://roomies-backend-prithajnath.c9users.io/
