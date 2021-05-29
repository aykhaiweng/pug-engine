from rest_framework.views import APIView

from ...models import Pug, Team

from .serializers import PugSerializer, TeamSerializer



class PugCreateListAPIView(APIView):
    """
    Create/List Pugs
    """
    http_method_names = ['GET', 'POST']
    serializer_class = PugSerializer

    def get_initial_queryset(self, *args, **kwargs):
        """
        """
        return Pug.objects.filter(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        """
        Retrieve a list of Pugs
        """
        qs = self.get_initial_queryset(*args, **kwargs)
        return qs

    def get(self, request, *args, **kwargs):
        """
        Retrieve a list of Pugs
        """

    def post(self, request, *args, **kwargs):
        """
        Create a Pug
        """