from .models import KickStarter
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
        return Response(ks_list, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def get_kickstarter_category(self, request):
        """
        GET all entries for a particular kickstarter category
        """
        if request.GET.get('category', None):
            ks_list = [ks.iframe for ks in KickStarter.objects.filter(sort_category=request.GET.get('category'))]
            return Response(ks_list, status=status.HTTP_200_OK)
        else:
            return Response('Category field required.', status=status.HTTP_400_BAD_REQUEST)
