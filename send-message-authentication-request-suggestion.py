# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sends a text message to the user with an authentication request suggestion.

It allows the user to authenticate with OAuth and has a fallback text.
Read more: https://developers.google.com/business-communications/business-messages/guides/how-to/message/send?hl=en#authentication-request-suggestion

This code is based on the https://github.com/google-business-communications/python-businessmessages
Python Business Messages client library.
"""

import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import BusinessMessagesAuthenticationRequest
from businessmessages.businessmessages_v1_messages import BusinessMessagesAuthenticationRequestOauth
from businessmessages.businessmessages_v1_messages import BusinessmessagesConversationsMessagesCreateRequest
from businessmessages.businessmessages_v1_messages import BusinessMessagesMessage
from businessmessages.businessmessages_v1_messages import BusinessMessagesRepresentative
from businessmessages.businessmessages_v1_messages import BusinessMessagesSuggestion
from oauth2client.service_account import ServiceAccountCredentials

# Before continuing, learn more about the prerequisites for authenticating
# with OAuth at: https://developers.google.com/business-communications/business-messages/guides/how-to/integrate/oauth?hl=en

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'
oauth_client_id = 'EDIT_HERE'
oauth_code_challenge = 'EDIT_HERE'
oauth_scope = 'EDIT_HERE'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    path_to_service_account_key,
    scopes=['https://www.googleapis.com/auth/businessmessages'])

client = bm_client.BusinessmessagesV1(credentials=credentials)

representative_type_as_string = 'BOT'
if representative_type_as_string == 'BOT':
  representative_type = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
else:
  representative_type = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.HUMAN

# Create a text message with an authentication request
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=representative_type
    ),
    text='Sign in to continue the conversation.',
    fallback='Visit support.growingtreebank.com to continue.',
    suggestions=[
        BusinessMessagesSuggestion(
            authenticationRequest=BusinessMessagesAuthenticationRequest(
                oauth=BusinessMessagesAuthenticationRequestOauth(
                    clientId=oauth_client_id,
                    codeChallenge=oauth_code_challenge,
                    scopes=[oauth_scope])
                )
            ),
        ]
    )

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
