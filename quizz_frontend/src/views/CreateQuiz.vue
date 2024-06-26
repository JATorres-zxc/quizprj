<template>
    <div class="min-h-screen flex flex-col items-center bg-gray-100 p-6">
        <!-- Top Controls -->
        <div class="w-full max-w-5xl flex items-center justify-between mb-4 p-4 bg-white shadow-lg rounded-lg">
            <button class="px-4 py-2 bg-purple-500 text-white rounded-lg" @click="saveQuestions">Save all questions</button>
        </div>

        <!-- Question and Answers Section -->
        <form v-for="(question, qIndex) in questions" :key="qIndex" class="w-full max-w-5xl bg-white shadow-lg rounded-lg p-6 mb-6">
            <!-- Question Area -->
            <div class="mb-6 p-4 bg-purple-900 text-white rounded-lg">
                <textarea v-model="question.text" class="w-full bg-purple-900 text-white border focus:outline-none p-1" rows="3" placeholder="Type question here"></textarea>
            </div>

            <!-- Answer Options -->
            <div class="grid grid-cols-4 gap-4">
                <div v-for="(answer, aIndex) in question.answers" :key="aIndex" class="flex flex-col items-center p-4 bg-blue-600 text-white rounded-lg">
                    <textarea v-model="answer.text" class="w-full bg-blue-600 text-white border focus:outline-none p-1" rows="2" placeholder="Type answer option here"></textarea>
                    <button class="mt-2 bg-gray-200 p-1 rounded-lg" @click="deleteAnswer(qIndex, aIndex)">Delete</button>
                </div>
            </div>

            <!-- Answer Type Buttons -->
            <div class="mt-6 flex justify-center space-x-4">
                <button class="px-4 py-2 bg-gray-200 rounded-lg" @click="setSingleCorrectAnswer(qIndex)">Single correct answer</button>
                <button class="px-4 py-2 bg-gray-200 rounded-lg" @click="setMultipleCorrectAnswers(qIndex)">Multiple correct answers</button>
            </div>
        </form>

        <!-- Add New Question -->
        <div class="mt-6 flex justify-center space-x-4">
            <button class="px-4 py-2 bg-gray-200 rounded-lg" @click="addQuestion">Add question</button>
        </div>

        <div>
            hehe
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            questions: [
                {
                    text: 'Type question here',
                    answers: [
                        { id: 1, text: 'Type answer option here' },
                        { id: 2, text: 'Type answer option here' },
                        { id: 3, text: 'Type answer option here' },
                        { id: 4, text: 'Type answer option here' }
                    ],
                    questionType: 'MCQ'
                }
            ],
            quizId: 1 // This should be dynamically set based on the quiz being edited
        };
    },
    methods: {
        saveQuestions() {
            this.questions.forEach((question, index) => {
                const payload = {
                    text: question.text,
                    question_type: question.questionType,
                    answers: question.answers.map(answer => answer.text)
                };
                console.log(`Question ${index + 1}:`, payload);
                // Uncomment the fetch request below to send data to the backend
                /*
                fetch(`/question/save/${this.quizId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': this.getCSRFToken()
                    },
                    body: JSON.stringify(payload)
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        alert(`Question ${index + 1} saved successfully!`);
                    } else {
                        alert(`Error saving question ${index + 1}`);
                    }
                });
                */
            });
        },
        addQuestion() {
            this.questions.push({
                text: 'Type question here',
                answers: [
                    { id: 1, text: 'Type answer option here' },
                    { id: 2, text: 'Type answer option here' },
                    { id: 3, text: 'Type answer option here' },
                    { id: 4, text: 'Type answer option here' },
                ],
                questionType: 'MCQ'
            });
        },
        deleteAnswer(questionIndex, answerIndex) {
            this.questions[questionIndex].answers.splice(answerIndex, 1);
        },
        setSingleCorrectAnswer(questionIndex) {
            this.questions[questionIndex].questionType = 'SA';
        },
        setMultipleCorrectAnswers(questionIndex) {
            this.questions[questionIndex].questionType = 'MCQ';
        },
        getCSRFToken() {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, 10) === 'csrftoken=') {
                        cookieValue = decodeURIComponent(cookie.substring(10));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    }
};
</script>
