document.addEventListener('DOMContentLoaded', function() {
    // Add click event to toggle card details
    const cards = document.querySelectorAll('.post-card');
    cards.forEach(card => {
        card.addEventListener('click', function() {
            this.classList.toggle('expanded');
        });
    });

    // Example interaction: toggle button text
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.innerText === 'Click Me') {
                this.innerText = 'Clicked!';
            } else {
                this.innerText = 'Click Me';
            }
        });
    });
});
