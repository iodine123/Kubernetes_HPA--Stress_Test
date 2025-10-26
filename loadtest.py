import random
from locust import HttpUser, task, between

class MultiColorLoadTest(HttpUser):
    wait_time = between(0, 0.5)

    paths = ["/blue", "/green", "/red"]

    @task
    def hit_random_path(self):
        path = random.choice(self.paths)
        with self.client.get(path, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"{path} failed with {response.status_code}")
            else:
                response.success()
