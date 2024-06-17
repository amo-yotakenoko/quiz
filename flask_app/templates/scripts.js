document.addEventListener('DOMContentLoaded', (event) => {
    // Display theme list in index.html
    if (window.location.pathname.includes('index.html') || window.location.pathname === '/') {
        const themeList = document.getElementById('theme-list');
        const themes = JSON.parse(localStorage.getItem('themes')) || [];
        themes.forEach(theme => {
            const li = document.createElement('li');
            li.textContent = theme;
            li.addEventListener('click', () => {
                window.location.href = `create_question.html?theme=${theme}`;
            });
            themeList.appendChild(li);
        });
    }

    // Theme setting in create_question.html
    const urlParams = new URLSearchParams(window.location.search);
    const theme = urlParams.get('theme');
    if (theme && document.getElementById('theme')) {
        document.getElementById('theme').value = theme;
    }

    // Handle form submission in create_question.html
    if (window.location.pathname.includes('create_question.html')) {
        const form = document.getElementById('create-question-form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const theme = document.getElementById('theme').value;
            const question = document.getElementById('question').value;
            const answer = document.getElementById('answer').value;

            let themes = JSON.parse(localStorage.getItem('themes')) || [];
            if (!themes.includes(theme)) {
                themes.push(theme);
            }
            localStorage.setItem('themes', JSON.stringify(themes));
            localStorage.setItem('theme', theme);
            localStorage.setItem('question', question);
            localStorage.setItem('answer', answer);
            window.location.href = 'answer_question.html';
        });
    }

    // Handling answer in answer_question.html
    if (window.location.pathname.includes('answer_question.html')) {
        const form = document.getElementById('answer-form');
        const themeElement = document.getElementById('quiz-theme');
        const questionElement = document.getElementById('quiz-question');
        const resultElement = document.getElementById('result');

        const question = localStorage.getItem('question');
        const answer = localStorage.getItem('answer');
        const theme = localStorage.getItem('theme');

        if (theme && themeElement) {
            themeElement.innerText = `テーマ: ${theme}`;
        }
        if (question && questionElement) {
            questionElement.innerText = question;
        }

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const userAnswer = document.getElementById('user-answer').value;
            if (userAnswer === answer) {
                resultElement.innerHTML = '<p style="color: green;">正解です！</p>';
            } else {
                resultElement.innerHTML = '<p style="color: red;">不正解です。正解は ' + answer + ' です。</p>';
            }
        });
    }
});
