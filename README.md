# PostersAndVoters
A simpe REST app where users can make posts and vote for them based on permisstions granted.

## Available endpoinsts:
- /api-auth/login/ -> default rest_framework authentication
- /api-auth/logout/ -> default rest_framework authentication
- /api/posts -> GET for getting all the posts, POST for creating new post
- /api/posts/{id} -> GET/PUT/PATCH/DELETE for retrieving, updating or deleting the post bound to user, otherwise you can only retrieve it.
- /api/posts/{id}/vote -> POST/DELETE for voting or deleting the vote on voted post. Restriction: 1 vote per user on each post.

## Installation:

1. Clone the repository:
```
git clone https://github.com/Techinek/PostersAndVoters.git
```
2. Install all the needed packages:
```
pip install -r requirements.txt
```
3. Make migrations:
```
python manage.py makemigrations и $ python manage.py migrate
```
4. Finally run local server:
```
python manage.py runserver
```
