from django.shortcuts import render

from .models import FoodEntry
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect

# Pertaining to Comments
from django.contrib.contenttypes.models import ContentType

from comments.forms import CommentForm
from comments.models import Comment


# Create your views here.
def food_list(request):
    """
    Main index that displays blog post.
    Grabs "filter" from cookies in order to filter the query of the database
    :param request:
    :return:
    """

    # get the name of the string called "filter"
    food_filter = str(request.GET.get('filter'))

    # Select only the objects in the database that match the filter
    if food_filter:
        if food_filter == 'breakfast':
            food_posts = FoodEntry.objects.filter(breakfast=True).filter(published=True)
        elif food_filter == 'entree':
            food_posts = FoodEntry.objects.filter(entree=True).filter(published=True)
        elif food_filter == 'snack':
            food_posts = FoodEntry.objects.filter(snack=True).filter(published=True)
        elif food_filter == 'foodprep':
            food_posts = FoodEntry.objects.filter(foodprep=True).filter(published=True)
        elif food_filter == 'beverage':
            food_posts = FoodEntry.objects.filter(snack=True).filter(published=True)
        elif food_filter == 'vegan':
            food_posts = FoodEntry.objects.filter(vegan=True).filter(published=True)
        elif food_filter == 'vegetarian':
            food_posts = FoodEntry.objects.filter(vegan=True).filter(published=True)
        elif food_filter == 'glutenfree':
            food_posts = FoodEntry.objects.filter(vegan=True).filter(published=True)
        else:
            food_posts = FoodEntry.objects.filter().filter(published=True)
    else:
        food_posts = FoodEntry.objects.filter().filter(published=True)

    print(food_posts)

    context = {
        'food_posts': food_posts,
    }

    return render(request, 'food/food_list.html', context)


# Create your views here.
def food_post(request, pk):
    """
    Main index that displays blog post
    :param request:
    :param pk: Primary key of the food post
    :return:
    """
    instance = get_object_or_404(FoodEntry, pk=pk)
    thumbnail = instance.recipe.cover_photo
    comments = instance.comments

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }

    comment_form = CommentForm(request.POST or None, initial=initial_data)

    if comment_form.is_valid():
        parent_obj = None
        c_type = comment_form.cleaned_data.get("content_type")
        print(c_type)
        try:  # TODO: This is my hack to fix <food entry> -> <foodentry> ContentType
            content_type = ContentType.objects.get(model=c_type)
        except:
            content_type = ContentType.objects.get(model=c_type.replace(' ', ''))
        obj_id = comment_form.cleaned_data.get("object_id")

        try:  # Get parent ID of
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:  # Verify parent id exists
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        content_data = comment_form.cleaned_data.get("content")

        new_comment, created = Comment.objects.get_or_create(
            # user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    context = {
        'post': instance,
        'thumbnail': thumbnail,
        'recipe': instance.recipe,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'food/food_post.html', context)


''''''
def add_comment(request, pk):
    """
    Add a comment to the food_post
    :param request: request
    :param pk: Database primary key of the food_post
    :return:
    """

    food_post = get_object_or_404(FoodEntry, pk=pk)

    if request.method == "POST":
        form = FoodEntryCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.food_post = food_post
            comment.save()
            return redirect('food_post', pk=food_post.pk)
    else:
        form = FoodEntryCommentForm()
    return render(request, 'add_comment.html', {'form': form})
