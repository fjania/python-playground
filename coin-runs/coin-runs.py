import random
from statistics import median, mode, mean


def count_runs(seq):
    counts = {}
    last_flip = None
    current_run = 0

    for flip in seq:

        if flip == last_flip or last_flip == None:
            current_run += 1

        else:
            count = counts.get(current_run, 0) + 1
            counts[current_run] = count
            current_run = 1

        last_flip = flip

    count = counts.get(current_run, 0) + 1
    counts[current_run] = count

    return counts

def do_trial(number_of_flips):
    flips = ''.join([random.choice(["H","T"]) for _ in range(number_of_flips)])
    return count_runs(flips)

def collect_trial_data(runs, trials):
    for run_len, count in runs.items():
        trial_run = trials.get(run_len, [])
        trial_run.append(count)
        trials[run_len] = trial_run

def run_trials(num_trials, num_flips):
    print("Number of Trial Runs:", num_trials)
    print("Number of Flips per Trial:", num_flips)
    trials = {}
    for _ in range(num_trials):
        collect_trial_data(do_trial(num_flips), trials)

    print("{:<15} {:>13} {:>10} {:>10} {:>10}".format("Run Length", "Occurances", "Mean", "Median", "Mode"))

    for k in sorted(trials.keys()):
        all_runs = trials[k]
        occurance_percent = len(all_runs) / num_trials * 100
        print("{:<15d} {:>12.2f}% {:10.0f} {:10.0f} {:10d}".format(k, occurance_percent, mean(all_runs), median(all_runs), mode(all_runs)))

run_trials(10000, 1000)
