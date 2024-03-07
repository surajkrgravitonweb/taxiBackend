from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class RegisterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve all registered accounts
        queryset = UserRegistration.objects.all()
        serializer = RegisterSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new account
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        # Update an existing account
        try:
            account = UserRegistration.objects.get(pk=pk)
        except UserRegistration.DoesNotExist:
            return Response({"detail": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RegisterSerializers(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        # Delete an existing account
        try:
            account = UserRegistration.objects.get(pk=pk)
        except UserRegistration.DoesNotExist:
            return Response({"detail": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    



class UserLoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate the user
        try:
            user = UserRegistration.objects.get(username=username, password=password)
        except UserRegistration.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # You can customize the response based on your requirements
        response_data = {
            "msg": "Login successful",
            "status": "success",
            "user_id": user.id,
            "username": user.username,
            # Add more fields as needed
        }

        return Response(response_data, status=status.HTTP_200_OK)


from django.http import Http404

class GetTaxiFormListCreateView(APIView):
    def get(self, request, format=None):
        queryset = GetTaxiForm.objects.all()
        serializer = GetTaxiFormSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GetTaxiFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Record created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetTaxiFormRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return GetTaxiForm.objects.get(pk=pk)
        except GetTaxiForm.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = GetTaxiFormSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = GetTaxiFormSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Record updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'status': 'success', 'message': 'Record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



class DriverListCreateView(APIView):
    def get(self, request, format=None):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "msg": "Driver created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverDetailView(APIView):
    def get_object(self, pk):
        try:
            return Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Response({"status": "error", "msg": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "msg": "Driver updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        driver = self.get_object(pk)
        driver.delete()
        return Response({"status": "success", "msg": "Driver deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response


class SendmailRegistrations(APIView):
    def post(self, request):
        email = request.data.get('to')  # Recipient's email address
        user_id = request.data.get('userid')
        password = request.data.get("password")

        if not email:
            return Response({'status': False, 'message': 'Email address is missing'})

        # Construct the email message
        email_subject = "Welcome to ShubhamTravellers!"
        email_body = (
            f"Dear User,\n\n"
            f"Congratulations and welcome to Shubham Travellers!\n\n"
            f"Your account has been successfully created. Here are your login details:\n"
            f"User ID: {user_id}\n"
            f"Password: {password}\n\n"
            "Please keep your credentials secure \n\n"
            "If you have any questions or need assistance, feel free to reach out to our support team at support@ShubhamTravellers.com.\n\n"
            "Best regards,\n"
            "The Shubham Travellers Team"
        )

        email_message = EmailMessage(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            [email]
        )

        try:
            email_message.send()
            return Response({'status': True, 'message': 'Email sent successfully'})
        except Exception as e:
            return Response({'status': False, 'message': 'Failed to send email', 'error': str(e)})


from rest_framework import generics

class ContactNameListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactNameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# invoices/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Invoice

@csrf_exempt
def upload_invoice(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        amount = request.POST.get('amount')

        # Save PDF file
        pdf_file = request.FILES.get('pdf_file')
        file_path = default_storage.save(f'invoices/pdfs/{pdf_file.name}', ContentFile(pdf_file.read()))

        # Save invoice details to the database
        invoice = Invoice.objects.create(
            customer_name=customer_name,
            amount=amount,
            pdf_file=file_path
        )

        return JsonResponse({'success': True, 'invoice_id': invoice.id})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})



def get_invoices(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()

        data = []
        for invoice in invoices:
            data.append({
                'id': invoice.id,
                'customer_name': invoice.customer_name,
                'amount': str(invoice.amount),
                'pdf_file': invoice.pdf_file.url,
            })

        return JsonResponse({'success': True, 'data': data})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})



