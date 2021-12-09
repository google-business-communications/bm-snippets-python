# This code is based on the https://github.com/google-business-communications/python-businessmessages
# Python Business Messages client library.

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'

import json
import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import (
    BusinessmessagesConversationsSurveysCreateRequest, BusinessMessagesSurvey)
from oauth2client.service_account import ServiceAccountCredentials

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
