a = lambda b: " ".join(
    list(
        map(
            lambda c: c.lower(),
            filter(
                lambda c: sum(1 for d in c if d.isupper()) == 1
                and not c[0].isupper()
                and not c[-1].isupper(),
                b.split()
            )
        )
    )
)