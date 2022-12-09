import re, datetime
from rest_framework import serializers
from tasks.models import Task, Category, User
from django.core.exceptions import ObjectDoesNotExist


class EmailRelatedField(serializers.RelatedField):
    lookup_field = 'pk'

    def to_representation(self, value):
        return value.email

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get(pk=self.pk)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('invalid')


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='api:task-detail')
    user = EmailRelatedField(queryset=User.objects.all())
    priority = serializers.CharField(source='get_priority_display', required=False)
    category = serializers.HyperlinkedRelatedField(view_name='api:category-detail', queryset=Category.objects.all())
    to_deadline = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_to_deadline(self, obj):
        return obj.deadline.date() if obj.deadline else None


class CategorySerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['title', 'tasks']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

    def validate_email(self, value):
        if not re.match(r'^[\w.\-]{1,25}@yandex\.(by|ru|ua|com)$', value):
            raise serializers.ValidationError('wrong email')
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('user exists')
        return value

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        if not any([first_name, last_name]):
            raise serializers.ValidationError('first_name or last_name required')
        return attrs
