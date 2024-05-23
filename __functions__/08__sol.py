def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Shaktiman",power="Lazer")
print_kwargs(name="Superman")
print_kwargs(name="Ironman",power="Suit",enemy="Thanos")