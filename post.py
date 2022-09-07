class Post:
  def __init__(self, title, message, author):
    self.title = title
    self.message = message
    self.author = author

  def get_post_info(self):
    print(f"Post: {self.title} written by {self.author}")