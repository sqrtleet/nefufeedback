import pymongo


class Feedback:
    def __init__(self, *args):
        (self.id, self.user_id, self.user_nickname, self.text, self.rating, self.date_time, self.tags, self.file_id,
         self.status) = args


def create_feedbacks():
    feedbacks = [
        Feedback(1, 1, 'plam', 'Не работает клавиатура в ауд. 424', 2, '24.04.24', ['кфен', 'техника'], 'file_id1',
                 'на рассмотрении'),
        Feedback(2, 2, 'sypyx', 'Не работает смыв в туалете', 5, '25.04.24', ['кфен', 'туалет'], 'file_id2',
                 'на рассмотрении'),
        Feedback(3, 3, 'kronter', 'Сломаны стулья в ауд. 518', 3, '26.04.24', ['кфен', 'мебель'],
                 ['file_id3', 'file_id4'],
                 'на рассмотрении')
    ]

    for feedback in feedbacks:
        col.insert_one(
            {"id": feedback.id, "user_id": feedback.user_id, "user_nickname": feedback.user_nickname,
             "text": feedback.text,
             "rating": feedback.rating, "date_time": feedback.date_time, "tags": feedback.tags,
             "file_id": feedback.file_id,
             "status": feedback.status}
        )


if __name__ == '__main__':
    """
    Это только для создания записей в бд
    """
    local = 'mongodb://localhost:27017'
    server = f"mongodb://test:test@test:27017/"
    client = pymongo.MongoClient(server)
    db = client['test']
    col = db['feedbacks']
    create_feedbacks()
