def make_averager():
    series = []
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)


