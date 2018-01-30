from kickstarters.models import KickStarter
from rest_framework import status, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

class KickStarterViewSet(viewsets.ViewSet):
    queryset = KickStarter.objects.all()

    @list_route(methods=['get'])
    def get_kickstarters(self, request):
        """
        GET all kickstarter iframes.
        """
        ks_list = [ks.iframe for ks in KickStarter.objects.all()]
        return Response(ks_list, status=status.HTTP_201_CREATED)
