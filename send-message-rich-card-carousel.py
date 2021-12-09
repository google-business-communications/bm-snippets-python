# This code is based on the https://github.com/google-business-communications/python-businessmessages
# Python Business Messages client library.

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'

import json
import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import (
    BusinessMessagesCardContent, BusinessMessagesCarouselCard,
    BusinessMessagesContentInfo,
    BusinessmessagesConversationsMessagesCreateRequest, BusinessMessagesMedia,
    BusinessMessagesMessage, BusinessMessagesRepresentative,
    BusinessMessagesRichCard, BusinessMessagesSuggestedReply,
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

# Create a carousel message with two cards and a suggested reply for each card
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=representativeType
    ),
    fallback='Card #1\nThe description for card #1\n\nCard #2\nThe description for card #2\n\nReply with \"Card #1\" or \"Card #2\"',
    richCard=BusinessMessagesRichCard(
      carouselCard=BusinessMessagesCarouselCard(
        cardWidth=BusinessMessagesCarouselCard.CardWidthValueValuesEnum.MEDIUM,
        cardContents=[
          BusinessMessagesCardContent(
              title='Card #1',
              description='The description for card #1',
              suggestions=[
                BusinessMessagesSuggestion(
                        reply=BusinessMessagesSuggestedReply(
                            text='Card #1',
                            postbackData='card_1')
                        )
              ],
              media=BusinessMessagesMedia(
                  height=BusinessMessagesMedia.HeightValueValuesEnum.MEDIUM,
                  contentInfo=BusinessMessagesContentInfo(
                      fileUrl='https://storage.googleapis.com/kitchen-sink-sample-images/cute-dog.jpg',
                      forceRefresh=False))),
          BusinessMessagesCardContent(
              title='Card #2',
              description='The description for card #2',
              suggestions=[
                BusinessMessagesSuggestion(
                        reply=BusinessMessagesSuggestedReply(
                            text='Card #2',
                            postbackData='card_2')
                        )
              ],
              media=BusinessMessagesMedia(
                  height=BusinessMessagesMedia.HeightValueValuesEnum.MEDIUM,
                  contentInfo=BusinessMessagesContentInfo(
                      fileUrl='https://storage.googleapis.com/kitchen-sink-sample-images/elephant.jpg',
                      forceRefresh=False)))
        ]
    )))

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
