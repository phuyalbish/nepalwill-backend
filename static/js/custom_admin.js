document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const activeLink = document.querySelector('.sidebar .nav-link.active');
        if (activeLink) {
            activeLink.scrollIntoView({ behavior:'smooth', block: 'center' }); 
        }
    }, 100); 
});
