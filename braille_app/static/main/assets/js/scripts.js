// document.addEventListener('DOMContentLoaded', function() {
//     const loader = document.getElementById('loader');
//     const overlay = document.getElementById('loader-overlay');

//     function showLoader() {
//         loader.style.display = 'flex'; // Show the loader
//         overlay.style.display = 'block'; // Show the blurred overlay
//         document.body.classList.add('loading'); // Add 'loading' class to body
//     }

//     function hideLoader() {
//         loader.style.display = 'none'; // Hide the loader
//         overlay.style.display = 'none'; // Hide the blurred overlay
//         document.body.classList.remove('loading'); // Remove 'loading' class from body
//     }

//     // Show loader on form submission
//     document.querySelectorAll('form').forEach(form => {
//         form.addEventListener('submit', function() {
//             showLoader();
//         });
//     });

//     // Show loader when navigating to a new page
//     window.addEventListener('beforeunload', function() {
//         showLoader();
//     });

//     // Example: Hiding the loader when the page fully loads (you can modify this logic)
//     window.addEventListener('load', function() {
//         hideLoader();
//     });
// });


document.addEventListener('DOMContentLoaded', function() {
    const loader = document.getElementById('loader');
    const overlay = document.getElementById('loader-overlay');

    function showLoader() {
        loader.style.display = 'block'; // Show the loader
        overlay.style.display = 'block'; // Show the blurred overlay
        document.body.classList.add('loading'); // Add 'loading' class to body for blurring content
    }

    function hideLoader() {
        loader.style.display = 'none'; // Hide the loader
        overlay.style.display = 'none'; // Hide the blurred overlay
        document.body.classList.remove('loading'); // Remove 'loading' class from body
    }

    // Example: Show loader when form is submitted
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            showLoader();
        });
    });

    // Example: Show loader on page navigation or refresh
    window.addEventListener('beforeunload', function() {
        showLoader();
    });

    // Example: Hide loader when page has fully loaded
    window.addEventListener('load', function() {
        hideLoader();
    });
});
