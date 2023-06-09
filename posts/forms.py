from django import forms
from .models import Post, Comment

class imageForm(forms.Form):
    image = forms.ImageField()


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요',
            }
        )
    )
    select1_content = forms.CharField(
        label='1번 선택지',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '선택지를 입력하세요',
                'style': 'height: 10em;',
            }
        )
    )
    select2_content = forms.CharField(
        label='2번 선택지',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '선택지를 입력하세요',
                'style': 'height: 10em;',
            }
        )
    )
    select1_image = forms.ImageField(
        label='1번 이미지',
        required=False,
    )
    select2_image = forms.ImageField(
        label='2번 이미지',
        required=False,
    )
    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'select2_content', 'select1_image', 'select2_image')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'placeholder': '댓글 내용을 입력하세요',
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)