from locust import HttpUser, task

class HelpDeskLocust(HttpUser):

    @task
    def get_tickets(self):
        self.client.get("/v1/ticket")
