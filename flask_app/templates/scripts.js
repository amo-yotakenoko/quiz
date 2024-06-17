document.addEventListener('DOMContentLoaded', (event) => {
    // Check if the user is logged in
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';

    if (!isLoggedIn && window.location.pathname !== '/login.html') {
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

    // Theme setting in create_question.html
    const urlParams = new URLSearchParams(window.location.search);
    const themeName = urlParams.get('theme');
    if (themeName && document.getElementById('theme')) {
        document.getElementById('theme').value = themeName;
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
            let themeObj = themes.find(t => t.name === theme);
            if (!themeObj) {
                themeObj = { name: theme, opens: 0, correct: 0, incorrect: 0 };
                themes.push(themeObj);
            }
            localStorage.setItem('themes', JSON.stringify(themes));
            localStorage.setItem('currentTheme', JSON.stringify(themeObj));
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
        const statisticsElement = document.getElementById('statistics');

        const question = localStorage.getItem('question');
        const answer = localStorage.getItem('answer');
        const themeObj = JSON.parse(localStorage.getItem('currentTheme'));

        if (themeObj && themeElement) {
            themeElement.innerText = `テーマ: ${themeObj.name}`;
        }
        if (question && questionElement) {
            questionElement.innerText = question;
        }

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const userAnswer = document.getElementById('user-answer').value;
            if (userAnswer.toLowerCase() === answer.toLowerCase()) {
                resultElement.innerHTML = '<p>正解！</p>';
                themeObj.correct = (themeObj.correct || 0) + 1;
            } else {
                resultElement.innerHTML = '<p>不正解！正解は ' + answer + ' です。</p>';
                themeObj.incorrect = (themeObj.incorrect || 0) + 1;
            }
            localStorage.setItem('themes', JSON.stringify(JSON.parse(localStorage.getItem('themes')).map(t => t.name === themeObj.name ? themeObj : t)));

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

    // Handle logout
    const logoutLink = document.getElementById('logout-link');
    if (logoutLink) {
        logoutLink.addEventListener('click', () => {
            localStorage.setItem('isLoggedIn', 'false');
        });
    }
});
