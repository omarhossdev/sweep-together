// HTMX configuration
document.body.addEventListener('htmx:configRequest', (event) => {
    // Add CSRF or other headers here if needed
});

// Handle 303 redirects from HTMX (auth redirects)
document.body.addEventListener('htmx:beforeSwap', (event) => {
    if (event.detail.xhr.status === 303) {
        window.location.href = event.detail.xhr.getResponseHeader('Location');
    }
});
