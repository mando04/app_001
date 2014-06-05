from django.forms import ModelForm
from www.models import Post



class PostForm(ModelForm):
    css_class = "error"
    class Meta:
        model = Post
        fields = ['title','author','text','slug']