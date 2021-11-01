
from rest_framework import serializers
from .models import Advisor, Booking, Customer

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('name', 'profile_pic','id')

    def create(self, validate_data):
        return Advisor.objects.create(**validate_data)


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = "booking_time"

    def create(self, validate_data):
        return Booking.objects.create(**validate_data)


class BooKingSerializer(serializers.ModelSerializer):
    advisor_name = serializers.CharField(source="advisor_id.name")
    advisor_profile_pic = serializers.ImageField(source="advisor_id.profile_pic")

    class Meta:
        model = Booking
        fields = ('booking_time', 'advisor_name', 'advisor_profile_pic')




class registerCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'password')

        def create(self, validated_data):
            return Customer.objects.create(**validated_data)


class loginCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('email', 'password')










