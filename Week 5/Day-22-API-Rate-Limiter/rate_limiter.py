import time


class RateLimiter:

    def __init__(self, token_capacity, refill_rate_per_sec):
        self.capacity = token_capacity
        self.refill_rate = refill_rate_per_sec
        self.ledger = {}

    def allow_request(self, client_ip):

        now = time.time()

        if client_ip not in self.ledger:
            self.ledger[client_ip] = {
                "tokens": self.capacity,
                "last_updated": now
            }

        state = self.ledger[client_ip]

        elapsed = now - state["last_updated"]

        state["tokens"] = min(
            self.capacity,
            state["tokens"] + (elapsed * self.refill_rate)
        )

        state["last_updated"] = now

        if state["tokens"] >= 1:
            state["tokens"] -= 1
            return True

        return False


limiter = RateLimiter(
    token_capacity=3,
    refill_rate_per_sec=0.5
)


client_ip = "127.0.0.1"

print("=== API RATE LIMITER TEST ===")
print("Token Capacity: 3")
print("Refill Rate: 0.5 tokens/sec")
print("Client:", client_ip)
print("-" * 50)

for request_number in range(1, 8):

    if limiter.allow_request(client_ip):
        print(
            f"Request {request_number}: ALLOWED"
        )
    else:
        print(
            f"Request {request_number}: DENIED - Rate Limit Exceeded"
        )

    time.sleep(0.1)

print("-" * 50)
print("Waiting for token refill...")

time.sleep(3)

if limiter.allow_request(client_ip):
    print("After Refill: REQUEST ALLOWED")
else:
    print("After Refill: REQUEST DENIED")