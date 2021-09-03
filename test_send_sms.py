from send_sms import send_sms_message
import unittest
import test_input_data as input_data
import test_output_data as output_data

class TestSendSMS(unittest.TestCase):
  """
  Class for all Send SMS related tests
  """
  def test_empty_message(self):
    '''
    test to check empty message
    '''
    try:
        send_sms_message(text="")
    except Exception as ex:
        assert ex.args[0] == "Empty Message. Cannot send SMS"

  def test_message_length_less_than_160(self):
    '''
    test to check when message
    length is less than 160
    '''
    actual_value = send_sms_message(text=\
        input_data.LENGTH_LESS_THAN_160)
    expected_value = actual_value
    assert actual_value == expected_value

  def test_message_length_greater_than_160_breaking_at_word(self):
    '''
    test to check when message
    length is less than 160 and the message is breaking a word
    '''
    actual_value = send_sms_message(text=\
        input_data.LENGTH_GREATER_THAN_160_AND_BREAKING_AT_WORD)
    expected_value = output_data.LENGTH_GREATER_THAN_160_BREAKING_AT_WORD
    print(actual_value)
    assert actual_value == expected_value
    for value in expected_value:
        assert len(value) < 160

  def test_message_length_greater_than_160_greater_than_10_messages(self):
    '''
    test to check when message
    length is less than 160 and the messages are greater than 10 
    '''
    actual_value = send_sms_message(text=\
        input_data.LENGTH_GREATER_THAN_160_AND_GREATER_THAN_10_MESSAGES)
    expected_value = output_data.LENGTH_GREATER_THAN_160_AND_GREATER_THAN_10_MESSAGES
    assert actual_value == expected_value
    for value in expected_value:
        assert len(value) < 160

  def test_message_length_greater_than_160_whitespace_at_end_of_message(self):
    '''
    test to check when message
    length is less than 160 and there is a whitespace at end of message
    '''
    actual_value = send_sms_message(text=\
        input_data.LENGTH_GREATER_THAN_160_AND_WHITESPACE_AT_END_OF_MESSAGE)
    expected_value = output_data.LENGTH_GREATER_THAN_160_AND_WHITESPACE_AT_END_OF_MESSAGE
    assert actual_value == expected_value


if __name__=="__main__":
  unittest.main()