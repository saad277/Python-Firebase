#pip install pip install pyfcm
from pyfcm import FCMNotification 



push_service=FCMNotification(api_key="AAAAzEH9DzA:APA91bHFaOMxGoMmqsWc537JcwyytWoioR2irKNdHFsyLEGGlPjf8H1wlVuh2yUp7ZN8IiarD00esaHPlk1iCRpgI63NoDf_qO0VwNqZIwnKu2n9jjxZn61g7ldaK8FnZMbkHUJ-BFxe")


print(push_service)


registration_id="d6_KH7m_Gzw:APA91bEoSA_6K0Csjct7oAPiY3YNAscRJL58IYw_F-BspQQiKIuYpyB8qa_40gqQ44p5koVB3Io1is65332Ene4iG9V0p5FbHKkFCQkS3bgHAILbMczEQ9jTVqxFXz1iKqssFOW-LCdg"
message_title="Uber update"
message_body="Hi john,your customized news for today is ";

result=push_service.notify_single_device(registration_id,
                                         message_title=message_title,
                                         message_body=message_body)


print(result)
