import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = ("AAAAAAAAAAAAAAAAAAAAAIgBigEAAAAAsx5kPMshGB7oKN%2FEdLzqJfxAE0s%3DIVJ5vS2W5EhFweG9HTv4LdhHXoOmrKDpfEC4P1u6iuf9aguR3b")


def create_url(TwitterName):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=" + TwitterName
    user_fields = "user.fields=id"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url("SenatorBaldwin")
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True).split('"')[5])


if __name__ == "__main__":
    main()