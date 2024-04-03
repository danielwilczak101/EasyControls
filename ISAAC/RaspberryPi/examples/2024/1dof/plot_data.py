import sqlite3
import matplotlib.pyplot as plt
import sys

database = 'imu_data.db'

def fetch_data(table, id_number):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    query = f"SELECT * FROM {table} WHERE id = ?"
    c.execute(query, (id_number,))
    data = c.fetchone()
    conn.close()
    return data

def plot_data(table, id_number, columns):
    data = fetch_data(table, id_number)
    if data is None:
        print("No data found.")
        return

    timestamps = []
    values = {column: [] for column in columns}

    for row in data:
        timestamps.append(row[1])  # Assuming the second column is the timestamp
        for column in columns:
            index = data.description.index(column)
            values[column].append(row[index])

    for column in columns:
        plt.plot(timestamps, values[column], label=column)

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f'Data for ID {id_number} from {table}')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python plot_data.py <table> <id> <data1> <data2> ...")
        sys.exit(1)

    table_name = sys.argv[1]
    record_id = int(sys.argv[2])
    columns_to_plot = sys.argv[3:]

    plot_data(table_name, record_id, columns_to_plot)


# Example
# python plot_data.py imu_data 5 roll pitch yaw