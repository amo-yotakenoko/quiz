document.addEventListener('DOMContentLoaded', (event) => {
    // Check if the user is logged in
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';

    if (!isLoggedIn && window.location.pathname !== '/login.html' && window.location.pathname !== '/create_account.html') {
        window.location.href = 'login.html';
    }

    // Display theme list in index.html
    if (window.location.pathname.includes('index.html')) {
        const themeList = document.getElementById('theme-list');
        const themes = JSON.parse(localStorage.getItem('themes')) || [];
        themes.forEach(theme => {
            const li = document.createElement('li');
            li.textContent = `${theme.name} (開かれた回数: ${theme.opens || 0})`;
            li.addEventListener('click', () => {
                theme.opens = (theme.opens || 0) + 1;
                localStorage.setItem('themes', JSON.stringify(themes));
                window.location.href = `answer_question.html?theme=${theme.name}`;
            });
            themeList.appendChild(li);
        });
    }

    // Handle form submission in create_question.html
    if (window.location.pathname.includes('create_question.html')) {
        const form = document.getElementById('create-question-form');
        const addQuestionButton = document.getElementById('add-question');
        const questionFieldsContainer = document.getElementById('question-fields');
        let questionCount = 1;

        // Add new question fields
        addQuestionButton.addEventListener('click', () => {
            questionCount++;
            const questionBlock = document.createElement('div');
            questionBlock.className = 'question-block';
            questionBlock.innerHTML = `
                <label for="question-${questionCount}">問題:</label>
                <textarea id="question-${questionCount}" name="questions[]" required></textarea>
                <label for="answer-${questionCount}">回答:</label>
                <input type="text" id="answer-${questionCount}" name="answers[]" required>
            `;
            questionFieldsContainer.appendChild(questionBlock);
        });

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const theme = document.getElementById('theme').value;
            const questions = Array.from(document.querySelectorAll('textarea[name="questions[]"]')).map(q => q.value);
            const answers = Array.from(document.querySelectorAll('input[name="answers[]"]')).map(a => a.value);

            let themes = JSON.parse(localStorage.getItem('themes')) || [];
            let themeObj = themes.find(t => t.name === theme);
            if (!themeObj) {
                themeObj = { name: theme, opens: 0, correct: 0, incorrect: 0, questions: [] };
                themes.push(themeObj);
            }
            themeObj.questions = questions.map((question, index) => ({ question, answer: answers[index] }));
            localStorage.setItem('themes', JSON.stringify(themes));
            localStorage.setItem('currentTheme', JSON.stringify(themeObj));
            window.location.href = 'answer_question.html';
        });
    }

    // Handling answer in answer_question.html
    if (window.location.pathname.includes('answer_question.html')) {
        const form = document.getElementById('answer-form');
        const themeElement = document.getElementById('quiz-theme');
        const questionsContainer = document.getElementById('questions-container');
        const resultElement = document.getElementById('result');
        const statisticsElement = document.getElementById('statistics');

        const themeObj = JSON.parse(localStorage.getItem('currentTheme'));

        if (themeObj && themeElement) {
            themeElement.innerText = `テーマ: ${themeObj.name}`;
        }

        if (themeObj && themeObj.questions) {
            themeObj.questions.forEach((q, index) => {
                const questionBlock = document.createElement('div');
                questionBlock.className = 'question-block';
                questionBlock.innerHTML = `
                    <p>${q.question}</p>
                    <input type="text" id="answer-${index}" name="user-answers[]" required>
                `;
                questionsContainer.appendChild(questionBlock);
            });
        }

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const userAnswers = Array.from(document.querySelectorAll('input[name="user-answers[]"]')).map(a => a.value);
            let resultHTML = '';
            let correctCount = 0;

            userAnswers.forEach((answer, index) => {
                const correctAnswer = themeObj.questions[index].answer;
                if (answer.toLowerCase() === correctAnswer.toLowerCase()) {
                    resultHTML += `<p>問題 ${index + 1}: 〇</p>`;
                    correctCount++;
                    themeObj.correct = (themeObj.correct || 0) + 1;
                } else {
                    resultHTML += `<p>問題 ${index + 1}: × (正解は: ${correctAnswer})</p>`;
                    themeObj.incorrect = (themeObj.incorrect || 0) + 1;
                }
            });

            localStorage.setItem('themes', JSON.stringify(JSON.parse(localStorage.getItem('themes')).map(t => t.name === themeObj.name ? themeObj : t)));

            resultElement.innerHTML = resultHTML;
            statisticsElement.innerHTML = `<p>正解数: ${themeObj.correct || 0}</p><p>不正解数: ${themeObj.incorrect || 0}</p>`;
        });
    }

    // Handle login in login.html
    if (window.location.pathname.includes('login.html')) {
        const form = document.getElementById('login-form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // Here you would typically verify the username and password with the server
            localStorage.setItem('isLoggedIn', 'true');
            window.location.href = 'index.html';
        });
    }

    // Handle create account in create_account.html
    if (window.location.pathname.includes('create_account.html')) {
        const form = document.getElementById('create-account-form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const newUsername = document.getElementById('new-username').value;
            const newPassword = document.getElementById('new-password').value;
            // Here you would typically save the new username and password to the server or localStorage
            alert(`新しいアカウントが作成されました。\nユーザーID: ${newUsername}\nパスワード: ${newPassword}`);
            window.location.href = 'login.html';
        });
    }

    // Handle logout
    const logoutLink = document.getElementById('logout-link');
    if (logoutLink) {
        logoutLink.addEventListener('click', () => {
            localStorage.setItem('isLoggedIn', 'false');
            window.location.href = 'login.html';
        });
    }
});
