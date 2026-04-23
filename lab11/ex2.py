a = lambda b: " ".join(
    list(
        map(
            lambda c: c[::-1],
            filter(
                lambda c: not any(d.isdigit() for d in c) and len(c) % 2 == 0,
                b.split()
            )
        )
    )
)