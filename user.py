class User:
  def __init__(self, username, email, password, job_title):
    self.username = username
    self.email = email
    self.password = password
    self.job_title = job_title
  
  def change_password(self, new_password):
    self.password = new_password

  def change_job_title(self, new_job_title):
    self.job_title = new_job_title

  def get_user_info(self):
    print(f"username: {self.username}, email: {self.email}, job title: {self.job_title}")


