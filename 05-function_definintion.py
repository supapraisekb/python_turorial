days_to_minutes = 24 * 60
days_to_seconds = 24 * 60 * 60

minutes_units = "mins"
seconds_units = "secs"


def days_to_mins_converter():
    print(f"20 days to minutes are {20 * days_to_minutes} {minutes_units}")
    print("done")

def days_to_sec_conv():
    print(f"50 days to seconds are {50 * days_to_seconds} {seconds_units}")
    print("done")


days_to_mins_converter()
days_to_sec_conv()
