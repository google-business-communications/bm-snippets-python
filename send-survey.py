## Copyright 2022 Google LLC
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     https://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

"""This code sends a survey to the user.

Read more: https://developers.google.com/business-communications/business-messages/guides/how-to/message/surveys?hl=en

This code is based on the https://github.com/google-business-communications/python-businessmessages
Python Business Messages client library.
"""

import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import BusinessmessagesConversationsSurveysCreateRequest
from businessmessages.businessmessages_v1_messages import BusinessMessagesSurvey
from oauth2client.service_account import ServiceAccountCredentials

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    path_to_service_account_key,
    scopes=['https://www.googleapis.com/auth/businessmessages'])

client = bm_client.BusinessmessagesV1(credentials=credentials)

# Create the survey request
survey_request = BusinessmessagesConversationsSurveysCreateRequest(
    surveyId=str(uuid.uuid4().int),
    parent='conversations/' + conversation_id,
    businessMessagesSurvey=BusinessMessagesSurvey())

# Send the survey
bm_client.BusinessmessagesV1.ConversationsSurveysService(
    client=client).Create(request=survey_request)
