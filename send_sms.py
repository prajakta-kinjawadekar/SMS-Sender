# /* Each SMS can only be a maximum of 160 characters.
#    If the user wants to send a message bigger than that, we need to break it up.
#    We want a multi-part message to have this suffix added to each message:
#    " - Part X of Y"
# */

# // You need to fix this method, currently it will crash with > 160 char messages.
# function sendSmsMessage (text, to, from) {
#   deliverMessageViaCarrier(text, to, from)
# }

# // This method actually sends the message via an already existing SMS carrier
# // This method works, you don't change it,
# function deliverMessageViaCarrier (text, to, from) {
#   SmsCarrier.deliverMessage(text, to, from)
# }
import math
LENGTH = 160
PAGING = "- Part %s of %s"

def get_paging_string(index, total):
  '''
  Method to get the paging string
  :param index(int) : index number
  :param total(int) : total page numbers

  returns: String to be added as pagination
  '''
  return PAGING%(index, total)

def get_index_of_last_space_before_nth_char(text, n):
  '''
  Method that checks where to cut the message (it can't be cut at
  160th char because it could cut mid-word).

  :param text(str) - text message
  :param n(int) - len of text message

  return: If space does not exist in message, returns end position.
          If space exists, returns space position + 1, to retain space in text.

  '''
  val = text[:n].rfind(' ')
  if val == -1:
      return n
  else:
      return val + 1

def send_sms_message(text, recipent=None, sender=None):
  '''
  Method that takes in a string message and returns
  an array of string messages with pagination if required.

  :param text(str) - Text Message to send
  :param recipent(str) - Recipent Number. Defaults to None as considered dummy.
  :param sender(str) - Sender Number. Defaults to None as considered dummy.

  return: List of messages
  '''
  if not text:
    raise Exception("Empty Message. Cannot send SMS")
  string_messages = []
  if len(text) <= LENGTH:
    # No pagination is needed
    string_messages.append(text)
  else:
    # Pagination is needed
    index = -1
    total = math.ceil(len(text)/LENGTH)
    while text:
      index += 1
      single_str_max_len = LENGTH - len(str(get_paging_string(index, total)))
      if len(text) <= single_str_max_len:
        # if it's the last message then don't bother about not breaking words
        # if space does not exist before pagination string in message. Add space
        if(len(text) + len(str(get_paging_string(index, total))) \
          < LENGTH and text[-1] != " "):
          text += " "
        msg_len = len(text)
      else:
        # check where is the last space before
        # end of the sms to avoid breaking words
        msg_len = get_index_of_last_space_before_nth_char(
          text,
          single_str_max_len)
      # generate new SMS
      msg_content = text[: msg_len]
      # append it to returned list
      string_messages.append(msg_content)
      # cut it out of the whole text
      text = text[msg_len:]
    # append pagination to each string message
    for i in range(0, len(string_messages)):
      string_messages[i] += get_paging_string(i+1, len(string_messages))

  sms_packets = []
  for each_sms in string_messages:
    sms_packets.append(each_sms)
    deliver_message_via_carrier(each_sms, recipent, sender)
  return sms_packets


def deliver_message_via_carrier(text, recipent, sender):
  '''
  Method to send message via an already existing SMS carrier.
  SMS carries is considered to be dummy

  :param text(str) - Text Message to send
  :param recipent(str) - Recipent Number. Defaults to None as considered dummy.
  :param sender(str) - Sender Number. Defaults to None as considered dummy.
  '''
  print("....Sending SMS....")
  print(f"Length of Text: {len(text)}")
  print(f"Actual Text: {text}")

if __name__=="__main__":
  send_sms_message(text="Message Writing is one of the common formal\
  types of writing that we learn in our school curriculum")  
