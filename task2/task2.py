def processFile(filename, limit):
    seen = set()
    duplicates = []
    firstDuplicate = None
    frequency = {}
    userFrequency = {}
    suspicious = []
    transactions = []

    with open(filename, "r") as file:
        for line in file:
            tid, user, amount = line.strip().split(",")
            amount = int(amount)

            transaction = (tid, user, amount)
            key = (user, amount)

            transactions.append(transaction)

            if key in seen:
                duplicates.append(transaction)

                if firstDuplicate is None:
                    firstDuplicate = transaction
            else:
                seen.add(key)

            if key in frequency:
                frequency[key] += 1
            else:
                frequency[key] = 1

            if user in userFrequency:
                userFrequency[user] += 1
            else:
                userFrequency[user] = 1

            if amount > limit:
                suspicious.append(transaction)

    return duplicates, firstDuplicate, frequency, userFrequency, suspicious, transactions


def topUsers(userFrequency, n):
    return sorted(
        userFrequency.items(),
        key=lambda x: x[1],
        reverse=True
    )[:n]


def topTransactions(transactions, n):
    return sorted(
        transactions,
        key=lambda x: x[2],
        reverse=True
    )[:n]


def display(filename):
    duplicates, firstDuplicate, frequency, userFrequency, suspicious, transactions = processFile(
        filename, 10000
    )

    print("Duplicates:", duplicates)
    print("First Duplicate:", firstDuplicate)
    print("Frequency:", frequency)
    print("User Frequency:", userFrequency)
    print("Top Users:", topUsers(userFrequency, 3))
    print("Top Transactions:", topTransactions(transactions, 3))
    print("Suspicious:", suspicious)


display("task2.log")