# Django Based Blog
A personal project based on Python Django Web Application Framework
# Features
* Clean and responsive design
* Supports rich text post content using quill editor
* Has content word counter when you type
* Auto generated sitemap feature
* Dynamic meta description generator
* More features coming soon ...
* 
# Goal
To learn Django with hands on experience to increase the experience with the framework<br>
Using github and git to track and push the new changes as I continue to develop more

# How to Setup a django project from scratch?
1. Install Django (if not installed) using <code>pip install django</code>
2. Run command: (create the base project)
<pre>django-admin startproject project_name</pre>
3. Create an app inside the project.
run command:
<pre>python manage.py startapp home</pre>
4. register the app (copy the class name from apps.py and place inside installed_apps of settings.py)
5. do the initial migration<br>
- step 1: create migration files using below command
- <pre>python manage.py makemigrations</pre>
- step 2: run the migration
- <pre>python manage.py migrate</pre>

# How to run this project?
<pre>python manage.py runserver</pre>

# To-Do
- [x] Create a landing page
- [x] Activate user account system
- [x] Let the logged in user submit a blog post
- [x] Configure the post details page
- [x] Allow people to register
- [x] Update the post creation page
- [x] Create a clean design
- [x] Let people comment on posts
- [ ] Enable email verification
- [x] Implement all the CRUD concepts
- [ ] Change the database to mysql
- [ ] Add more To-Do list later
