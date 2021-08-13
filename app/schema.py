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
from marshmallow import Schema, fields, EXCLUDE


class UserSchema(Schema):
    username = fields.Str(required=True)
    name = fields.Str(required=True)

    class Meta:
        unknown = EXCLUDE


class DataSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    slug = fields.Str()

    class Meta:
        unknown = EXCLUDE


class ChallengesSchema(Schema):
    data = fields.List(fields.Nested(DataSchema))

    class Meta:
        unknown = EXCLUDE


class CodeChallengeSchema(Schema):
    name = fields.Str(required=True)
    url = fields.Url(required=True)

    class Meta:
        unknown = EXCLUDE


class PayloadUserSchema(Schema):
    id = fields.Str(required=True)

    class Meta:
        unknown = EXCLUDE


class WebhookPayloadSchema(Schema):
    action = fields.Str(required=True)
    user = fields.Nested(PayloadUserSchema)

    class Meta:
        unknown = EXCLUDE
