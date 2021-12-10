from time import perf_counter
import matplotlib.pyplot as plt
import matplotx

def race(lola, lynne, lines):
    fig, ax = plt.subplots()
    loop_count = 1000
    lynne_times = [0]
    lola_times = [0]
    loops = range(loop_count)
    for _ in loops:
        lynne_start = perf_counter()
        lynne(lines)
        lynne_time = perf_counter() - lynne_start
        lynne_times.append(lynne_time + lynne_times[-1])

    # print(f'Lynne: {lynne_time} ({lynne_time/loops}/it)')
    for _ in loops:
        lola_start = perf_counter()
        lola(lines)
        lola_time = perf_counter() - lola_start
        lola_times.append(lola_time + lola_times[-1])
    lola_times.pop(0)
    lynne_times.pop(0)

    diffs = [abs(lola_times[i] - lynne_times[i]) for i in loops]

    ax.plot(loops, lola_times, label='Lola')
    ax.plot(loops, lynne_times, label='Lynne')
    ax.plot(loops, diffs, label='Diff')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cumulative execution time')
    matplotx.line_labels()

    plt.show()