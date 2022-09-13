import datetime

import instaloader  # https://instaloader.github.io/as-module.html#python-module-instaloader
from instaloader.structures import Profile
import random

L = instaloader.Instaloader()
# ig = instaloader.Instaloader()
# dp = input("Enter Insta username : ")
#
# ig.download_profile(dp, profile_pic_only=True)

profile = Profile.from_username(L.context, "cat.shitpost")
posts = profile.get_posts()
totalPosts = posts.count

randomPostNumber = random.randint(1, totalPosts)
# list(posts)
# print(profile.)
L.download_pic("cattest", "https://www.instagram.com/p/CiYn0KsvRAq/?utm_source=ig_web_copy_link", datetime.datetime.now())
# L.download_post(posts[randomPostNumber], "CatofTheDay")

# for posts in profile.get_posts():
#     L.download_post(posts, "cat")
#     break

