
from rest_framework import status
from rest_framework.parsers import  JSONParser
from rest_framework.response import Response

from contacts.serializers import (ContactSerailizer)
from core.permissions import AllowAnyAPIView
from sendmail.views import consultation_message_received_mail

import requests
from django.conf import settings




def verify_recaptcha(token, remote_ip=None):

    
    secret_key = settings.GOOGLE_SECRET_KEY
    data = {"secret": secret_key, "response": token}
    if remote_ip:
        data["remoteip"] = remote_ip
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
    return response.json()


class ContactCreateView(AllowAnyAPIView):
    parser_classes = (JSONParser,)

    def post(self, request):
        captcha_token = request.data.get("captcha")
        captcha_result = verify_recaptcha(captcha_token, request.META.get("REMOTE_ADDR"))
        if not captcha_result.get("success"):
            return Response({"message": "Captcha verification failed"}, status=400)

        name = request.data.get("name", "")
        capitalized_name = " ".join(word.capitalize() for word in name.strip().split())
        request.data["name"] = capitalized_name

        serializer = ContactSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            name = serializer.data.get("name", "")
            first_name = name.strip().split(" ")[0]
            email = serializer.data.get("email", "")
            phone = serializer.data.get("phone", "")
            message = serializer.data.get("message", "")

            try:
                consultation_message_received_mail(
                    email,
                    f"Hey {first_name}, Namaste,\nThank you for reaching out. We truly value your interest and will be in touch with you very shortly.".strip(),
                    f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage: {message}",
                )
            except Exception as e:
                print(f"Email Error: {e}")
                return Response({"message": "Trouble sending email"}, status=500)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
