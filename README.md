# PostersAndVoters
A simpe REST app where users can make posts and vote for them based on permisstions granted.

## Available endpoinsts:
- /api-auth/login/ -> default rest_framework authentication
- /api-auth/logout/ -> default rest_framework authentication
- /api/posts -> GET for getting all the posts, POST for creating new post
- /api/posts/{id} -> GET/PUT/PATCH/DELETE for retrieving, updating or deleting the post bound to user, otherwise you can only retrieve it.
- /api/posts/{id}/vote -> POST/DELETE for voting or deleting the vote on voted post. Restriction: 1 vote per user on each post.

## How to run the app
In terminal activate virtual env and run the following command: `pip install -r requirements.txt`