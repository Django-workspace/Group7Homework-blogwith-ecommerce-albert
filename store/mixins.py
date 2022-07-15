from django.shortcuts import get_object_or_404
from .models import Post


class MultipleFieldLookupMixin:
    """
    Mixin to filter comments based on slug and id
    """

    def get_object(self):
        queryset = self.get_queryset()  
        queryset = self.filter_queryset(queryset) 
        filter = {}
        parent_id = Post.objects.get(slug=self.kwargs["slug"]).id
        filter["parent"] = parent_id
        filter["id"] = self.kwargs["id"]
        obj = get_object_or_404(queryset, **filter) 
        self.check_object_permissions(self.request, obj)
        return obj