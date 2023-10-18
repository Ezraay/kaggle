def write_file(output_file, filename):
    with open(filename, 'r') as read_file:
        output_file.writelines(read_file.readlines())


if __name__ == "__main__":
    with open('out.py', 'w+') as file:
        write_file(file, 'source/core/board.py')
        write_file(file, 'source/agents/smart_minimax_agent.py')
        write_file(file, 'kaggle.py')