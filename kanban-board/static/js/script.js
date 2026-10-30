function filterCards() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        const title = card.querySelector('h4').textContent.toLowerCase();
        const description = card.querySelector('.card-description')?.textContent.toLowerCase() || '';
        const tags = card.querySelector('.tags')?.textContent.toLowerCase() || '';
        
        const matchesSearch = title.includes(searchTerm) || 
                             description.includes(searchTerm) || 
                             tags.includes(searchTerm);
        
        card.style.display = matchesSearch ? 'block' : 'none';
    });
}

// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-messages > div');
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.display = 'none';
        }, 5000);
    });
});
