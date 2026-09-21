"""05: Dunder methods. Python 3.9+; no external dependencies."""


class ProfitSamples:
    def __init__(self, values):
        self.values = list(values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __repr__(self):
        return f"ProfitSamples({self.values!r})"


def main():
    profits = ProfitSamples([0.61, 0.41, 0.71])
    print(len(profits))
    print(profits[0])
    print(profits)


if __name__ == "__main__":
    main()
