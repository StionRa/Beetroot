def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature < 800) and (neutrons_emitted > 500):
        return True
    else:
        return False
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    rand = (generated_power/theoretical_max_power)*100
    if rand >= 80:
        return "green"
    elif rand < 80 and rand >60:
        return 'orange'
    elif rand < 60 and rand > 30:
        return 'red'
    elif rand < 30:
        return 'black'
    else:
        return False
print(reactor_efficiency(200,50,15000))

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < threshold * 0.9:
        return 'LOW'
    elif 0.9 * threshold <= temperature * neutrons_produced_per_second <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'
print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))

    #fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)