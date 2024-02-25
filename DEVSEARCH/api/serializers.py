from rest_framework import serializers # converts complex data to json format for easy rendering
from projects.models import Project,Tag,Review
from users.models import Profile

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields= "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    # DOING THESE STEPS TO GET OBJECTS FOR SUB FIELDS RATHER THAN ID
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True) 
    reviews = serializers.SerializerMethodField() # since reviews is outside of project model we need to do these steps to add it to the json output

    class Meta:
        model = Project
        fields = '__all__' 
    # since reviews is outside of project model we need to do these steps to add it to the json output
    def get_reviews(self,obj): # serializer methods need to start with get, obj is what we will be serializing  and get_reviews is being used automatically
        reviews= obj.review_set.all()
        serializer= ReviewSerializer(reviews,many=True)
        return serializer.data
