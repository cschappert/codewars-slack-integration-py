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
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

codewarsIconUrl = "https://www.codewars.com/assets/logos/logo-square-paper-bg-c3d2b1eb4fb35d75b0c0c0e3b74616fab527afdce9d1d3184624cf0b4e950357.jpg"
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)


def post_to_slack(username, challenge_name, url):
    msg = f"User *{username}* completed coding challenge *{challenge_name}*\nTry it! {url}"

    try:
        client.chat_postMessage(
            channel="CEJ7Q970X",
            text=msg,
            icon_url=codewarsIconUrl,
            username="Codewars"
        )
    except SlackApiError as e:
        return
