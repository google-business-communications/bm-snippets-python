# This code is based on the https://github.com/google-business-communications/python-businessmessages
# Python Business Messages client library.

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'

import json
import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import (
    BusinessmessagesConversationsMessagesCreateRequest,
    BusinessMessagesDialAction, BusinessMessagesMessage,
    BusinessMessagesRepresentative, BusinessMessagesSuggestedAction,
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

# Create a text message with a dial action
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=representativeType
    ),
    text='Contact support for help with this issue.',
    fallback='Give us a call at +12223334444.',
    suggestions=[
        BusinessMessagesSuggestion(
            action=BusinessMessagesSuggestedAction(
                text='Call support',
                postbackData='call-support',
                dialAction=BusinessMessagesDialAction(
                    phoneNumber='+12223334444'))
            ),
        ])

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)