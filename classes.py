from user import User
from post import Post

user1 = User("user1", "user1@email.com", "123456", "developer")
user1.get_user_info()

job_title = input("Enter your new job title:\n")
user1.change_job_title(job_title)
user1.get_user_info()

post1 = Post("post 1", "first post","author 1")
post1.get_post_info()
