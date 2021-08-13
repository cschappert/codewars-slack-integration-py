# Copyright 2021 Chris Schappert
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import requests
from app import schema


def get_username_by_id(user_id):
    url = f"https://www.codewars.com/api/v1/users/{user_id}"
    res = requests.get(url)
    s = schema.UserSchema()
    r = s.loads(res.content.decode("utf-8"))
    return r['username']


def get_last_challenge_completed_by_username(username):
    url = f"https://www.codewars.com/api/v1/users/{username}/code-challenges/completed?page=0"
    res = requests.get(url)
    s = schema.ChallengesSchema()
    r = s.loads(res.content.decode("utf-8"))
    name = r['data'][0]['name']
    slug = r['data'][0]['slug']
    # TODO create a type for this
    return {"name": name, "slug": slug}


def get_challenge_details_by_slug(slug):
    url = f"https://www.codewars.com/api/v1/code-challenges/{slug}"
    res = requests.get(url)
    s = schema.CodeChallengeSchema()
    r = s.loads(res.content.decode("utf-8"))
    return r['url']
