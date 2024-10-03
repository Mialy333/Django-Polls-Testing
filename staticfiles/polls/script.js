document.addEventListener('DOMContentLoaded', function () {
    const questions = document.querySelectorAll('.question-list li');
    const questionList = document.querySelector('.question-list');

    // Clone les questions pour une boucle infinie
    const clone = questionList.cloneNode(true);
    questionList.appendChild(clone);

    // Appliquer la classe active à la première question
    questions[0].classList.add('active');

    // Ajuste la vitesse de l'animation si nécessaire
    questionList.style.animationDuration = '20s'; // Ajuste cette valeur pour contrôler la vitesse
});
