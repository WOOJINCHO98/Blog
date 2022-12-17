from rest_framework import serializers
from .models import Blog
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    blog = serializers.ReadOnlyField(source='blog.title')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('blog', 'user')
        
        
class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    #comment = serializers.StringRelatedField(many=True)
    comment = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')
        