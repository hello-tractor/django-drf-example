from .models import Farm, Farmer
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__' # ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

# Serializers define the API representation.
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__' # ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'farm', FarmViewSet)
router.register(r'farmer', FarmViewSet)