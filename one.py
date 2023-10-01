import csv
import logging

SECTIONS = dict(SECURITY=['работ', 'серви'],
                REFUNDS=['верну', 'возвр', 'деньг'],
                TROUBLESHOOTING=['пробл', 'ошибк', 'непра', 'забыл', 'баг'],
                ACCOUNT=['аккау', 'учетн', 'подпи', 'автор', 'логин'],
                ADVERTISING_AND_COLLABORATION=['сотру', 'рекла'],
                LIMIT=['лимит', 'огран', 'увели'],
                PAYMENTS=['плате', 'оплат', 'средс'],
                FEATURES=['функц'])


def logger():
    logging.basicConfig(filename="log.log", encoding='utf-8', level=logging.INFO, format="%(message)s")


def sorter(rows: list, selections: dict):
    logger()
    for key, items in selections.items():
        dictor = []
        for number, message in rows:
            word = [word[:5].lower() for word in message[0].split()]

            if set(word) & set(items):
                if [number, message] not in dictor:

                    dictor.append({"number": str(number),
                                   "message": "".join(message)})

                    with open(f"{key}.csv", "w", encoding="utf-8", newline="") as file:
                        fieldnames = ['number', 'message']

                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        for line in dictor:
                            writer.writerow(line)
            else:
                error_msg = f"{number} - {''.join(message)} \n"
                logging.info(msg=error_msg)


with open("user_support_letters.csv", "r", encoding="utf-8") as f:
    data = []
    for num, row in enumerate(csv.reader(f), start=1):
        data.append([num, row])

sorter(data, SECTIONS)

if __name__ == '__main__':
    sorter(data, SECTIONS)