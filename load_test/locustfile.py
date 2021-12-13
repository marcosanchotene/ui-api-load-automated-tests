import logging
import random

from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 5)

    @task(10)
    def get_post(self):
        post_id = random.randrange(1, 100)
        self.client.get(f"posts/{post_id}")

    @task(5)
    def get_comments(self):
        post_id = random.randrange(1, 100)
        self.client.get(f"comments?postId={post_id}")

    @task(1)
    def create_post(self):
        user_id = random.randrange(1, 10)
        response = self.client.post("posts", json={"title": "foo", "body": "bar", "userId": user_id})
        if response.status_code != 201:
            logging.info(f"Create post response:\n status code: {response.status_code}\n body: {response.text}")

    @task(2)
    def delete_post(self):
        photo_id = random.randrange(1, 5000)
        self.client.delete(f"photos/{photo_id}")
