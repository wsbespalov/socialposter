from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .controllers import UserAPIController
from .controllers import APIController

from .serializers import UserSerializer

class UserAPIView(APIView):
    
    def get(self, request):
        # get list of users
        controller = UserAPIController()
        result = controller.listUsers()
        serializer = UserSerializer(result)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        # create user
        controller = UserAPIController()
        if request.data:
            data = request.data
            result = controller.createUser(data=data)
            serializer = UserSerializer(result)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": "No data provided"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 



class UserDetailAPIView(APIView):
    
    def get(self, request, pk):
        # get one user
        pass

    def post(self, request, pk):
        # update user
        pass

    def delete(self, request, pk):
        # delete user
        pass


class InstagramAPIView(APIView):

    def post(self, request, pk):
        # make post for user
        pass
