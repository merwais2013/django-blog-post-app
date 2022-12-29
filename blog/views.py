from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": 'img13.jpg',
        "author": "Merwais",
        "date": date(2022, 7, 12),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views when you get whilst hiking",
        "content": """
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years,
             sometimes by accident, sometimes on purpose (injected humour and the like).
             It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years,
             sometimes by accident, sometimes on purpose (injected humour and the like).
        """
    },
    {
        "slug": "programming-is-fun",
        "image": 'img11.jpg',
        "author": "Merwais",
        "date": date(2022, 11, 22),
        "title": "Programming is Great!",
        "excerpt": "While programming you need to have coffee.",
        "content": """
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years,
             sometimes by accident, sometimes on purpose (injected humour and the like).
             It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years,
             sometimes by accident, sometimes on purpose (injected humour and the like).
        """
    },
    {
        "slug": "into-the-woods",
        "image": 'img12.jpg',
        "author": "Merwais",
        "date": date(2022, 12, 25),
        "title": "Natures Wow..😍!",
        "excerpt": "Nature is amazing only look the amount of the inspiration.",
        "content": """
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years,
             sometimes by accident, sometimes on purpose (injected humour and the like).
             It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years,
             sometimes by accident, sometimes on purpose (injected humour and the like).
        
        """
    }
]


def get_post(post):
    return post['date']



# Create your views here.

def index(request):
    sotrted_posts = sorted(all_posts, key=get_post)
    latest_posts = sotrted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })
    
def post_detail(request, slug):
    post_identified = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post_identified
    })
    