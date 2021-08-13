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
from app import slack
from app import codewars
from app import schema
from flask import (
    Blueprint, request
)

bp = Blueprint('webhook', __name__, url_prefix='/v1')


@bp.route('/webhook', methods=['POST'])
def hook():
    s = schema.WebhookPayloadSchema()
    r = s.loads(request.get_data().decode("utf-8"))
    if r['action'] == 'honor_changed':
        # print out user id for debugging purposes
        # print(r['user']['id'])
        username = codewars.get_username_by_id(r['user']['id'])
        last_challenge = codewars.get_last_challenge_completed_by_username(
            username)
        challenge_detail = codewars.get_challenge_details_by_slug(
            last_challenge['slug'])
        slack.post_to_slack(username, last_challenge['name'], challenge_detail)
        return {"result": "ok"}
    else:
        return {"result": "ok"}
