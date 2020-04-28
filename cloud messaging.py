#pip install pip install pyfcm
from pyfcm import FCMNotification 



push_service=FCMNotification(api_key="AAAAzEH9DzA:APA91bHFaOMxGoMmqsWc537JcwyytWoioR2irKNdHFsyLEGGlPjf8H1wlVuh2yUp7ZN8IiarD00esaHPlk1iCRpgI63NoDf_qO0VwNqZIwnKu2n9jjxZn61g7ldaK8FnZMbkHUJ-BFxe")


print(push_service)


registration_id="fWocAhZ550c:APA91bEgzs-bt5J_ZMNJklW335K8YkShIDadbVTynmvpdHkBlY-YvCjJ4ssam6qZNHlWHZ9H7ef_JHrWCCLIp8O4TAzyUk-3NF5bLSNSaKoEpp19VuMoK976BnZeY6nZHBHFc5Q6qLGL"
message_title="Uber update"
message_body="Hi john,your customized news for today is ";

result=push_service.notify_single_device(registration_id,
                                         message_title=message_title,
                                         message_body=message_body,
                                         sound="default",
                                        )


print(result)
#commit2
