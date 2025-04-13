// Custom JavaScript for Flask Portfolio

document.addEventListener('DOMContentLoaded', function() {
    // Add fade-in animation to sections
    const sections = document.querySelectorAll('section');
    
    // Create an intersection observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target); // Stop observing once animation is triggered
            }
        });
    }, {
        root: null, // viewport
        threshold: 0.1, // 10% of the item is visible
        rootMargin: '0px'
    });
    
    // Observe each section
    sections.forEach(section => {
        observer.observe(section);
    });
    
    // Handle form submission with validation
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            let valid = true;
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const messageInput = document.getElementById('message');
            
            // Simple validation
            if (nameInput.value.trim() === '') {
                valid = false;
                highlightInvalid(nameInput);
            } else {
                removeHighlight(nameInput);
            }
            
            if (emailInput.value.trim() === '' || !isValidEmail(emailInput.value)) {
                valid = false;
                highlightInvalid(emailInput);
            } else {
                removeHighlight(emailInput);
            }
            
            if (messageInput.value.trim() === '') {
                valid = false;
                highlightInvalid(messageInput);
            } else {
                removeHighlight(messageInput);
            }
            
            if (!valid) {
                e.preventDefault();
            }
        });
    }
    
    // Email validation helper
    function isValidEmail(email) {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
    
    // Form validation helpers
    function highlightInvalid(element) {
        element.classList.add('is-invalid');
    }
    
    function removeHighlight(element) {
        element.classList.remove('is-invalid');
    }
    
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Initialize tooltips if Bootstrap is loaded
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});


// Dans votre fichier main.js ou dans un bloc script
document.querySelectorAll('.skill-title').forEach(title => {
    title.addEventListener('click', function() {
        // Ajoute une rotation à l'icône (si vous en ajoutez une)
        const icon = this.querySelector('i');
        if (icon) {
            icon.classList.toggle('rotate-90');
        }
    });
});