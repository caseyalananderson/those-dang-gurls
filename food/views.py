from django.shortcuts import render

from .models import FoodPost
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect

# Pertaining to Comments
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from comments.forms import CommentForm
from comments.models import Comment


# Create your views here.
def foodpost_list(request):
    """
    Main index that displays blog post.
    Grabs "filter" from cookies in order to filter the query of the database
    :param request:
    :return:
    """

    print(request.user.username)

    # get the name of the string called "filter"
    food_filter = str(request.GET.get('filter'))

    if food_filter:  # Select the matched ones that match the filter
        if food_filter == 'breakfast':
            food_posts = FoodPost.objects.breakfast()
        elif food_filter == 'entree':
            food_posts = FoodPost.objects.entree()
        elif food_filter == 'snack':
            food_posts = FoodPost.objects.snack()
        elif food_filter == 'dessert':
            food_posts = FoodPost.objects.dessert()
        elif food_filter == 'foodprep':
            food_posts = FoodPost.objects.foodprep()
        elif food_filter == 'beverage':
            food_posts = FoodPost.objects.beverage()
        elif food_filter == 'vegan':
            food_posts = FoodPost.objects.vegan()
        elif food_filter == 'vegetarian':
            food_posts = FoodPost.objects.vegetarian()
        elif food_filter == 'glutenfree':
            food_posts = FoodPost.objects.glutenfree()
        else:
            food_posts = FoodPost.objects.published()
    else:
        food_posts = FoodPost.objects.published()

    context = {
        'food_posts': food_posts,
    }

    return render(request, 'food/foodpost_list.html', context)


# Create your views here.
def foodpost_detail(request, pk):
    """
    Main index that displays blog post
    :param request: django request
    :param pk: Primary key of the food post
    :return:
    """

    instance = get_object_or_404(FoodPost, pk=pk)
    thumbnail = instance.recipe.cover_photo
    comments = instance.comments

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }

    comment_form = CommentForm(request.POST or None, initial=initial_data)

    if comment_form.is_valid():  # If the comment form is valid
        parent_obj = None
        c_type = comment_form.cleaned_data.get("content_type")
        try:  # TODO: Hack to fix <food entry> -> <foodentry> ContentType
            content_type = ContentType.objects.get(model=c_type)
        except:
            content_type = ContentType.objects.get(model=c_type.replace(' ', ''))
        obj_id = comment_form.cleaned_data.get("object_id")

        try:  # Get the id of the parent comment
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:  # Verify parent id exists, get the first
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        content_data = comment_form.cleaned_data.get("content")

        if request.user.username:  # Must be logged in to post comment
            new_comment, created = Comment.objects.get_or_create(
                user=request.user,
                content_type=content_type,
                object_id=obj_id,
                content=content_data,
                parent=parent_obj,
            )
            return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
        else:
            return HttpResponseRedirect('.')

    context = {
        'post': instance,
        'thumbnail': thumbnail,
        'recipe': instance.recipe,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'food/foodpost_detail.html', context)


''''''
def add_comment(request, pk):
    """
    Add a comment to the food_post
    :param request: request
    :param pk: Database primary key of the food_post
    :return:
    """

    food_post = get_object_or_404(FoodPost, pk=pk)

    if request.method == "POST":
        form = FoodPostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.food_post = food_post
            comment.save()
            return redirect('food_post', pk=food_post.pk)
    else:
        form = FoodPostCommentForm()
    return render(request, 'add_comment.html', {'form': form})
