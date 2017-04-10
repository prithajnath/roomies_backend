# roomies_backend
A mobile app for finding like minded people to room with. This is the backend code for the REST API.

## API Endpoints
* `get_auth_token` : Returns a token when passed a valid username and password

```
curl --data "username=jessicajones&password=biliejoe" https://roomies-backend-prithajnath.c9users.io/get_auth_token/ 

```

* `get_profile` : Returns user details when passed a valid token

```
curl -X GET https://roomies-backend-prithajnath.c9users.io/get_profile -H 'Authorization: Token c37a94ff17f65dcae6e4f925682bf5cf39d75cf7'

```

* `sign_up` : Registers the new user and returns the newly generated token for that user

```
curl --data "username=${USERNAME}&password=${PASSWORD}&email=${EMAIL}" https://roomies-backend-prithajnath.c9users.io/sign_up/

```

* `profile_pic` : Returns the URL of the associated profile picture

```
curl -X GET https://roomies-backend-prithajnath.c9users.io/profile_pic -H 'Authorization: Token 4ed1b13f2fd75122ea4cfa1b9f986231dc815f1d'

```

* `get_matches` : Returns a list of matches for a given user

```
curl -X GET https://roomies-backend-prithajnath.c9users.io/get_matches -H 'Authorization: Token 4ed1b13f2fd75122ea4cfa1b9f986231dc815f1d'

```

* `get_match_profile` : Returns details of the match

```
curl https://roomies-backend-prithajnath.c9users.io/get_match_profile?username=jessicajones -H 'Authorization: Token 4ed1b13f2fd75122ea4cfa1b9f986231dc815f1d'

```

* `update_profile` : Updates user profile (first_name, last_name, email)

```
curl --data "email=helloluke@marvel.io&first_name=Lucane&last_name=Cagebendix" https://roomies-backend-prithajnath.c9users.io/update_profile -H 'Authorization: Token 245e0226ed84b39af4c8ac5ad9231bac1291f48b'

```


## URL 
https://roomies-backend-prithajnath.c9users.io/
