import matplotlib.pyplot as plt
import statistics

# participants times on the 5 tasks
p1 = [15.6, 5.2, 4.9, 15, 6.2]
p2 = [23.2, 7.4, 6, 32.1, 8.8]
p3 = [7.8, 5.9, 6.2, 11.2, 4.9]
p4 = [8, 7.8, 14.4, 13, 11.7]
p5 = [32, 5.2, 6.3, 8.8, 5.2]


def show_sums():
    # declare vars
    task_sum = [0, 0, 0, 0, 0]
    task_means = [0, 0, 0, 0, 0]

    # calculate sums
    for x in range(5):
        task_sum[x] = p1[x] + p2[x] + p3[x] + p4[x] + p5[x]

    # calculate means
    for x in range(5):
        task_means[x] = round(task_sum[x] / 5, 2)

    # print(task_sum)
    print(f'means: {task_means}')
    print(f'standard div: {round(statistics.stdev(task_sum), 2)}')

    # pie chart
    labels = ['task 1', 'task 2', 'task 3', 'task 4', 'task 5']
    explode = (.15, 0, 0, .1, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(task_sum, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')

    plt.show()


def extra_clicks():
    clicks_by_task = [2, 0, 0, 6, 1]

    # bar chart
    fig, ax = plt.subplots()
    tasks = ['task 1', 'task 2', 'task 3', 'task 4', 'task 5']
    bar_colors = ['tab:blue', 'tab:blue', 'tab:blue', 'tab:red', 'tab:purple']

    ax.bar(tasks, clicks_by_task, color=bar_colors)

    ax.set_ylabel('Total number of extra clicks')
    ax.set_title('Extra clicks')

    plt.show()


if __name__ == '__main__':
    show_sums()
    # extra_clicks()
