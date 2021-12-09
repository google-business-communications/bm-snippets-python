# This code is based on the https://github.com/google-business-communications/python-businessmessages
# Python Business Messages client library.

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'
oauth_client_id = 'EDIT_HERE'
oauth_code_challenge = 'EDIT_HERE'
oauth_scope = 'EDIT_HERE'

import json
import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import (
    BusinessMessagesAuthenticationRequest,
    BusinessMessagesAuthenticationRequestOauth,
    BusinessmessagesConversationsMessagesCreateRequest,
    BusinessMessagesMessage, BusinessMessagesRepresentative,
    BusinessMessagesSuggestion)
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    path_to_service_account_key,
    scopes=['https://www.googleapis.com/auth/businessmessages'])

client = bm_client.BusinessmessagesV1(credentials=credentials)

representativeTypeAsString = 'BOT'
if representativeTypeAsString == 'BOT':
    representativeType = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
else:
    representativeType = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.HUMAN

# Create a text message with an authentication request
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=representativeType
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
