db.mcq_test_app_student.insertMany([
    {id: 1, name: "student 1", age: 20, phone: "01015529890"},
    {id: 2, name: "student 2", age: 21, phone: "01015529891"},
    {id: 3, name: "student 3", age: 22, phone: "01015529892"},
]);

db.mcq_test_app_topic.insertMany([
    {id: 1, name: "topic 1", desc: "topic 1"},
    {id: 2, name: "topic 2", desc: "topic 2"},
    {id: 3, name: "topic 3", desc: "topic 3"},
]);

db.mcq_test_app_question.insertMany([
    {id: 1, content: "question 1", topic: 1},
    {id: 2, content: "question 2", topic: 1},
    {id: 3, content: "question 3", topic: 1},

    {id: 4, content: "question 1", topic: 2},
    {id: 5, content: "question 2", topic: 2},
    {id: 6, content: "question 3", topic: 2},

    {id: 7, content: "question 1", topic: 3},
    {id: 8, content: "question 2", topic: 3},
    {id: 9, content: "question 3", topic: 3},
]);

db.mcq_test_app_answer.insertMany([
    {id: 1, content: "answer 1", question: 1, correct: 1},
    {id: 2, content: "answer 2", question: 1, correct: 0},
    {id: 3, content: "answer 3", question: 1, correct: 0},

    {id: 4, content: "answer 1", question: 2, correct: 1},
    {id: 5, content: "answer 2", question: 2, correct: 0},
    {id: 6, content: "answer 3", question: 2, correct: 0},

    {id: 7, content: "answer 1", question: 3, correct: 1},
    {id: 8, content: "answer 2", question: 3, correct: 0},
    {id: 9, content: "answer 3", question: 3, correct: 0},


    {id: 10, content: "answer 1", question: 4, correct: 1},
    {id: 11, content: "answer 2", question: 4, correct: 0},
    {id: 12, content: "answer 3", question: 4, correct: 0},

    {id: 13, content: "answer 1", question: 5, correct: 1},
    {id: 14, content: "answer 2", question: 5, correct: 0},
    {id: 15, content: "answer 3", question: 5, correct: 0},

    {id: 16, content: "answer 1", question: 6, correct: 1},
    {id: 17, content: "answer 2", question: 6, correct: 0},
    {id: 18, content: "answer 3", question: 6, correct: 0},


    {id: 19, content: "answer 1", question: 7, correct: 1},
    {id: 20, content: "answer 2", question: 7, correct: 0},
    {id: 21, content: "answer 3", question: 7, correct: 0},

    {id: 22, content: "answer 1", question: 8, correct: 1},
    {id: 23, content: "answer 2", question: 8, correct: 0},
    {id: 24, content: "answer 3", question: 8, correct: 0},

    {id: 25, content: "answer 1", question: 9, correct: 1},
    {id: 26, content: "answer 2", question: 9, correct: 0},
    {id: 27, content: "answer 3", question: 9, correct: 0},

]);
