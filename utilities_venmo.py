from venmo_api import Client
from secrets import username, password, usernames

message = "September utilities"
amount = 22.02

assert(len(usernames) == 10)

access_token = Client.get_access_token(username, password)
venmo = Client(access_token=access_token)

for username in usernames:
    user = venmo.user.get_user_by_username(username)
    venmo.payment.request_money(amount, message, user.id)
    print(f"Requesting {amount} from {user.first_name} {user.last_name}")
