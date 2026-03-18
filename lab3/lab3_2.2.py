# 2
def filter_words(words):
    for w in words:
        if len(w) > 4:
            yield "c a" if "a" in w else w


words = ["кот", "машина", "арбуз", "дом"]
print(list(filter_words(words)))
#2
def filter_words(words):
    for w in words:
        # 1-шарт: сөздің ұзындығы 4-тен үлкен болуы керек
        if len(w) > 4:
            # 2-шарт: егер ішінде "а" болса "с а" қайтарады, әйтпесе сөздің өзін
            yield "с а" if "а" in w else w

words = ["кот", "машина", "арбуз", "дом"]
# Генераторды тізімге айналдырып шығарамыз
print(list(filter_words(words)))