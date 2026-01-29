// HTMX Global Configuration & Error Logging
document.addEventListener('DOMContentLoaded', () => {
    console.log('Canyon Intel: App initialized');

    // Global HTMX Error Listener
    document.body.addEventListener('htmx:responseError', (event) => {
        const xhr = event.detail.xhr;
        console.error(`HTMX Response Error: ${xhr.status} - ${xhr.statusText}`);
        console.error('Target Container:', event.detail.target);

        // Optionally show a toast for 500 errors
        if (xhr.status >= 500) {
            if (typeof showToast === 'function') {
                showToast(`Server Error (${xhr.status}). Please try again later.`, 'danger');
            }
        }
    });

    // Log HTMX Out-of-Band Swaps
    document.body.addEventListener('htmx:oobAfterSwap', (event) => {
        console.log('HTMX: OOB Swap performed on', event.detail.target);
    });

    // Indicator logic if needed beyond class-based
    document.body.addEventListener('htmx:beforeRequest', (event) => {
        // console.log('HTMX: Request starting...', event.detail.pathInfo.path);
    });
});
