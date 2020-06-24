file = '../PyPoll/resources/election_data.csv'

with open(file, 'r') as text:

    print(text)

    lines = text.read()

    print(f"file has {len(lines)} lines")
